import ffmpeg
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TENC

def set_encoding_library(file_path, encoding_lib="LAME"):
    audio = MP3(file_path, ID3=ID3)
    if not audio.tags:
        audio.add_tags()
    audio.tags.add(TENC(encoding=3, text=[encoding_lib]))
    audio.save()
    print(f"Metadatos actualizados para {file_path}")

def convert_to_mp3_and_replace(source_folder):
    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)
        # Verifica si el archivo es de audio evitando convertir archivos que no lo sean.
        if os.path.isfile(filepath) and (filepath.endswith('.mp3') or filepath.endswith('.aac') or filepath.endswith('.m4a') or filepath.endswith('.wav')):
            temp_output_filepath = os.path.join(source_folder, os.path.splitext(filename)[0] + "_temp.mp3")
            try:
                # Realiza la conversión sin verificación de AAC LC
                ffmpeg.input(filepath).output(temp_output_filepath, acodec='libmp3lame').run(overwrite_output=True)
                set_encoding_library(temp_output_filepath, "LAME")  # Actualiza los metadatos del archivo MP3 convertido
                os.remove(filepath)  # Elimina el archivo original
                final_output_filepath = os.path.splitext(filepath)[0] + ".mp3"
                os.rename(temp_output_filepath, final_output_filepath)  # Reemplaza el archivo original
                print(f"Convertido y reemplazado: {filename}")
            except ffmpeg.Error as e:
                print(f"Error al convertir {filename}: {e}")

if __name__ == "__main__":
    source_folder = input("Ingresa el directorio de los archivos de audio: ").strip()
    convert_to_mp3_and_replace(source_folder)
