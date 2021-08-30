def main(peso,estatura):
    #escribe tu código abajo de esta línea
    imc= peso/(estatura**2)
    return imc
if __name__=='__main__':
    peso1=float(input("Ingresa tu peso:"))
    est1=float(input("Ingresa tu estatura:"))
    proceso= main(peso1, est1)
    if proceso <20:
        print("peso bajo")
    elif proceso <=20 and proceso <25:
        print("peso noraml ")
    elif proceso <= 25 and proceso <30:
        print("sobre peso")
    elif proceso <= 30 and proceso <40:
        print("obesisdad")
    elif proceso >= 40:
        print("obesidad morbida")