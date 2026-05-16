##############################################################
#     Classe pour interpréter le contenu des codes QR
##############################################################

import re

def tri_regex(texte):
    match texte:
        case str(s) if re.match(r"^<fr>", s):
            return "Français détecté"
        case str(s) if re.match(r"^<es>", s):
            return "Espagnol détecté"
        case str(s) if re.match(r"^<en>", s):
            return "Espagnol détecté"

print(tri_regex("<fr>Tout va bien"))

print("-" * 50)

def extraire_et_afficher(texte):
    match texte:
        # On cherche un motif <...> au début, et on capture l'intérieur (...)
        case str(s) if (m := re.match(r"^<([a-z]{2})>(.*)", s)):
            langue = m.group(1)  # Contient 'fr', 'es' ou 'en'
            contenu = m.group(2)  # Contient le reste du texte
            print(f"Code langue détecté : {langue}")
            print(f"Message à traiter : {contenu}")

        case _:
            print("Format non reconnu.")


extraire_et_afficher("<fr>Bonjour !")

print("-" * 50)

import re


def extraire_tout(texte):
    match texte:
        # Groupe 1 : langue (optionnel)
        # Groupe 2 : contenu (obligatoire, mais peut être vide)
        # Groupe 3 : suffixe après l'étoile (optionnel)
        case str(s) if (m := re.match(r"^(?:<([a-z]{2})>)?(.*?)(?:\*([a-z]))?$", s)):
            langue = m.group(1) or "Inconnue"
            contenu = m.group(2).strip()
            suffixe = m.group(3) or "Aucun"

            print(f"--- Analyse de : '{s}' ---")
            print(f"Langue  : {langue}")
            print(f"Message : {contenu}")
            print(f"Suffixe : {suffixe}\n")

        case _:
            print(f"Format non reconnu pour : {texte}")


# Tests avec tes exemples
extraire_tout("<fr>Bonjour*e")
extraire_tout("<es>Hola !*d")
extraire_tout("<en>Hi!")
extraire_tout("Coucou*e")
extraire_tout("Ça va ?*d")

print("#" * 50)

def parser(texte):
    match texte:
        # On cherche un motif <gd> au début, et on capture l'ID du fichier
        # Pour les drives
        case str(s) if (m := re.match(r"^<(gd)>(.*)", s)):
            drive_type = m.group(1)     # Contient 'gd', 'md' ou '??' (Selon le type de Cloud)
            file_id = m.group(2)        # Contient le reste du texte

            return [drive_type, file_id]   # Pas besoin de renvoyer la valeur
            # --> Lancer la méthode directement avec ces paramètres


        # Pour parser les
        # Groupe 1 : langue (optionnel)
        # Groupe 2 : contenu (obligatoire, mais peut être vide)
        # Groupe 3 : suffixe après l'étoile (optionnel)
        case str(s) if (m := re.match(r"^(?:<([a-z]{2})>)?(.*?)(?:\*([a-z]))?$", s)):
            langue = m.group(1) or "fr"
            contenu = m.group(2).strip()
            suffixe = m.group(3) or ""

            return [langue, contenu, suffixe]

        case _:
            print(f"Format non reconnu pour : {texte}")
            return None



def parser_wifi(qr_data):

    def parse_wifi_qr(qr_data):
        params = {k.lower(): v for k, v in (p.split(":", 1) for p in qr_data.split(";") if ":" in p)}
        return {
            "security": params.get("t", "").upper(),  # Normaliser en majuscules
            "ssid": params.get("s", ""),
            "password": params.get("p", None),
            "hidden": params.get("h", "false").lower() == "true"
        }

    # Exemple d'utilisation
    qr_data = "WIFI:S:MonReseau;H:false;T:WPA;P:monmotdepasse;;"
    print(parse_wifi_qr(qr_data))


# Tests avec tes exemples
print(parser("<gd>5sq564fze546cx8er8q"))
print(parser("<fr>Bonjour*e"))
print(parser("<es>Hola !*d"))
print(parser("<en>Hi!"))
print(parser("Coucou*e"))
print(parser("Ça va ?*d"))
print(parser("Ça fonctionne bien"))

print("-" * 50)