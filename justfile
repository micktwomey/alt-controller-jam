circuitpython_version := "8.2.7"
circuitpython_mount := "/Volumes/CIRCUITPY"
firmware_mount := "/Volumes/RPI-RP2"
tmp := env_var_or_default("TMPDIR", "/tmp")
builddir := join(tmp, "circuitpython")

default: help

help:
    @just --list

# List possible serial ports for the circuitpython board
list-serial-ports:
    ls -lart /dev/tty.usbmodem*

# Connect to the circuitpython REPL
repl serial_port:
    screen -R -S repl {{ serial_port }} 115200

# Run all lint steps
lint: black ruff mypy shellcheck

black:
    poetry run black src
    poetry run black boards

ruff:
    poetry run ruff check src
    poetry run ruff check boards

mypy:
    poetry run mypy --ignore-missing-imports src
    poetry run mypy --ignore-missing-imports boards

shellcheck:
    just shellcheck-target build
    just shellcheck-target deploy
    just shellcheck-target install-firmware
    just shellcheck-target reset

shellcheck-target target:
    @echo {{ target }}
    just -n {{ target }} > {{ tmp }}/just-{{ target }}.sh 2>&1
    shellcheck {{ tmp }}/just-{{ target }}.sh
    rm {{ tmp }}/just-{{ target }}.sh

# Eject the circuitpython disk
eject mount=circuitpython_mount:
    diskutil eject {{ mount }}

# Build folder tree suitable for syncing onto circuitpython board
build dest=builddir:
    #!/bin/bash
    set -euo pipefail
    if [ -d "{{ dest }}" ]; then
        rm -rf {{ dest }}
    fi
    mkdir -p {{ dest }}/lib
    poetry run pipkin -m {{ dest }} install .
    rm -r {{ dest }}/lib/*.dist-info
    cp boards/circuitpython/boot.py {{ dest }}/boot.py
    cp boards/circuitpython/code.py {{ dest }}/code.py

# Sync files onto circuitpython board
deploy build=builddir mount=circuitpython_mount:
    #!/bin/bash
    set -euo pipefail

    if [ ! -d {{ circuitpython_mount }} ]; then
        echo "Can't find circuitpython folder. Is it connected?"
        exit 1
    fi

    rsync -avP {{ build }}/ {{ circuitpython_mount }}/

# Download and install the circuitpython uf2 onto the board
install-firmware circuitpython_mount=circuitpython_mount firmware_mount=firmware_mount version=circuitpython_version:
    #!/bin/bash
    set -euo pipefail

    if [ ! -d {{ firmware_mount }} ]; then
        echo "Can't find RPI-RP2 folder. Is it connected and did you hold down bootsel when plugging in?"
        exit 1
    fi

    VERSION={{ circuitpython_version }}
    echo "Installing Circuitpython ${VERSION}"

    UF2_FILENAME="adafruit-circuitpython-raspberry_pi_pico-en_US-${VERSION}.uf2"
    UF2_URL="https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/${UF2_FILENAME}"

    if [ ! -f "{{ tmp }}/${UF2_FILENAME}" ]; then
        echo "Downloading ${UF2_FILENAME} from ${UF2_URL}"
        curl -o "{{ tmp }}/${UF2_FILENAME}" "${UF2_URL}"
    fi

    echo "Copying to Pico"
    cp "{{ tmp }}/${UF2_FILENAME}" {{ firmware_mount }}/
    sync

    while true; do
        if [ -d "{{ circuitpython_mount }}" ]; then
            echo "Installation complete"
            exit 0
        fi
        echo "Waiting for circuitpython volume to appear..."
        sleep 5
    done

# Attempt to reset the circuitpython folders to a clean state
reset mount=circuitpython_mount:
    #!/bin/bash
    set -euo pipefail

    if [ ! -d {{ circuitpython_mount }} ]; then
        echo "Can't find circuitpython folder. Is it connected?"
        exit 1
    fi

    rm -rfv {{ circuitpython_mount }}/lib/*
    rm {{ circuitpython_mount }}/boot.py
    cat >> {{ circuitpython_mount }}/code.py <<EOF
    print("Hello, world!")
    EOF

# Watch status of firmware and circuitpython mounts
watch circuitpython_mount=circuitpython_mount firmware_mount=firmware_mount:
    #!/bin/bash
    set -euo pipefail

    while true; do
        clear
        date
        if [ -d "{{circuitpython_mount}}" ]; then
            echo "{{circuitpython_mount}} mounted"
        fi
        if [ -d "{{firmware_mount}}" ]; then
            echo "{{firmware_mount}} mounted"
        fi
        sleep 1
    done
