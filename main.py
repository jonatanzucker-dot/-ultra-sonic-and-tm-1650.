from machine import Pin, I2C, time_pulse_us
from tm1650 import TM1650
import time

trig = Pin(13, Pin.OUT)   #הגדרת פינים
echo = Pin(12, Pin.IN)
i2c = I2C(0, scl=Pin(22), sda=Pin(23))
disp = TM1650(i2c, brightness=5)

def read_distance():#יצירת פונציה שתעזור לכתוב את קוד
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    d = time_pulse_us(echo, 1, 30000)
    return d * 0.0343 / 2

while True:
    x = read_distance()#יצירת משנה

    if x > 0:
        print(int(x))
        disp.display(str(int(x)))#מראה את הערכים בtm1650

    time.sleep(0.3)
    
    


