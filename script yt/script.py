import os
import shutil
import yt_dlp

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_ffmpeg_path():
    path = shutil.which('ffmpeg')
    if path:
        return path
    local_path = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'ffmpeg', 'bin', 'ffmpeg.exe'))
    if os.path.isfile(local_path):
        return local_path
    raise FileNotFoundError(
        'ffmpeg no encontrado. Instálalo en el PATH del sistema o coloca ffmpeg.exe en:\n'
        f'  {os.path.normpath(os.path.join(SCRIPT_DIR, "..", "ffmpeg", "bin"))}\n'
        'Descárgalo desde: https://www.gyan.dev/ffmpeg/builds/'
    )

# --- Configuración del Downloader ---
def descargar_audio(urls):
    ydl_opts = {
        'ffmpeg_location': get_ffmpeg_path(),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    # Bucle para descargar cada URL de la lista
    for url in urls:
        try:
            print(f"\n--- Descargando: {url} ---")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("¡Descarga completada!")
        except Exception as e:
            print(f"❌ Error al descargar {url}: {e}")

# --- Código Principal ---
if __name__ == "__main__":
    # Lee las URLs desde el archivo de texto
    archivo_urls = "lista_musica.txt"
    try:
        with open(archivo_urls, 'r') as file:
            lista_urls = [linea.strip() for linea in file if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_urls}'.")
        exit()

    if lista_urls:
        print(f"Se encontraron {len(lista_urls)} enlaces para descargar.")
        descargar_audio(lista_urls)
    else:
        print("El archivo de lista está vacío.")