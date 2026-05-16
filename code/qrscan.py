###########################################################################
#     Classe pour activer le capteur de code QR et recevoir le contenu
###########################################################################

import random
from crypt import Crypt    # Pour simuler que le code QR a été crypté par MAEL Gen

# --- Simulation d'un scan de code QR encrypté lu ---

class QRscan_fake:

    def __init__(self):
        pass

    def scan(self):
        liste_mots = ["Le chat mange le gâteau.",
                       "Les garçons sont de bons élèves.",
                       "Trois chameaux sont sur l'île.",
                       "Que pensez-vous de tout cela ?",
                       "C'est Noël ! Voyez-vous ?",
                       "Ça ce sont des œufs. Œufs frais là ?",
                       "Aïe, ce sont est trop aigü !",
                       "& ça coûte combien d'€ ?",
                       "J'eppelle un mot : a, m, o, u, r."
                       ]

        x = random.randint(0,len(liste_mots)-1)

        # Création d'une instance de la classe Crypt()
        cryptor = Crypt()

        content_qr_crypted = cryptor.encrypt(liste_mots[x])
        print(f"Contenu crypté du code QR : {content_qr_crypted}")

        return content_qr_crypted



# --- Classe de contrôle du module de lecture de QR : GM861S-LED ---

class QRScan_GM861SLED:         # Seulement sur le RPi Zéro 2W
    pass




if __name__ == "__main__":

    qr_module = QRscan_fake()
    qr_module.scan()