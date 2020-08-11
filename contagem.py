import time
import sys
from datetime import datetime

c=':'

now = datetime.now()
horas_total = now.strftime("%H:%M:%S")
horas = now.strftime("%H")
minutos = now.strftime("%M")
segundos = now.strftime("%S")

h1 = int(horas)
m1 = int(minutos)
s1 = int(segundos)

hora = int(17)
minutos = int(30)
seg = int(0)

x1 = (hora-h1)
x2 = (minutos-m1)
x3 = (seg-s1)

hourz=x1
minz=x2
secz=(60 - (x3*-1))

hour=int(hourz)
min=int(minz)
sec=int(secz)

while hour > -1:
    while min > -1:
        while sec > 0:
            sec=sec-1
            time.sleep(1)
            sec1 = ('%02.f' % sec)  # format
            min1 = ('%02.f' % min)
            hour1 = ('%02.f' % hour)
            sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))

        min=min-1
        sec=60
    hour=hour-1
    min=59

print('\nCountdown Complete.')
time.sleep(30)