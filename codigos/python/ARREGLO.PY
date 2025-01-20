import math

#Imprime las opcines del menú
def opciones():
    print("\nMenú principal")
    print("1. Rectángulo")
    print("2. Triángulo rectángulo")
    print("3. Triángulo isósceles")
    print("4. Círculo")
    print("5. Salir ")

#se encarga de tomar la opción de la figura
def figura():
        figura = int(input("\nSeleccione una opción: "))
        if figura in range(1,6):
            return figura
        else:
            print("Por favor ingrese una opción válida")

#pregunta del tipo de cálculo que se debe hacer 
def tipo_calculo():
    print("\n[1] Calcular área de la figura")
    print("[2] Calcular perímetro de la figura")
    while True:
        calculo = int(input("Ingrese la opción que necesita: "))
        if calculo == 1 or calculo == 2:
            return calculo
        else:
            print("La opción no existe")

#se encarga de tomar los datos, solo cuando la figura usa base y altura
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

def rectangulo(calculo):
    base, altura = datos()
    if calculo == 1:
        print("\n Área del rectángulo \n")
        area = base * altura
        return area
    elif calculo == 2:
        print("\nPerímetro del rectángulo \n")
        perimetro = 2 * (base + altura)
        return perimetro

def triangulo_rectangulo(calculo):
    base, altura = datos()
    if calculo == 1:
        print("\n Área del triángulo rectangulo\n")
        area = (base * altura) / 2
        print(f"El área del triángulo rectángulo es: {area}")
    elif calculo == 2:
        print("\nPerímetro del triángulo rectángulo \n")
        hipotenusa = math.sqrt(base**2 + altura**2)
        perimetro = base + altura + hipotenusa
        print(f"El perímetro del triángulo rectángulo es: {perimetro}")

def triangulo_isoseles(calculo):
    if calculo == 1:
        print("\nárea del triángulo isóseles \n")
        base, altura = datos()
        area = (base * altura) / 2
        print(f"El área del triángulo isósceles es: {area}")
    elif calculo == 2:
        print("\nPerímetro del triángulo isóseles \n")
        lado = float(input("Ingrese el lado igual: "))
        base = float(input("Ingrese la base: "))
        perimetro = 2 * lado + base
        print(f"El perímetro del triángulo isósceles es: {perimetro}")

def circulo(calculo):
    diametro = float(input("Ingrese el diámetro: "))
    if diametro <= 0:   
        print("El diámetro debe ser un valor positivo.")
        return
    if calculo == 1:
        print("\nÁrea del círculo \n")
        radio = diametro / 2
        area = math.pi * (radio**2)
        print(f"El área del círculo es: {area}")
    elif calculo == 2:
        print("\nPerímetro del círculo \n")
        perimetro = math.pi * diametro
        print(f"El perímetro del círculo es: {perimetro}")

def menu():
    while True:
        opciones()
        opcion_figura = figura()
        if opcion_figura == 5:
            print("Saliendo del programa. ¡Gracias!")
            break
        calculo = tipo_calculo()
        if opcion_figura == 1 and calculo == 1:
            area = rectangulo(calculo)
            print("El área del rectángulo es", area)
        elif opcion_figura == 1 and calculo == 2:
            perimetro = rectangulo(calculo)
            print(f"El pe´rimetro del rectángulo es {perimetro}")
        elif opcion_figura == 2:
            triangulo_rectangulo(calculo)
        elif opcion_figura == 3:
            triangulo_isoseles(calculo)
        elif opcion_figura == 4:
            circulo(calculo)

menu()
