import os
from mutagen.mp3 import MP3
from mutagen import File
import shutil  # Importa shutil para mover archivos

def mover_no_mpeg(directorio, directorio_destino):
    archivos_no_mpeg = []

    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        
        try:
            audio = File(ruta_archivo)
            if audio is not None and not isinstance(audio, MP3):
                archivos_no_mpeg.append(ruta_archivo)
        except Exception as e:
            print(f"No se pudo procesar el archivo {archivo}. Error: {e}")
    
    if archivos_no_mpeg:
        print("Se encontraron los siguientes archivos no MPEG que serán movidos:")
        for archivo in archivos_no_mpeg:
            print(archivo)
        
        respuesta = input("¿Deseas continuar y mover estos archivos? (s/n): ")
        if respuesta.lower() == 's':
            for archivo in archivos_no_mpeg:
                destino = os.path.join(directorio_destino, os.path.basename(archivo))
                print(f"Moviendo archivo no MPEG: {archivo} a {directorio_destino}")
                shutil.move(archivo, destino)
            print("Archivos no MPEG movidos.")
        else:
            print("Operación cancelada. No se movieron archivos.")
    else:
        print("No se encontraron archivos no MPEG. No se necesita realizar ninguna acción.")

# Define la ruta del directorio origen y el directorio destino
directorio_origen = r"C:\Users\scri0\Music"
directorio_destino = r"C:\Users\scri0\NonMPEG_Music"  # Asegúrate de que este directorio exista

mover_no_mpeg(directorio_origen, directorio_destino)
