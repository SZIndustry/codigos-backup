import os 
 
def rectangulo(calculo, datos):
    base, altura = datos
    if calculo == 1:
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    elif calculo == 2:
        perimetro = 2 * (base + altura)
        print(f"El perímetro del rectángulo es: {perimetro}")
             
def datos():
    while True:
        try:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            if base != altura or altura != base:
                return base, altura
            else:
                print("La base y la altura no pueden ser las mismas")
        except ValueError:
            print("Igrese un numero")

calculo = int(input("Ingrese un numero "))
os.system("cls")
datos = datos()
os.system("cls")
rectangulo(calculo, datos)




