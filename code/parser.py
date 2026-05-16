##############################################################
#     Classe pour interpréter le contenu des codes QR
##############################################################

import re

# --- Fonction pour récupérer le contenu d'un code QR Wifi ---
def wifi_parser(raw_str: str):
    # 1. Valider et nettoyer le préfixe (redondant)
    if not re.match(r"^WIFI:", raw_str, re.IGNORECASE):
        raise ValueError("Format WIFI: manquant")

    # Isoler le corps après 'WIFI:' --->  ⚠️ Et le ; de la fin ?
    content = re.sub(r"^WIFI:", "", raw_str, flags=re.IGNORECASE)

    # 2. La Regex pour créer des groupes derrière les lettres TSPH:
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

    # Récupérer les groupes dans une liste de tuples
    matches = pattern.findall(content)
    # print(matches)

    # 3. Stockage et Dé-échappement (Unescaping)
    # Dictionnaire recevant les données
    data = {}
    for key, value in matches:
        # On remplace les séquences échappées par le caractère seul
        # \: devient : | \; devient ; | \\ devient \
        clean_value = re.sub(r"\\(.)", r"\1", value)
        # Mettre toutes les clés en majuscule
        data[key.upper()] = clean_value     # Pour correspondre à return

    # Conversion en liste qui est le format attendu
    return [data.get("T", "nopass"),
            data.get("S", ""),
            data.get("P"),
            data.get("H", "").lower() == "true"
            ]

# --- Méthode pour analyser tous les contenus de QR possibles
def qr_parser(texte):
    match texte:

        # 1. --> Cas des QR Wifi (Script encore mal compris)
        case str(s) if s.upper().startswith("WIFI:"):
            # print("C'est un Wifi")
            # print(wifi_parser(str(s)))
            return wifi_parser(str(s))

        # 2. --> Cas des Liens vers Google Drive (Implémenter Drive "La suite")
        # On cherche un motif <gd> au début, et on capture l'ID du fichier
        case str(s) if (m := re.match(r"^/(gd)/(.*)", s)):
            drive_name = m.group(1)     # Contient 'gd', 'md' ou '??' (Selon le type de Cloud)
            file_id = m.group(2)        # Contient le reste du texte

            return [drive_name, file_id]   # Pas besoin de renvoyer la valeur
            # --> Lancer la méthode directement avec ces paramètres

        # 3. Cas des fichiers .mp3 locaux
        case str(s) if (m := re.match(r"^_([a-z]{2})_(.*)", s)):
            folder_url = m.group(1)  #
            file_name = m.group(2)  #

            return [f"assets/{folder_url}", f"_{folder_url}_{file_name}.mp3"]



        # 4. --> Cas des QR avec contenu à vocaliser
        # Groupe 1 : langue (optionnel) --> 2 ou 3 lettres min / maj
        # Groupe 2 : contenu (obligatoire, mais peut être vide)
        # Groupe 3 : suffixe après l'étoile (optionnel)
        case str(s) if (m := re.match(r"^(?:<([A-Za-z]{2,3})>)?(.*?)(?:\#([a-z]))?$", s)):
            langue = m.group(1) or "fr"     # Mettre "fr" si champ vide
            contenu = m.group(2).strip()
            suffixe = m.group(3) or "l"     # Mettre un "l" de lecture si champ vide
                                            # (Plus explicite qu'un strig vide)

            return [langue, contenu, suffixe]

        case _:
            print(f"Format non reconnu pour : {texte}")
            return None



# --- Tests ---
tests = [
    r"WIFI:S:Mon\;Reseau:Cool;P:P\@ss\:w\;rd;T:WPA;;",  # Contient \; et \:
    r"WIFI:S:L'aventure \\ C'est l'aventure;P:12345;",  # Contient \\ (un vrai backslash) ⚠️ ne fonctionne pas !!!
    r"WIFI:T:<type_de_sécurité>;S:<SSID>;P:<mot_de_passe>;H:<caché_ou_non>;",
    r"WIFI:T:WEP;S:CLARO_5697Rg;P:Ne1ed1TaPers0nne;H:true;",
    "/gd/5sq564fze546cx8er8q",
    "<fr>Bonjour#e",
    "<es>Hola !#d",
    "<en>Hi!",
    "Coucou#e",
    "Ça va ?#d",
    "Ça fonctionne bien",
    "_bm_ou",
    "_es_GATEAU",
    "<frC>Hola !#d",

]

for t in tests:
    print(qr_parser(t))

