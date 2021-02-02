import time
import serial


ser = serial.Serial()
ser.baudrate = 2400
ser.port = 'COM1'
ser.open()
ser.write(str("88888888").encode("latin_1"))
for i in range (1):
    ser.write(str(i).encode("latin_1"))
    time.sleep(1)
while True:
    day = time.strftime("%d", time.localtime())
    month = time.strftime("%m", time.localtime())
    year = time.strftime("%Y", time.localtime())
    sec = time.strftime("%S", time.localtime())
    minu = time.strftime("%M", time.localtime())
    hour = time.strftime("%H", time.localtime())
    out = str(day)+str(hour)+str(minu)+str(sec)
    ser.write(str(out).encode("latin_1"))
    time.sleep(0.07)

    
    
