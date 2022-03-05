def is_float(numero):
    try:
        return True, float(numero)
    except:
        return False, float("NaN")

def is_par(numero):
    is_numero, numero = is_float(numero)

    if is_numero:
        par = True if (numero % 2) == 0 else False

        if par:
            print("¡Es un numero Par!")
        else:
            print("¡Es un numero Impar!")
    else:
        print("No es un numero")
