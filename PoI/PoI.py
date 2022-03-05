import sys
import Fun_PoI as PoI

repetir = "Y"

while repetir == "Y":
    numero = input("¿En que número estas pensando? ")

    PoI.is_par(numero)

    while True:
        repetir = input("¿Quieres añadir otro [Y/N]? ")
        if repetir == "Y" or repetir == "N":
            break

sys.exit("Hasta pronto")
