import os
import time 

print('''
__        __   _                            _    
\\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___ 
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\
  \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/ 

                 _           _                       _   
 _ __  _ __ ___ (_) ___  ___| |_    __ _ _ __   __ _| |_   _ _______ _ __ 
| '_ \\| '__/ _ \\| |/ _ \\/ __| __|  / _` | '_ \\ / _` | | | | |_  / _ \\ '__|
| |_) | | | (_) | |  __/ (__| |_  | (_| | | | | (_| | | |_| |/ /  __/ |   
| .__/|_|  \\___// |\\___|\\___|\\__|  \\__,_|_| |_|\\__,_|_|\\__, /___\\___|_|   
|_|           |__/                                     |___/             
''')


print("\033  By sDuckerS \n")

list_users = []

def analisis_de_ruta(ruta, limite=10):

    archivos = []

    for raiz, directorios, archivos_en_dir in os.walk(ruta):
        for nombre_archivo in archivos_en_dir:
            ruta_completa = os.path.join(raiz, nombre_archivo)
            try:
                tamaño = os.path.getsize(ruta_completa)
                archivos.append((tamaño, ruta_completa))
            except OSError as e:
                print(f"Error: {e} al intentar leer el archivo {ruta_completa}")
                continue

    archivos.sort(reverse=True)

    return archivos

def primera_pantalla():
    global users
    while True:    
        users = input("Ingrese el Nombre del dispositivo -> ")

        if users in list_users:
            print(f"Usuario {users} ya registrado")

        else:
            list_users.append(users)
            print("Registro completo")
            segunda_pantalla(users)  
            break
            #if not segunda_pantalla():
                #list_users.remove(users)

def segunda_pantalla(users):

    print(f"Elija la opcion que desea a continuacion para el ussuario {users}")

    while True:
        ans = input("\n[1] Analisis completo\n[2] Analizar ruta especifica\n[3] Regresar\n[4] Salir\n --> ")
        if ans == "1":
            ruta = "C:\\"
            print("Empezando análisis...")
            time.sleep(1)
            print("Esto puede tardar un poco")

            archivos_grandes = analisis_de_ruta(ruta)

            print(f"\nA continuacion se muestran los 3 archivos mas pesados:\n")

            if archivos_grandes:
                for tamaño, archivo in archivos_grandes[:3]:
                    nombre_del_archivo = os.path.basename(archivo)      
                    print(f"{nombre_del_archivo}: {tamaño / (1024 * 1024):.2f} MB\n")

            result = input("\n[1] Mostrar ubicacion de archivos\n[2] Contibuar\n--> ")

            if result == "1":
                for tamaño, archivo in archivos_grandes[:3]:
                    print(f"{archivo}: {tamaño / (1024 * 1024):.2f} MB\n")
            else:
                continue

        elif ans == "2":
            while True:
                try:
                    cantidad_dearchivos = int(input("Ingrese cuantos archivos grandes desea mostrar\n --> "))
                    break
                except ValueError:
                    print("Ingrese un número válido")
                    
            ruta = input("Ingrese la ruta a escanear\n --> ")
            print(f"Iniciando análisis de la siguiente ruta: {ruta} en el equipo {users}")
            
            archivos_grandes = analisis_de_ruta(ruta, cantidad_dearchivos)

            time.sleep(2)

            print(f"\nA continuación se muestran los {cantidad_dearchivos} archivos más pesados:\n")

            if archivos_grandes:
                for tamaño, archivo in archivos_grandes[:cantidad_dearchivos]:
                    nombre_del_archivo = os.path.basename(archivo)      
                    print(f"{nombre_del_archivo}: {tamaño / (1024 * 1024):.2f} MB\n") 
            else:
                print("No se encontraron archivos o no se pudo acceder a ellos.")

            result = input("\n[1] Mostrar ubicacion de archivos\n[2] Continuar\n--> ")

            if result == "1":
                for tamaño, archivo in archivos_grandes[:3]:
                    print(f"\n{archivo}: {tamaño / (1024 * 1024):.2f} MB\n")
            else:
                continue

        elif ans == "3":
            list_users.remove(users)
            return primera_pantalla() 

        elif ans == "4":
            print("Saliendo...")
            exit() 



#Inicio del programa
primera_pantalla()