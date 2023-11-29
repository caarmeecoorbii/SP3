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
