
def main():
    edad= int(input("cual es tu edad:" ))
    if edad >= 18:
        ident=str(input("¿Tienes identificación oficial? (s/n):"))
        if ident == "s" : 
            print("Tramite de licencia concedido")
    else: 
        print("no cumples los requisitos")

if __name__ == '__main__':
    main()
