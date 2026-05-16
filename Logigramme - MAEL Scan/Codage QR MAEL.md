# Contenu des codes QR

 

## 1- Codes QR Wifi

```py
WIFI:							# Mot-clé pour déclarer que c'est un QR Wifi
    T:<type_de_sécurité>;		# Type de sécurité : `WPA`, `WEP`, `nopass`
	S:<SSID>;					# Nom du réseau Wifi
	P:<mot_de_passe>;			# Mot de passe (facultatif si T:nopass)
	H:<caché_ou_non>;			# Caché ou non "True", "False" = ""
;
```

**Exemple :**

`WIFI:T:WPA;S:CLARO1_F53E79;P:c024ZwRKpG;H:;;`

:arrow_forward: Voir doc .md **Analyse des Codes QR Wifi**

## 2- Codes QR d’accès à un .mp3 sur cloud

| Type de Drive                                                | Préfixe | Payload       | Suffixe |
| ------------------------------------------------------------ | ------- | ------------- | ------- |
| Google Drive                                                 | `/gd/`    | ID du fichier | aucun   |
| :pick: MAEL Drive                                            | `/md/`    | ?             | aucun   |
| :pick: https://lasuite.numerique.gouv.fr/ Drive nommé : "Fichier" | `/ls/` ?  | ?             | aucun   |

**Exemple : **

`/gd/1WQdqf6ZL96EvWNi7ZP606QXG7AWixqpX`

## 3- Codes QR lecture des fichiers .mp3 internes


| Type de contenu                          | Préfixe | Payload | Suffixe |
| ---------------------------------------- | ------- | ------- | ------- |
| Sons Borel Mayisony (fr)                 | `_bm_`    | lettres | aucun   |
| Mots de l'Abécedaire trilingue français  | `_fr_`    | lettres | aucun   |
| Mots de l'Abécedaire trilingue espagnol  | `_es_`    | lettres | aucun   |
| Mots de l'Abécedaire trilingue portugais | `_pt_`    | lettres | aucun   |

Arrêter avec les `*` et les `-` tout passer avec le `_` ?

## 4- Codes QR des textes à vocaliser

Voix utilisées au LVH :

| Langue    | Préfixe        | Payload | Suffixes possibles |
| --------- | -------------- | ------- | ------------------ |
| français  | `<fr>` ou rien | lettres | #c / #d / #e       |
| espagnol  | `<es>`         | lettres | #c / #d / #e       |
| anglais   | `<en>`         | lettres | #c / #d / #e       |
| portugais | `<pt>`         | lettres | #c / #d / #e       |
| Italien   | `<it>`         | lettres | #c / #d / #e       |
| Chinois   | `<zh>`         | lettres | #c / #d / #e       |

### 1) Fonction "Lire" :arrow_forward: aucun suffixe

Lit `payload` dans la langue indiquée par le préfixe et l'affiche sur l'écran.

### 2) Fonction "Cacher" :arrow_forward: suffixe = `#c`

Lit `payload` dans la langue indiquée par le préfixe et affiche à l'écran : `Écoute bien`.

### 3) Fonction "Dicter" :arrow_forward: suffixe = `#d`

Lit `payload` dans la langue indiquée par le préfixe ***ainsi que la ponctuation par le préfixe*** et affiche `Écoute la dictée`.

### 4) Fonction "Épeler" :arrow_forward: suffixe = `#e`

Lire `toPronounce` (Lettres séparées par des virgules) dans la langue indiquée par le préfixe ***ainsi que la ponctuation par le préfixe*** et affiche `Écoute la dictée`.

---

Dans tous les modes, il sera possible de faire "play / pause / +5s / -5s"

Il faut compléter le tableau de correspondances :  
- "lettres spéciales ou accentuées / majuscules / traits d'union" --> "comment les prononcer" 
- "signes de ponctuation" --> "comment les prononcer" 

 :arrow_forward: Pour au moins les 6 langues de l'école !!!

---

Langues gérées par `gtts` sont celles disponibles sur ***Google Traduction***.

```python
from gtts import gTTS
import gtts.lang
print(gtts.lang.tts_langs())
```

### 1- Le tableau

| Balise MAEL Scan | Code gtts python | Voix locale Android | Voix locale iOS | voix API MAEL |
| :--- | :--- | :--- | :--- | :--- |
| af | af | af | | |
| am | am | am | | |
| ar | ar | ar | | |
| bg | bg | bg | | |
| bn | bn | bn | | |
| bs | bs | bs | | |
| ca | ca | ca | | |
| cs | cs | cs | | |
| cy | cy | cy | | |
| da | da | da | | |
| de | de | de | | |
| el | el | el | | |
| en | en | enGBR | | |
| enU | | enUSA | | |
| enB | | enGBR | | |
| enI | | enIND | | |
| es | es | esUSA | | |
| esE | es | esESP | | |
| et | et | et | | |
| eu | eu | eu | | |
| fi | fi | fi | | |
| fr ou rien | fr | fr | | |
| frC | fr-CA | frCAN | | |
| gl | gl | gl | | |
| gu | gu | gu | | |
| ha | ha | ha | | |
| hi | hi | hi | | |
| hr | hr | hr | | |
| hu | hu | hu | | |
| id | id | id | | |
| is | is | is | | |
| it | it | it | | |
| iw | iw | iw | | |
| ja | ja | ja | | |
| jw | jw | jw | | |
| km | km | km | | |
| kn | kn | kn | | |
| ko | ko | ko | | |
| la | la | la | | |
| lt | lt | lt | | |
| lv | lv | lv | | |
| ml | ml | ml | | |
| mr | mr | mr | | |
| ms | ms | ms | | |
| my | my | my | | |
| ne | ne | ne | | |
| nlB | nl | nlBEL | | |
| nl | nl | nl | | |
| no | no | no | | |
| pa | pa | pa | | |
| pl | pl | pl | | |
| pt | pt | pt | | |
| ptP | pt-PT | ptPRT | | |
| ro | ro | ro | | |
| ru | ru | ru | | |
| si | si | si | | |
| sk | sk | sk | | |
| sq | sq | sq | | |
| sr | sr | sr | | |
| su | su | su | | |
| sv | sv | sv | | |
| sw | sw | sw | | |
| ta | ta | ta | | |
| te | te | te | | |
| th | th | th | | |
| tl | tl | tl | | |
| tr | tr | tr | | |
| uk | uk | uk | | |
| ur | ur | ur | | |
| vi | vi | vi | | |
| yue | yue | yue | | |
| zhC | zh-CN | zh-CN | | |
| zhT | zh-TW | zh-TW | | |
| zh | zh | zh | | |

### 2- Le dictionnaire

```python
DATA = {
    "af": ("af", "af", "", ""),
    "am": ("am", "am", "", ""),
    "ar": ("ar", "ar", "", ""),
    "bg": ("bg", "bg", "", ""),
    "bn": ("bn", "bn", "", ""),
    "bs": ("bs", "bs", "", ""),
    "ca": ("ca", "ca", "", ""),
    "cs": ("cs", "cs", "", ""),
    "cy": ("cy", "cy", "", ""),
    "da": ("da", "da", "", ""),
    "de": ("de", "de", "", ""),
    "el": ("el", "el", "", ""),
    "en": ("en", "enGBR", "", ""),
    "enU": ("", "enUSA", "", ""),
    "enB": ("", "enGBR", "", ""),
    "enI": ("", "enIND", "", ""),
    "es": ("es", "esUSA", "", ""),
    "esE": ("es", "esESP", "", ""),
    "et": ("et", "et", "", ""),
    "eu": ("eu", "eu", "", ""),
    "fi": ("fi", "fi", "", ""),
    "fr": ("fr", "fr", "", ""),
    "frC": ("fr-CA", "frCAN", "", ""),
    "gl": ("gl", "gl", "", ""),
    "gu": ("gu", "gu", "", ""),
    "ha": ("ha", "ha", "", ""),
    "hi": ("hi", "hi", "", ""),
    "hr": ("hr", "hr", "", ""),
    "hu": ("hu", "hu", "", ""),
    "id": ("id", "id", "", ""),
    "is": ("is", "is", "", ""),
    "it": ("it", "it", "", ""),
    "iw": ("iw", "iw", "", ""),
    "ja": ("ja", "ja", "", ""),
    "jw": ("jw", "jw", "", ""),
    "km": ("km", "km", "", ""),
    "kn": ("kn", "kn", "", ""),
    "ko": ("ko", "ko", "", ""),
    "la": ("la", "la", "", ""),
    "lt": ("lt", "lt", "", ""),
    "lv": ("lv", "lv", "", ""),
    "ml": ("ml", "ml", "", ""),
    "mr": ("mr", "mr", "", ""),
    "ms": ("ms", "ms", "", ""),
    "my": ("my", "my", "", ""),
    "ne": ("ne", "ne", "", ""),
    "nlB": ("nl", "nlBEL", "", ""),
    "nl": ("nl", "nl", "", ""),
    "no": ("no", "no", "", ""),
    "pa": ("pa", "pa", "", ""),
    "pl": ("pl", "pl", "", ""),
    "pt": ("pt", "pt", "", ""),
    "ptP": ("pt-PT", "ptPRT", "", ""),
    "ro": ("ro", "ro", "", ""),
    "ru": ("ru", "ru", "", ""),
    "si": ("si", "si", "", ""),
    "sk": ("sk", "sk", "", ""),
    "sq": ("sq", "sq", "", ""),
    "sr": ("sr", "sr", "", ""),
    "su": ("su", "su", "", ""),
    "sv": ("sv", "sv", "", ""),
    "sw": ("sw", "sw", "", ""),
    "ta": ("ta", "ta", "", ""),
    "te": ("te", "te", "", ""),
    "th": ("th", "th", "", ""),
    "tl": ("tl", "tl", "", ""),
    "tr": ("tr", "tr", "", ""),
    "uk": ("uk", "uk", "", ""),
    "ur": ("ur", "ur", "", ""),
    "vi": ("vi", "vi", "", ""),
    "yue": ("yue", "yue", "", ""),
    "zhC": ("zh-CN", "zh-CN", "", ""),
    "zhT": ("zh-TW", "zh-TW", "", ""),
    "zh": ("zh", "zh", "", ""),
}
```



### 3- Le NamedTuple

Pas au point !!!

```python
from typing import NamedTuple

# 🏗️ Définition de la structure
class LangueConfig(NamedTuple):
    python_gtts: str
    android: str
    ios: str
    api_mael: str

# 📚 Dictionnaire complet des correspondances
# Structure : "qr_MAEL": LangueConfig(python_gtts, android, ios, api_mael)
DATA_LANGUES = {
    "af": LangueConfig("af", "af", "", ""),
    "am": LangueConfig("am", "am", "", ""),
    "ar": LangueConfig("ar", "ar", "", ""),
    "bg": LangueConfig("bg", "bg", "", ""),
    "bn": LangueConfig("bn", "bn", "", ""),
    "bs": LangueConfig("bs", "bs", "", ""),
    "ca": LangueConfig("ca", "ca", "", ""),
    "cs": LangueConfig("cs", "cs", "", ""),
    "cy": LangueConfig("cy", "cy", "", ""),
    "da": LangueConfig("da", "da", "", ""),
    "de": LangueConfig("de", "de", "", ""),
    "el": LangueConfig("el", "el", "", ""),
    "en": LangueConfig("en", "enGBR", "", ""),
    "enU": LangueConfig("", "enUSA", "", ""),
    "enB": LangueConfig("", "enGBR", "", ""),
    "enI": LangueConfig("", "enIND", "", ""),
    "es": LangueConfig("es", "esUSA", "", ""),
    "esE": LangueConfig("es", "esESP", "", ""),
    "et": LangueConfig("et", "et", "", ""),
    "eu": LangueConfig("eu", "eu", "", ""),
    "fi": LangueConfig("fi", "fi", "", ""),
    "fr": LangueConfig("fr", "fr", "", ""),  # "fr ou rien" géré ici par la clé "fr"
    "frC": LangueConfig("fr-CA", "frCAN", "", ""),
    "gl": LangueConfig("gl", "gl", "", ""),
    "gu": LangueConfig("gu", "gu", "", ""),
    "ha": LangueConfig("ha", "ha", "", ""),
    "hi": LangueConfig("hi", "hi", "", ""),
    "hr": LangueConfig("hr", "hr", "", ""),
    "hu": LangueConfig("hu", "hu", "", ""),
    "id": LangueConfig("id", "id", "", ""),
    "is": LangueConfig("is", "is", "", ""),
    "it": LangueConfig("it", "it", "", ""),
    "iw": LangueConfig("iw", "iw", "", ""),
    "ja": LangueConfig("ja", "ja", "", ""),
    "jw": LangueConfig("jw", "jw", "", ""),
    "km": LangueConfig("km", "km", "", ""),
    "kn": LangueConfig("kn", "kn", "", ""),
    "ko": LangueConfig("ko", "ko", "", ""),
    "la": LangueConfig("la", "la", "", ""),
    "lt": LangueConfig("lt", "lt", "", ""),
    "lv": LangueConfig("lv", "lv", "", ""),
    "ml": LangueConfig("ml", "ml", "", ""),
    "mr": LangueConfig("mr", "mr", "", ""),
    "ms": LangueConfig("ms", "ms", "", ""),
    "my": LangueConfig("my", "my", "", ""),
    "ne": LangueConfig("ne", "ne", "", ""),
    "nlB": LangueConfig("nl", "nlBEL", "", ""),
    "nl": LangueConfig("nl", "nl", "", ""),
    "no": LangueConfig("no", "no", "", ""),
    "pa": LangueConfig("pa", "pa", "", ""),
    "pl": LangueConfig("pl", "pl", "", ""),
    "pt": LangueConfig("pt", "pt", "", ""),
    "ptP": LangueConfig("pt-PT", "ptPRT", "", ""),
    "ro": LangueConfig("ro", "ro", "", ""),
    "ru": LangueConfig("ru", "ru", "", ""),
    "si": LangueConfig("si", "si", "", ""),
    "sk": LangueConfig("sk", "sk", "", ""),
    "sq": LangueConfig("sq", "sq", "", ""),
    "sr": LangueConfig("sr", "sr", "", ""),
    "su": LangueConfig("su", "su", "", ""),
    "sv": LangueConfig("sv", "sv", "", ""),
    "sw": LangueConfig("sw", "sw", "", ""),
    "ta": LangueConfig("ta", "ta", "", ""),
    "te": LangueConfig("te", "te", "", ""),
    "th": LangueConfig("th", "th", "", ""),
    "tl": LangueConfig("tl", "tl", "", ""),
    "tr": LangueConfig("tr", "tr", "", ""),
    "uk": LangueConfig("uk", "uk", "", ""),
    "ur": LangueConfig("ur", "ur", "", ""),
    "vi": LangueConfig("vi", "vi", "", ""),
    "yue": LangueConfig("yue", "yue", "", ""),
    "zhC": LangueConfig("zh-CN", "zh-CN", "", ""),
    "zhT": LangueConfig("zh-TW", "zh-TW", "", ""),
    "zh": LangueConfig("zh", "zh", "", ""),
}


```





