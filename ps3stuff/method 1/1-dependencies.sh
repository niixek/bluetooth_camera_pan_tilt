#!/bin/bash
# It's good practice to run update prior to any installation session.
sudo apt-get update &&

# The && bit is like hitting return to execute a command.

# This script is for installing some purpose built programs to be able to
# use a PS3 six axis controller. In linux, a lot of programs use common
# background drivers and programmes. These are known as *dependencies*.
# We're now going to install these dependencies.

sudo apt-get -y install bluez-utils bluez-compat bluez-hcidump libbluetooth-dev libusb-dev joystick checkinstall 
