#########################################################
#    Classe qui permet les opérations de lecture audio
#########################################################

# sudo apt install moc

import subprocess
import time

class Player:

    # Dire "Bonjour" et +-5s pour le foward par défaut
    def __init__(self, file_mp3: str = "Bonjour.mp3", move: int=5):
        self.file_mp3 = file_mp3
        self.foward_s = str(move)
        self.backward_s = f"-{str(move)}"

        # Vérifier si le processus MOC est déjà lancé avec la commande "pgrep -x mocp"
        # Exécuter la commande et récupérer la sortie
        moc_on = subprocess.run(["pgrep", "-x", "mocp"], capture_output=True)
        # print(moc_on)
        # Lancer le processus MOC au démarrage
        # print(f"MOC est-il déjà en cours ? --> {not moc_on.returncode}")
        if not moc_on.returncode:
            print("Processus déjà actif.")
        else:
            subprocess.Popen(["mocp", "-S"])
            print("Le serveur MOC a été lancé.")
            time.sleep(0.2)


    def play(self):
        # Vider la playlist, ajouter le fichier et lire sans interface.
        subprocess.Popen(["mocp", "-l", self.file_mp3])
        print("le fichier est en cours de lecture.")

    def toggle(self):
        # Bascule Pause / Play
        subprocess.Popen(["mocp", "-G", self.file_mp3])

    def foward(self):
        # Avancer de xs
        subprocess.Popen(["mocp", "-k" ,self.foward_s, self.file_mp3])

    def backward(self):
        # reculer de xs
        subprocess.Popen(["mocp", "-k" ,self.backward_s, self.file_mp3])

    def volume(self, volume: int):          # +10 = augm. de 10 | -20 = bais. de 20 | 50 = mettre à 50
        subprocess.Popen(["mocp", "-v", str(volume)])


if __name__ == "__main__":
    player = Player("Current_payload.mp3")
    player.play()
    # time.sleep(3)
    # player.foward()