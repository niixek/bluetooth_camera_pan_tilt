import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])
    print msb, lsb

while True:
    #write_pot(0x66)
   # time.sleep(1)
    #write_pot(0xCC)
   # time.sleep(1)
    #write_pot(0x133)
   # time.sleep(1)
   # write_pot(0x199)
   # time.sleep(1)
    write_pot(0x1FF)
    time.sleep(1)
   # write_pot(0x00)
