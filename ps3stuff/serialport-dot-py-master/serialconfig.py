# Author:  Adam Anderson
# Depends on:  Python 3.3
# Created:  February 12, 2012
# Updated:  March 31st, 2013

import configparser

class SerialConfig(object):
    """ A class that contains all the config properties for Serial communication
        with the Arduino.
    """
    
    def __init__(self, configName='serial', configFileName='config.cfg'):
        """ Constructs anew instance of SerialConfig.
            
            Param:
                configName:  The name of the section of the config file to read 
                in the serial config data from.  Default value is 'serial' if no
                other value is specified.
        """
        # Create a config parser and read in the properties
        config = configparser.RawConfigParser()
        config.read(configFileName)
        self.configName = configName

        # The serial port's identifier (this is '/dev/tty/AM0' on Unix-like systems or 'COM4' on windows systems)
        self.port = config.get(self.configName, 'port')

        # The baudrate to use for serial communications.
        self.baud = config.getint(self.configName, 'baud')

        # The 'go-ahead' byte configured, if any.  When the serial port
        # receives this byte it knows its okay to transmit more bytes to
        # the target device.
        self.readybyte = config.getint(self.configName, 'readybyte')
    
        # the configured 'wait byte', if any.  When the SerialPort gets
        # this byte it waits until receiving the readbyte before continuing
        # to xmit more data.
        self.waitbyte = config.getint(self.configName, 'waitbyte')
