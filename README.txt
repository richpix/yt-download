📘 README - Español
Descargador de música por lotes de YouTube
Script en Python para descargar listas de reproducción o videos individuales de YouTube y convertirlos automáticamente a MP3 de alta calidad (192 kbps).

📋 Requisitos previos
Python 3.8 o superior instalado en tu sistema.

yt-dlp – instalar con el comando:
pip install yt-dlp

ffmpeg – necesario para convertir el audio a MP3.

Instalación de ffmpeg en Windows

Opción A - ffmpeg ya instalado en el sistema (recomendado):
Si ya tienes ffmpeg en el PATH de Windows, el script lo detectará automáticamente.
No necesitas hacer nada más.

Opción B - ffmpeg local en el proyecto:
1. Descarga ffmpeg desde: https://www.gyan.dev/ffmpeg/builds/
2. Elige la versión ffmpeg-release-essentials.zip (es la más ligera).
3. Descomprime el ZIP en la raíz del proyecto y renombra la carpeta resultante a ffmpeg.

Estructura esperada:
  tu-proyecto/
  ├── script yt/
  │   ├── script.py
  │   ├── README.txt
  │   └── lista_musica.txt
  └── ffmpeg/
      └── bin/
          ├── ffmpeg.exe
          ├── ffplay.exe
          └── ffprobe.exe

El script buscará ffmpeg automáticamente: primero en el PATH del sistema y,
si no lo encuentra, en la ruta relativa ../ffmpeg/bin/ffmpeg.exe.

⚙️ Configuración del script
No es necesario editar ninguna ruta. El script detecta ffmpeg automáticamente.
📄 Preparar el archivo de URLs
Crea un archivo llamado lista_musica.txt en la misma carpeta que el script. En él, escribe una URL de YouTube por línea. No uses el carácter # porque el script no lo ignora (cada línea se toma como URL).

Ejemplo de lista_musica.txt:

text
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=9bZkp7q19f0
https://www.youtube.com/playlist?list=PLplXQ2cg9B_qrCVd1J_iId5SvP8Kf_BfS
🚀 Uso paso a paso
1. Obtener las URLs de una lista de reproducción
Abre una terminal en la carpeta del proyecto y ejecuta:

bash
yt-dlp --get-url --flat-playlist <URL_DE_LA_LISTA>
Esto te mostrará todas las URLs de los videos. Cópialas y pégalas en lista_musica.txt.

Ejemplo:

bash
yt-dlp --get-url --flat-playlist https://www.youtube.com/playlist?list=PLplXQ2cg9B_qrCVd1J_iId5SvP8Kf_BfS
2. Ejecutar el script
Una vez que tengas las URLs en lista_musica.txt, corre:

bash
python descargador.py
Los videos se descargarán como archivos .webm y luego se convertirán a MP3. Los MP3 se guardarán en la misma carpeta.

🛠 Personalización
Dentro del script puedes modificar:

Calidad del MP3: cambia 'preferredquality': '192' a 320 (máxima calidad) o 128 (menor tamaño).

Carpeta de salida: edita 'outtmpl': '%(title)s.%(ext)s'. Por ejemplo, 'Musica/%(title)s.%(ext)s' guardará los archivos en una subcarpeta llamada Musica.

⚠️ Nota legal
Este script es solo para uso personal y educativo. Respeta los derechos de autor y los términos de servicio de YouTube.

📘 README - English
YouTube Batch Music Downloader
Python script to download YouTube playlists or individual videos and automatically convert them to high-quality MP3 (192 kbps).

📋 Prerequisites
Python 3.8+ installed on your system.

yt-dlp – install with:
pip install yt-dlp

ffmpeg – required for audio conversion to MP3.

Installing ffmpeg on Windows

Option A - ffmpeg already installed on your system (recommended):
If ffmpeg is already in your Windows PATH, the script will detect it automatically.
No further action needed.

Option B - local ffmpeg in the project:
1. Download ffmpeg from: https://www.gyan.dev/ffmpeg/builds/
2. Choose the ffmpeg-release-essentials.zip version.
3. Extract the ZIP to the project root and rename the resulting folder to ffmpeg.

Expected structure:
  your-project/
  ├── script yt/
  │   ├── script.py
  │   ├── README.txt
  │   └── lista_musica.txt
  └── ffmpeg/
      └── bin/
          ├── ffmpeg.exe
          ├── ffplay.exe
          └── ffprobe.exe

The script will find ffmpeg automatically: first in the system PATH and,
if not found, in the relative path ../ffmpeg/bin/ffmpeg.exe.

⚙️ Script Configuration
No manual path editing required. The script detects ffmpeg automatically.
📄 Preparing the URLs file
Create a file named lista_musica.txt in the same folder as the script. Write one YouTube URL per line. Do not use the # character because the script will treat it as part of the URL.

Example lista_musica.txt:

text
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=9bZkp7q19f0
https://www.youtube.com/playlist?list=PLplXQ2cg9B_qrCVd1J_iId5SvP8Kf_BfS
🚀 How to use
1. Get URLs from a YouTube playlist
Open a terminal in the project folder and run:

bash
yt-dlp --get-url --flat-playlist <PLAYLIST_URL>
This will output all video URLs. Copy and paste them into lista_musica.txt.

Example:

bash
yt-dlp --get-url --flat-playlist https://www.youtube.com/playlist?list=PLplXQ2cg9B_qrCVd1J_iId5SvP8Kf_BfS
2. Run the script
Once the URLs are in lista_musica.txt, execute:

bash
python downloader.py
Videos will be downloaded as .webm then converted to MP3. The MP3 files will be saved in the same folder.

🛠 Customization
Inside the script you can modify:

MP3 quality: change 'preferredquality': '192' to 320 (highest) or 128 (smaller file size).

Output folder: edit 'outtmpl': '%(title)s.%(ext)s'. For example, 'Music/%(title)s.%(ext)s' will save files into a Music subfolder.

⚠️ Legal notice
This script is for personal and educational use only. Respect copyright and YouTube's Terms of Service.

