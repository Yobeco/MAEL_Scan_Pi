################################################
#         CallBack du bouton "Scanner"
################################################

from qrscan import QRscan_fake
from crypt import Crypt
from voice import Voice
from player import Player

################################################
#            1- Scanner le code QR
################################################

qr_module = QRscan_fake()
crypted_qr_content = qr_module.scan()


################################################
#      2- Décrypter le contenu du code QR
################################################

# Création d'une instance de la classe Crypt()
cryptor = Crypt()

# Utilisation de la méthode pour décrypter
decrypted_word = cryptor.decrypt(crypted_qr_content)
print(f"La chaine de caractères une fois décryptée est : {decrypted_word}")


################################################
#          3- Générer le fichier MP3
################################################

# Création d'une instance de la classe Voice()
texte_a_dire = Voice("fr")
# Envoi de la chaine de caratères au module de création du fichier mp3
texte_a_dire.api_gtts(decrypted_word)


################################################
#          2- Générer le fichier MP3
################################################

# Création d'une instance de la classe Player()
lire_mp3 = Player("Current_payload.mp3")
lire_mp3.play()


