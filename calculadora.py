#!/usr/bin/python3
#Parametros: python calculadora.py función operando1 operando2

import sys

if len(sys.argv) != 4:
    print("El numero de argumentos introducidos no es correcto")
    sys.exit()

operacion = sys.argv[1]
operando1 = sys.argv[2]
operando2 = sys.argv[3]

if operacion == "suma":
    print ("La operacion es una suma")
    resultado = int(operando1) + int(operando2)
elif operacion == "resta":
    print ("La operacion es una resta")
    resultado = int(operando1) - int(operando2)
elif operacion == "div":
    print ("La operacion es una division")
    try:
        resultado = int(operando1) / int(operando2)
    except ZeroDivisionError:
        print("No intentes dividir entre cero")
        sys.exit()
elif operacion == "mult":
    print ("La operacion es una multiplicacion")
    resultado = int(operando1) * int(operando2)
else:
    print ("La operacion introducida no es correcta")
    sys.exit()

print(resultado)
sys.exit()
