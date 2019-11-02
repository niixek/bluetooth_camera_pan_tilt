# While this script was written to control a robot, the contents here are not isolated to this project
# and can be used for PS3 controller setup for any RPi project

# Ensure the controller is paired
sudo ./sixpair &&

# Now we can start the SIXAD PS3 controller manager
sudo sixad --start
