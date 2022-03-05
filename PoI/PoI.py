import sys

repetir = "Y"

while repetir == "Y" :
    numero = float(input("¿En que número estas pensando? "))

    par = True if (numero % 2) == 0 else False

    if par:
        print("¡Es un numero Par!")
    else:
        print("¡Es un numero Impar!")

    repetir = input("¿Quieres añadir otro [Y/N]? ")

sys.exit("Hasta pronto")
