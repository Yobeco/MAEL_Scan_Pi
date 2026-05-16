########################################################################
#      Version fonctionnelle d'une classe permettant d' "encrypter"
#              et de décrypter des chaînes de caractères.
########################################################################

class Crypt:

    # Clés : liste des caractères qui déplacés +1 ne sont plus compatibles avec les QRcode
    # Valeurs : Valeur à assigner à la place de chr +1
    # --> À compléter en cas de bug
    # Pas besoin de l'accéder, donc un attribut de classe est suffisant
    encrypt_excl_dict = {"0x7e": "0xa0"}  # '~' Tilde +1 = 0x7f <control> --> U+00A1	'¡' 	0xc2 0xa1	INVERTED EXCLAMATION MARK

    # Contructeur de classe
    # Auncun attribut d'instance : aucun paramettre lors de l'instanciation.
    def __init__(self):
        pass

    # Fonctions nécessaires pour encrypter / décrypter

    # # # # # # # # # # # # # # # # # # # # #
    #     Décalage UTF-8 des caractères     #
    # # # # # # # # # # # # # # # # # # # # #

    # Fonction pour décaler les lettres du mot d'un octet
    def utf8_shifter(self, word, shift_value):  # "shift_value" = 1 ou -1 point UTF-8

        shifted_word = ""

        # Création d'un nouveau string en décalant chaque lettre de "decal"
        for letter in word:

            # Trouver l'héxadécimal du caractère
            hex_letter = hex(ord(letter))

            if hex_letter in self.encrypt_excl_dict:  # Si "hex_letter" est dans excl_dict

                print("!!! Caractère non-décalable détecté !!!")

                # Aller chercher la valeur de remplacement prévue dans le dictionnaire
                # excl_dict["0x7e"] --> retourne la valeur de la clé "0x7e" dans excl_dict
                # int(excl_dict["0x7e"], 16) --> convertir en int l'héxadécimal "0x7e" (sous forme de string)
                # chr() --> renvoie le caractère correspondant à l'int
                replace_a = chr(int(self.encrypt_excl_dict[hex_letter], 16))

                a = replace_a  # Donner la valeur de remplacement
            else:
                a = chr(ord(letter) + shift_value)  # Sinon, l'incrémenter

            shifted_word = shifted_word + a  # Ajouter la lettre au mot

        return shifted_word


    # # # # # # # # # # # # # # # # # # # # #
    #           Mélange des lettres         #
    # # # # # # # # # # # # # # # # # # # # #

    def shuffler(self, mot_a_encrypt):
        # Liste recevant les lettres mélangées du mot entré
        local_mixed_word = []

        # Créer une liste des éléments impaires
        i = 1

        # Mettre dans local_mixed_word les éléments impaires
        while i < len(mot_a_encrypt):
            local_mixed_word.append(mot_a_encrypt[i])
            i = i + 2

        # Ajouter à la suite dans local_mixed_word les éléments paires
        i = 0
        while i < len(mot_a_encrypt):
            local_mixed_word.append(mot_a_encrypt[i])
            i = i + 2

        # Inverser le sens des éléments de la liste obtenue
        local_mixed_word.reverse()

        # Convertir la liste en chaîne de caractères
        local_mixed_word_str = "".join(local_mixed_word)

        # Renvoyer cette liste (de lettres mélangées) pour être envoyée dans le code QR
        return local_mixed_word_str



    # # # # # # # # # # # # # # # # # # # # #
    #         Dé-mélange des lettres        #
    # # # # # # # # # # # # # # # # # # # # #


    def unshuffler(self, mot_a_decrypt):

        unmixed_word_list = []

        # // --> Partie entière de la division - Nécessaire pour rétablir l'ordre
        half_len = len(mot_a_decrypt) // 2

        # Si le nombre de lettres et paire (reste = 0)
        if not len(mot_a_decrypt) % 2:
            # print("Nombre de lettres PAIR.")
            i = half_len - 1
            while i >= 0:
                unmixed_word_list.append(mot_a_decrypt[i])
                unmixed_word_list.append(mot_a_decrypt[i + half_len])
                i -= 1

        else:
            # print("Nombre de lettres IMPAIR.")
            i = half_len
            while i >= 0:
                unmixed_word_list.append(mot_a_decrypt[i])
                unmixed_word_list.append(mot_a_decrypt[i + half_len])
                i -= 1
            del unmixed_word_list[-1]  # Enlever le dernier caractère : caractère A0 surnuméraire

        # Convertir la liste en chaîne de caractères
        unmixed_word_str = "".join(unmixed_word_list)

        # Renvoyer la chaine de caractères
        return unmixed_word_str


    # Méthode de cryptage d'une chaine de caractères
    def encrypt(self, word):
        shifted_word = self.utf8_shifter(word, 1)
        encrypted_word = self.shuffler(shifted_word)
        return encrypted_word

    # Méthode de décryptage d'une chaine de caractères
    def decrypt(self, word):
        unshifted_word = self.utf8_shifter(word, -1)
        decrypted_word = self.unshuffler(unshifted_word)
        return decrypted_word



if __name__ == "__main__":

    # Création d'une instance de la classe Crypt()
    cryptor = Crypt()

    string_to_crypt = "Bonjour tout le monde"
    print(f"La chaine de caractères à encrypter : {string_to_crypt}")

    # Utilisation de la méthode pour encrypter
    crypted_word = cryptor.encrypt(string_to_crypt)
    print(f"La chaine de caractères une fois encryptée est : {crypted_word}")

    # Utilisation de la méthode pour décrypter
    decrypted_word = cryptor.decrypt(crypted_word)
    print(f"La chaine de caractères une fois décryptée est : {decrypted_word}")
