##############################################################
#     Classe pour interpréter le contenu des codes QR
##############################################################

import re

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


## Pour parser les QR de connexion wifi : à améliorer (avec des regex ?)
# def parse_wifi_qr(qr_data):
#     # Supprimer le préfixe "WIFI:" (insensible à la casse)
#     if not qr_data.upper().startswith("WIFI:"):
#         raise ValueError("Format de code QR Wi-Fi invalide : doit commencer par 'WIFI:'.")
#
#     qr_data = qr_data[5:]  # Enlever "WIFI:"
#
#     # Initialiser les paramètres
#     params = {}
#     for param in qr_data.split(";"):
#         if ":" in param:
#             key, value = param.split(":", 1)
#             params[key.upper()] = value  # Normaliser les clés en majuscules
#
#     # Vérifier les champs obligatoires
#     if "S" not in params or "T" not in params:
#         raise ValueError("Format de code QR Wi-Fi invalide : champs S: ou T: manquants.")
#
#     return {
#         "security": params["T"].upper(),  # Normaliser le type de sécurité
#         "ssid": params["S"],              # Casse originale préservée
#         "password": params.get("P"),      # Casse originale préservée (optionnel)
#         "hidden": params.get("H", "false").lower() == "true"  # Booléen
#     }


import re
from dataclasses import dataclass


@dataclass
class WifiConfig:
    ssid: str
    security: str = "nopass"
    password: str | None = None
    hidden: bool = False


def ultra_robust_wifi_parser(raw_str: str) -> WifiConfig:
    # 1. Validation et nettoyage du préfixe
    if not re.match(r"^WIFI:", raw_str, re.IGNORECASE):
        raise ValueError("Format WIFI: manquant")

    # On isole le corps après 'WIFI:'
    content = re.sub(r"^WIFI:", "", raw_str, flags=re.IGNORECASE)

    # 2. La Regex Magique :
    # ([TSPH])  : Capture la clé
    # :         : Séparateur
    # (         : Début du groupe de capture de la valeur
    #   (?:     : Groupe non-capturant pour l'alternative
    #     \\.   : Soit un backslash suivi de N'IMPORTE QUEL caractère (\; \: \\ etc.)
    #     |     : OU
    #     [^;]  : N'importe quel caractère qui n'est PAS un point-virgule
    #   )* : Le tout, zéro ou plusieurs fois
    # )         : Fin de la capture de la valeur
    pattern = re.compile(r"([TSPH]):((?:\\.|[^;])*)", re.IGNORECASE)

    matches = pattern.findall(content)

    # 3. Stockage et Dé-échappement (Unescaping)
    data = {}
    for key, value in matches:
        # On remplace les séquences échappées par le caractère seul
        # \: devient : | \; devient ; | \\ devient \
        clean_value = re.sub(r"\\(.)", r"\1", value)
        data[key.upper()] = clean_value

    return WifiConfig(
        ssid=data.get("S", ""),
        security=data.get("T", "nopass"),
        password=data.get("P"),
        hidden=data.get("H", "").lower() == "true"
    )


# --- Tests de l'impossible ---
tests = [
    r"WIFI:S:Mon\;Reseau:Cool;P:P\@ss\:w\;rd;T:WPA;;",  # Contient \; et \:
    r"WIFI:S:L'aventure \\ C'est l'aventure;P:12345;",  # Contient \\ (un vrai backslash)
    r"WIFI:T:<type_de_sécurité>;S:<SSID>;P:<mot_de_passe>;H:<caché_ou_non>;",
    r"WIFI:T:WEP;S:CLARO_5697Rg;P:Ne1ed1TaPers0nne;H:true;",
]

for t in tests:
    config = ultra_robust_wifi_parser(t)
    print(f"Content   : {t}")
    print(f"SSID      : {config.ssid}")
    print(f"PWD       : {config.password}")
    print(f"Secu type : {config.security}")
    print(f"Hidden    : {config.hidden}")
    print("=" * 50)


# # Tests avec tes exemples
# print(parser("<gd>5sq564fze546cx8er8q"))
# print(parser("<fr>Bonjour*e"))
# print(parser("<es>Hola !*d"))
# print(parser("<en>Hi!"))
# print(parser("Coucou*e"))
# print(parser("Ça va ?*d"))
# print(parser("Ça fonctionne bien"))
