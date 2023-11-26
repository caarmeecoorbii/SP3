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
En aquest segon exercici, he creat un nou script **ex2.py** que fa servir FFmpeg per comparar dos vídeos, concretament dos codecs: VP8 i VP9. Aquest és el codi que he implementat:

```python
import subprocess

def comparar_videos(video1, video2, output_file):
    # Utilitza la comanda ffmpeg per combinar els dos vídeos en una única pantalla
    command = [
        'ffmpeg',                              # Comença una nova comanda FFmpeg
        '-i', video1,                          # Especifica el primer vídeo d'entrada
        '-i', video2,                          # Especifica el segon vídeo d'entrada
        '-filter_complex',                     # Inicia la secció de filtres complexos de FFmpeg
        '[0:v]setpts=PTS-STARTPTS[video1];'    # Ajusta els timestamps del primer vídeo
        '[1:v]setpts=PTS-STARTPTS[video2];'    # Ajusta els timestamps del segon vídeo
        '[video1][video2]hstack=inputs=2[output]',  # Apila horitzontalment els dos vídeos
        '-map', '[output]',                    # Especifica la sortida dels filtres
        output_file                            # Fitxer de sortida resultant
    ]
    
    subprocess.run(command)                    # Executa la comanda FFmpeg

def main():
    video1 = '/home/ccorbi/output_480p_vp8.webm'   # Ruta del primer vídeo (VP8)
    video2 = '/home/ccorbi/output_480p_vp9.webm'   # Ruta del segon vídeo (VP9)
    output_file = 'comparacio_vp8_vs_vp9.mp4'      # Fitxer de sortida

    comparar_videos(video1, video2, output_file)   # Crida a la funció de comparació de vídeos
    print(f'Comparació dels vídeos {video1} i {video2} creada a {output_file}')  # Imprimeix un missatge informatiu

if __name__ == "__main__":
    main()  # Executa la funció principal quan s'executa el script
```

**Resultat de l'exercici 2:**

El resultat d'aquest exercici és el vídeo **comparacio_vp8_vs_vp9.mp4**, aquí podem veure un frame d'aquest vídeo (part esquerra - VP8 i part dreta- VP9):

![](https://github.com/caarmeecoorbii/SP3/blob/main/SP3-Resultatex2.png)

Podem comparar els dos còdecs en diferents aspectes:

**1. Eficiència de compressió** 
VP9 té una compressió significativament millor que VP8, oferint qualitat semblant amb baixes taxes de bits, especialment útil per a la transmissió de vídeo d'alta resolució a través d'internet. En mitjana, VP9 pot proporcionar entre un 30-50% millor compressió que VP8, depenent del contingut i la configuració.

**2. Mides de bloc**
VP9 té mides de bloc més grans (4x4 fins a 64x64 píxels) que VP8 (fixa en 16x16 píxels), permetent una millor adaptació a continguts variats i millorant la compressió i qualitat visual.

**3. Predicció vector del moviment**
VP9 introdueix tècniques de predicció del vector de moviment més avançades en comparació amb VP8. En VP9, es poden considerar diversos candidats de vectors de moviment per a cada bloc, i se selecciona el millor candidat basant-se en l'error de predicció més baix. Això permet una estimació i compensació de moviment més precisa, la qual cosa contribueix a la millora de l'eficiència de compressió de VP9.


```python
# Executa l'exercici 2
python3 ex2.py
```


## Exercici 3: Creació GUI
En aquest exercici, he creat una GUI amb l'ajuda de la llibreria Tkinter de Python. La finalitat d'aquesta GUI és crear una aplicació que donat una dimensió, redimensiona el vídeo d'entrada que selecciones.

Aquesta és l'estructura que té la GUI:

| Menú principal | Selecció Vídeo Entrada |
|----------|----------|
| ![Descripción 1](https://github.com/caarmeecoorbii/SP3/blob/main/menuprincipalGUI.png) | ![Descripción 2](https://github.com/caarmeecoorbii/SP3/blob/main/selecciofitxerGUI.png) |
| Redimensionar vídeo | Exit |
| ![Descripción 3](https://github.com/caarmeecoorbii/SP3/blob/main/redimensionarGUI.png) | ![Descripción 4](https://github.com/caarmeecoorbii/SP3/blob/main/exitGUI.png) |



```python
# Executa l'exercici 3
python3 ex3.py
```


## Exercici 4: Funcionalitats Docker
