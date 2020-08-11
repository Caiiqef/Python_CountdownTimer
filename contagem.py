import time
import sys
from datetime import datetime

c=':'

now = datetime.now()
horas_total = now.strftime("%H:%M:%S") # Exibe o horário atual em String no formato H:M:S
horas = now.strftime("%H") # Exibe a hora atual
minutos = now.strftime("%M") # Exibe os minutos atuais
segundos = now.strftime("%S") # Exibe os segundos atuais

# Passando as varíaveis para valor int
h1 = int(horas) 
m1 = int(minutos)
s1 = int(segundos)

# Definindo o horário para finalizar o contador
hora = int(17)
minuto = int(30)
seg = int(0)

# Calculando a hora final menos a hora atual
x1 = (hora-h1)
x2 = (minuto-m1)
x3 = (seg-s1)

# Calculos para executar a contagem corretamente
hourz=(x1 - 1)
minz=(59 - (x2 * -1))
secz=(60 - (x3 * -1))

# Variaveis definidas como int
hour=int(hourz)
min=int(minz)
sec=int(secz)

# Calculos para o contador 
while hour > -1:
    while min > -1:
        while sec > 0:
            sec=sec-1
            time.sleep(1)
            sec1 = ('%02.f' % sec)  # formato de saída do horário com duas casas somente
            min1 = ('%02.f' % min)
            hour1 = ('%02.f' % hour)
            sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))

        min=min-1
        sec=60
    hour=hour-1
    min=59

# Mensagem de aviso ao terminar o contador.
print('\nCountdown Complete.')
time.sleep(30)