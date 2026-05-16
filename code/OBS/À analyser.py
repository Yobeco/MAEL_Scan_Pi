# Classe qui contiendra les données du code QR Wifi
@dataclass
class WifiConfig:
    ssid: str
    security: str = "nopass"
    password: str | None = None
    hidden: bool = False

# Fonction pour récupérer le contenu d'un code QR Wifi
# -> annotation de retour (Return Type Hint) : la sortie sera une instance de la classe WifiConfig
def wifi_parser(raw_str: str) -> WifiConfig:
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
