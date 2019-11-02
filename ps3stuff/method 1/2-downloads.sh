#!/bin/bash/

# Create a directory for all PS3 controller related work
mkdir ~/PS3control &&

# Ensure you are in the /home/pi/PS3control directory
cd ~/PS3control &&

# The script will download bluetooth pairing software using the WGET command.
wget http://www.pabr.org/sixlinux/sixpair.c &&

# Now, we can create an executeable file for pairing our bluetooth with the PS3 controller
gcc -o sixpair sixpair.c -lusb &&



# The next job is to download the source code for a program which can manage the PS3 sixaxis device.
# A few downloads are required but it shouldn't take long.
wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz &&

# Extract the downloaded file
tar xfvz QtSixA-1.5.1-src.tar.gz &&

# This software needs a patch applied. First we download the patch using WGET again
wget https://bugs.launchpad.net/qtsixa/+bug/1036744/+attachment/3260906/+files/compilation_sid.patch &&

# We can now apply the patch
patch ~/PS3control/QtSixA-1.5.1/sixad/shared.h < compilation_sid.patch
