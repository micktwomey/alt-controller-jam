
default: lint

list-serial-ports:
  ls -lart /dev/tty.usbmodem*

repl serial_port:
  screen -R -S repl {{serial_port}} 115200

lint: black ruff mypy

black:
  poetry run black src
  poetry run black boards

ruff:
  poetry run ruff check src
  poetry run ruff check boards

mypy:
  poetry run mypy --ignore-missing-imports src
  poetry run mypy --ignore-missing-imports boards

eject-circuitpython:
  diskutil eject /Volumes/CIRCUITPY

deploy-circuitpython:
  #!/bin/bash
  set -euo pipefail

  if [ ! -d /Volumes/CIRCUITPY ]; then
    echo "Can't find circuitpython folder. Is it connected?"
    exit 1
  fi

  rsync -avP src/alt_controller_jam/ /Volumes/CIRCUITPY/lib/alt_controller_jam/
  poetry run pipkin -m /Volumes/CIRCUITPY install adafruit-circuitpython-hid==6.0.1
  cp boards/circuitpython/boot.py /Volumes/CIRCUITPY/boot.py
  cp boards/circuitpython/code.py /Volumes/CIRCUITPY/code.py

install-circuitpython:
  #!/bin/bash
  set -euo pipefail

  if [ ! -d /Volumes/RPI-RP2 ]; then
    echo "Can't find RPI-RP2 folder. Is it connected and did you hold down bootsel when plugging in?"
    exit 1
  fi

  VERSION=8.2.7
  echo "Installing Circuitpython ${VERSION}"

  UF2_FILENAME="adafruit-circuitpython-raspberry_pi_pico-en_US-${VERSION}.uf2"
  UF2_URL="https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/${UF2_FILENAME}"

  if [ ! -f "/tmp/${UF2_FILENAME}" ]; then
    echo "Downloading ${UF2_FILENAME} from ${UF2_URL}"
    curl -o "/tmp/${UF2_FILENAME}" "${UF2_URL}"
  fi

  echo "Copying to Pico"
  cp "/tmp/${UF2_FILENAME}" /Volumes/RPI-RP2/
  sync

  while true; do
    if [ -d "/Volumes/CIRCUITPY" ]; then
      echo "Installation complete"
      exit 0
    fi
    echo "Waiting for circuitpython volume to appear..."
    sleep 5
  done
