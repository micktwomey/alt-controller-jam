
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

deploy-circuitpython:
  #!/bin/bash
  set -eux pipefail

  if [ ! -d /Volumes/CIRCUITPY ]; then
    echo "Can't find circuitpython folder. Is it connected?"
    exit 1
  fi

  rsync -avP src/alt_controller_jam/ /Volumes/CIRCUITPY/lib/alt_controller_jam/
  poetry run pipkin -m /Volumes/CIRCUITPY install adafruit-circuitpython-hid
  cp boards/circuitpython/boot.py /Volumes/CIRCUITPY/boot.py
  cp boards/circuitpython/code.py /Volumes/CIRCUITPY/code.py
