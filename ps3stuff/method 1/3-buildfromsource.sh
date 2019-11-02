#!/bin/bash/

# First we make sure we're in the right directory /home/pi/PS3control
cd /home/pi/PS3control &&

# Now we can go to a folder which was extracted from a previous download
cd QtSixA-1.5.1/sixad/ &&

# We need to create a directory for sixad profiles
sudo mkdir -p /var/lib/sixad &&
sudo mkdir -p /var/lib/sixad/profiles &&

# The make command will create instalable files for the next step
make &&

# Now we are ready to install the software you've just compiled
sudo checkinstall
