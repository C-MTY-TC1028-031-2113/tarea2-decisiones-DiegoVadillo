def main():
    # Escribe tu código abajo de esta línea
    numero= int(input("dame un numero"))
    if numero == 360 or 270 or 180 or 90 or 0:
        print ("eje")
    elif numero > 0 and < 90:
        print ("cuandrante 1")
    elif numero > 90 and < 180:
        print("cuadrante 2")
    elif numero > 180 and < 270:
        print("cuadrante 3")
    elif numero > 270 and < 360:
        print("cuadrante 4")
    elif numero >360: 
        print("excede")

if __name__ == '__main__':
    main()
