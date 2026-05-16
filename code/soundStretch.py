##########################################################
#    Classe pour étirer un son sans changer sa hauteur
##########################################################

# sudo apt install ffmpeg -y
# sudo apt install soundstretch
# https://www.surina.net/soundtouch/soundstretch.html

import subprocess
from importlib.util import source_hash


class SoundStretch:

    '''
    Convertit d'abord le fichier en .wav (car soundstretch ne supporte pas le mp3)
    soundstrech est de meilleure qualité que ffmpeg pour la fonction "tempo"
    '''

    def __init__(self, filename : str = "Current_payload.mp3", slowing_factor: int = -20):
        self.filename = filename
        self.slowing_factor = slowing_factor        # Ralentissement -20% par défaut

    def convert2wav(self):

        # Chemins des fichiers
        input_mp3 = self.filename
        output_wav = "input.wav"   # Ma sortie est identique à l'entrée mais au format WAV

        # Commande FFmpeg (+ arguments pour éviter les problèmes de shell)
        # ffmpeg -i input.mp3 -acodec pcm_s16le -ar 44100 -ac 2 input.wav
        command = [
            "ffmpeg",
            "-i", input_mp3,            # Fichier d'entrée
            "-acodec", "pcm_s16le",     # Codec WAV 16-bit
            "-ar", "44100",             # Fréquence d'échantillonnage
            "-ac", "2",                 # Canaux stéréo
            "-y",                       # Écraser le fichier de sortie si existe
            output_wav                  # Fichier de sortie
        ]

        # Exécution de la commande
        try:
            subprocess.run(
                command,
                check=True,                 # Lève une erreur si FFmpeg échoue
                stdout=subprocess.PIPE,     # Capture la sortie standard (optionnel)
                stderr=subprocess.PIPE,     # Capture les erreurs (optionnel)
                text=True                   # Retourne les sorties en texte (Python 3.7+)
            )
            print(f"Conversion réussie : {output_wav}")
        except subprocess.CalledProcessError as e:
            print(f"Erreur FFmpeg : {e.stderr}")  # Affiche l'erreur de FFmpeg


    def timeStretch(self, filename: str = "input.wav"):

        # Création de la commande "-tempo=xx"
        tempoCmd = f"-tempo={self.slowing_factor}"     # Argument de instance

        # Chemins des fichiers
        input_wav = filename
        output_wav = "Current_payload_slow.wav"

        # Commande soundstretch (+ arguments pour éviter les problèmes de shell)
        # soundstretch input.wav output.wav -tempo=-20
        command = [
            "soundstretch",
            input_wav,
            output_wav,
            tempoCmd                   # Tempo de sortie
        ]

        print(command)

        # Exécution de la commande
        try:
            subprocess.run(
                command,
                check=True,  # Lève une erreur si FFmpeg échoue
                stdout=subprocess.PIPE,  # Capture la sortie standard (optionnel)
                stderr=subprocess.PIPE,  # Capture les erreurs (optionnel)
                text=True  # Retourne les sorties en texte (Python 3.7+)
            )
            # print(f"Conversion réussie : {output_wav}")
        except subprocess.CalledProcessError as e:
            print(f"Erreur FFmpeg : {e.stderr}")  # Affiche l'erreur de FFmpeg

    def slowDownSound(self):
        self.convert2wav()
        self.timeStretch()

if __name__ == "__main__":

    son_lent = SoundStretch()
    son_lent.slowDownSound()





