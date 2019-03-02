#!/usr/bin/python
# coding: utf-8
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

##### Insert the values manually #####
bit = 16 # ADS1115 is 16-bit.
RoV = 6.144 # The Range of Voltage. See the ranges below.
R1, R2 = 11000, 1000 # The value of the resistors. 

# These values are automatically calculated (DO NOT CHANGE)
voltage = 0 # voltage of the batteries.
step = 2**bit - 1 # Represents how much is the voltage devided.
C = (RoV*(R1+R2))/(step*R2) # This will be the coefficient equating like "voltage = C * digital value"

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2/3

voltage = C * adc.read_adc(0, gain=GAIN)
print(voltage)


