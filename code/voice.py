#######################################################
#     Class pour vocaliser une chaine de caractères
#######################################################

# pip install gTTS

from gtts import gTTS

class Voice:

    def __init__(self, lang = "fr"):
        # Texte à convertir
        self.lang = lang

    def api_gtts(self, texte):
        # Créer un objet gTTS
        tts = gTTS(text=texte, lang=self.lang, slow=False)
        # Sauvegarder le fichier
        tts.save('Current_payload.mp3')
        print("Le fichier a été généré")




if __name__ == "__main__":

    texte = "Bonjour, je m'appelle Valérie. Enchantée !"

    voice = Voice("fr")
    voice.api_gtts(texte)

    import gtts.lang
    print(gtts.lang.tts_langs())