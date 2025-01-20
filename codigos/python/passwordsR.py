import string
import random 

print("\n||Generador de contraseñas seguras||\n")

longitud = int(input("Ingrese el largo de la contraseña: "))

#Especificaciones
print("\n[1] Números \n[2] Letras \n[3] Símbolos especiales \n[4] Todos\n")
valores = input("\n|| Ingrese las opciones para su contraseña, separadas por comas || \n--> ")

valores = list(map(int, valores.split(',')))

#las letras, caracteres y números de la librería string
# string.ascii_letters  string.digits string.punctuation

#primero concatena de forma aleatoria los caracteres 
# = "".join(random.choice(caracteres) for i in range(longitud))
                                            #el bucle se repite las veces que define el usuario
caracteres = ""
if 4 in valores:  # Se agregan todos los caracteres 
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    if 1 in valores:
        caracteres += string.digits
    if 2 in valores:
        caracteres += string.ascii_letters
    if 3 in valores:
        caracteres += string.punctuation

quitar = int(input("Elija una opcion \n[1]Quitar mayúsculas \n[2]Quitar minusculas \nO presione enter para omitir \n --> "))
if quitar == 1:
    caracteres = caracteres.lower()
elif quitar == 2:
    caracteres = caracteres.upper()

if caracteres:  #Comprueba si hay caracteres en la variable 
    password = "".join(random.choice(caracteres) for i in range(longitud))
    print(f'\nSu contraseña es --> "{password}"')
else:
    print("\nNo seleccionó ninguna opción válida. Por favor, intente de nuevo.")