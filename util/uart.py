import datetime
import serial

import time

from firebase_manager import pushData

ser = serial.Serial('/dev/ttyS0', 115200, timeout=2)
while True:
    ser.write(b'hello\n')
    r = ser.readline()
    r = r.decode('utf-8')
    # ser.write(b'hello\n')
    angle = r.split(',')[0]
    motor0 = r.split(',')[1]
    motor1 = r.split(',')[2]
    motor2 = r.split(',')[3]
    motor3 = r.split(',')[4]
    print(f'angle: {angle}, motor0: {motor0}, motor1: {motor1}, motor2: {motor2}, motor3: {motor3}')
    pushData({
        u'angle': angle,
        u'motor0': motor0,
        u'motor1': motor1,
        u'motor2': motor2,
        u'motor3': motor3,
        u'time': datetime.datetime.now()
    })
    time.sleep(1)