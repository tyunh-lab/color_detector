import datetime
import serial

ser = serial.Serial('/dev/ttyS0', 115200, timeout=2)
while True:
    r = ser.readline()
    # ser.write(b'hello\n')
    angle = r.split(',')[0]
    motor0 = r.split(',')[1]
    motor1 = r.split(',')[2]
    motor2 = r.split(',')[3]
    motor3 = r.split(',')[4]
    print(f'angle: {angle}, motor0: {motor0}, motor1: {motor1}, motor2: {motor2}, motor3: {motor3}')