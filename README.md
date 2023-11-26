# Sistemes de Codificació d'Àudio i Vídeo: SP3

## Exercici 1: Conversió mides i codecs
En aquest primer exercici, he creat una classe anomenada **ConversorVideo** que automatitza la conversió d'un vídeo a diverses resolucions i formats de codec utilitzant FFmpeg.
Aquest és el codi que he implementat:
   ```python
   import subprocess

class ConversorVideo:
    def __init__(self, input_file):
        # Inicialitza la classe amb el fitxer d'entrada i llistes buides per a resolucions, escales i formats.
        self.input_file = input_file
        self.resolucions = []
        self.escalas = {}
        self.formatos = []

    def afegir_resolucio(self, resolucio, escala):
        # Afegeix una resolució i la seva escala corresponent a les llistes.
        self.resolucions.append(resolucio)
        self.escalas[resolucio] = escala

    def afegir_format(self, format):
        # Afegeix un format a la llista de formats.
        self.formatos.append(format)

    def convertir_video(self):
        # Itera a través de les resolucions i formats per convertir el vídeo.
        for resolucio in self.resolucions:
            escala = self.escalas[resolucio]
            for format in self.formatos:
                fitxer_sortida = f"output_{resolucio}_{format}.{self._obtenir_extensio(format)}"
                self._executar_conversio(escala, fitxer_sortida, format)
                print(f"Vídeo convertit a {resolucio} amb format {format} i guardat a {fitxer_sortida}")

    def _executar_conversio(self, escala, fitxer_sortida, format):
        # Executa la conversió del vídeo amb l'eina ffmpeg en funció del format especificat.
        if format == 'vp8':
            command = f"ffmpeg -i {self.input_file} -vf scale={escala} -c:v libvpx -b:v 1M -c:a libvorbis {fitxer_sortida}"
        elif format == 'vp9':
            command = f"ffmpeg -i {self.input_file} -vf scale={escala} -c:v libvpx-vp9 -b:v 1M -c:a libvorbis {fitxer_sortida}"
        elif format == 'libx265':
            command = f"ffmpeg -i {self.input_file} -vf scale={escala} -c:a copy -c:v libx265 {fitxer_sortida}"
        elif format == 'libaom-av1':
            command = f"ffmpeg -i {self.input_file} -vf scale={escala} -c:v libaom-av1 -crf 30 {fitxer_sortida}"
        else:
            print(f"Format no suportat: {format}")
            return

        subprocess.call(command, shell=True)

    def _obtenir_extensio(self, format):
        # Obté l'extensió del fitxer basant-se en el format.
        extensions = {
            'vp8': 'webm',
            'vp9': 'webm',
            'libx265': 'mp4',
            'libaom-av1': 'mkv'
        }
        return extensions.get(format, 'webm')

def main():
    # Funció principal que crea una instància de ConversorVideo i realitza la conversió del vídeo.
    input_file = '/home/ccorbi/BigBuckBunny_SP3.mp4'

    conversor = ConversorVideo(input_file)

    # Demana a l'usuari les resolucions desitjades i les escalas corresponents.
    resolucions_str = input("Introdueix les resolucions desitjades separades per espais (ex. 720p 480p 360x240 160x120): ")
    resolucions = resolucions_str.split()

    for resolucio in resolucions:
        escala = input(f"Introdueix l'escala per a {resolucio} (ex. 1280:720): ")
        conversor.afegir_resolucio(resolucio, escala)

    # Demana a l'usuari els formats desitjats.
    formats_str = input("Introdueix els formats desitjats separats per espais (ex. vp8 vp9 libx265 libaom-av1): ")
    formats = formats_str.split()

    if not formats:
        print("No s'han proporcionat formats.")
        return

    # Afegeix els formats especificats i realitza la conversió del vídeo.
    for format in formats:
        conversor.afegir_format(format)

    conversor.convertir_video()

if __name__ == "__main__":
    main()

   ```
**Resultat de l'exercici 1:**
En aquest exemple, es pot veure com s'obté una resolució de 720p en els formats h265 i vp9. Es creen dos vídeos diferents: **output_720p_libx254.mp4** i **output_720p_vp9.webm**. 

![](https://github.com/caarmeecoorbii/SP3/blob/main/SP3-Resultatex1.png)

```python
# Executa l'exercici 1
python3 ex1.py
```

## Exercici 2: Comparació entre VP8 i VP9

## Exercici 3: Creació GUI

## Exercici 4: Funcionalitats Docker
