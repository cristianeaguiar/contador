# importar biblioteca

import os
import time

# entrada de dados
n = int(input( "Informe um número inteiro positivo: "))

while n >= 0:
    os.system("cls")
    print(n)
    time.sleep(1)
    n -= 1
os.system("cls")
print("BOOM!!!")