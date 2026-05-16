# Structures de données MAEL Scan

- Associations : préfixes | paramètres des voix de synthèse
- 

> Tu es spécialiste des structures de données sous Python 3. 
>
> Voici le contexte. J'utilise un système embarqué sur un Raspberry pi Zéro 2W programmé en "Python 3.13". J'ai besoin de gérer des  données ayant à peu près cette structure : 50 clés (ou plus) à chacune desquelles est associée une liste de 3 ou 4 valeurs. Les clés et les valeurs sont de type string. Ces données sont statiques. Elles ne seront pas modifiées lors de l'utilisation de mon programme. Mon application ne nécessite une consultation de ces données que toutes les 5s à 3 min. J'hésite entre ces solutions : 
>
> - Des variables globales de type dictionnaire - Une classe contenant les dictionnaires 
>
> - Des classe dédiées (data class ?) Notion que je ne maîtrise pas (encore) 
>
> - Une base de données SQLite 
>
> 1- Fais-moi un exposé de toutes les solutions existant en "python 3.13" pour créer les structures de données que j'ai décrites. 
>
> 2- Puis fais-moi un comparatif en tenant compte de mon contexte (sur la SD d'un RPi Zéro 2W)

---

ChatGPT

Très bonne question — et ton contexte (RPi Zero 2W + données statiques + accès peu fréquent) change énormément le choix optimal. Je vais structurer la réponse comme un vrai cours d’architecture Python embarqué.

------

# 1️⃣ Panorama COMPLET des solutions en Python 3.13

## 🔹 1. Dictionnaire simple (`dict`)

### Exemple

```python
DATA = {
    "wifi": ["ssid", "password", "channel"],
    "bluetooth": ["on", "off", "discoverable"],
}
```

### ✔️ Avantages

- Ultra simple
- Très rapide en accès (hash table optimisée en C)
- Idéal pour données statiques
- Faible overhead mental

### ❌ Inconvénients

- Pas de typage strict
- Risque d’erreurs sur les clés
- Peu structuré si ça grossit

👉 En Python 3.12+, les dict sont encore plus rapides (~2.3M ops/sec) ([Technical news about AI, coding and all](https://dasroot.net/posts/2026/01/modern-python-312-features-type-hints-generics-performance/?utm_source=chatgpt.com))

------

## 🔹 2. Dictionnaire typé (`TypedDict`)

```python
from typing import TypedDict

class Config(TypedDict):
    wifi: list[str]
    bluetooth: list[str]
```

### ✔️

- Typage statique (mypy, IDE)
- Toujours un dict → rapide

### ❌

- Aucun gain runtime
- Complexité inutile pour petit projet

------

## 🔹 3. Classe classique

```python
class Config:
    def __init__(self):
        self.wifi = ["ssid", "password"]
```

### ✔️

- Structure claire
- Ajout de logique possible

### ❌

- Plus verbeux
- Overkill pour données statiques

------

## 🔹 4. `@dataclass`

```python
from dataclasses import dataclass

@dataclass
class Config:
    wifi: list[str]
    bluetooth: list[str]
```

### ✔️

- Très lisible
- Génère `__init__`, `__repr__`, etc.
- Typage clair
- Peut être immutable (`frozen=True`)

### ❌

- Plus lourd en mémoire (objet + dict interne) ([CodeArchPedia.com](https://openillumi.com/en/en-python-dataclass-namedtuple-performance/?utm_source=chatgpt.com))

👉 Optimisation possible :

```python
@dataclass(slots=True, frozen=True)
class Config:
    wifi: tuple[str, ...]
```

➡️ `slots=True` réduit fortement la mémoire ([Practical Python Programming](https://www.python.digibeatrix.com/en/functions-classes/python-dataclass-advanced-usage-guide/?utm_source=chatgpt.com))

------

## 🔹 5. `NamedTuple` (très intéressant pour toi)

```python
from typing import NamedTuple

class Config(NamedTuple):
    wifi: tuple[str, ...]
    bluetooth: tuple[str, ...]
```

### ✔️

- Ultra léger en mémoire (−50 à −70%) ([CodeArchPedia.com](https://openillumi.com/en/en-python-dataclass-namedtuple-performance/?utm_source=chatgpt.com))
- Immutable (parfait pour données statiques)
- Très rapide
- Structure claire

### ❌

- Peu flexible (pas de mutation)
- Moins "orienté objet"

------

## 🔹 6. Fichier externe (JSON / YAML / TOML)

```json
{
  "wifi": ["ssid", "password"]
}
```

### ✔️

- Séparation code / données
- Modifiable sans recompiler
- Très courant en embarqué

### ❌

- Lecture disque (mais négligeable ici)
- Parsing au démarrage

------

## 🔹 7. SQLite

```sql
CREATE TABLE config (key TEXT, value TEXT);
```

### ✔️

- Structuré
- Requêtes puissantes
- Persistance robuste

### ❌

- Beaucoup trop lourd pour ton besoin
- Accès disque + moteur SQL
- Complexité inutile

------

## 🔹 8. Constantes Python optimisées

```python
DATA = {
    "wifi": ("ssid", "password")
}
```

👉 Utiliser `tuple` au lieu de `list`

- Immutable
- Moins de mémoire
- Plus rapide

------

# 2️⃣ Comparatif dans TON CONTEXTE (RPi Zero 2W)

## ⚙️ Ton cas :

- ~50 clés
- 3–4 valeurs
- données **statiques**
- accès **rare (5s à 3 min)**
- hardware limité (RAM + SD)

------

## 🧠 Critères importants

| Critère     | Importance         |
| ----------- | ------------------ |
| Mémoire     | ⭐⭐⭐                |
| Simplicité  | ⭐⭐⭐                |
| Performance | ⭐⭐ (faible besoin) |
| Maintenance | ⭐⭐⭐                |

------

## 🥊 Comparatif réel

| Solution        | RAM  | CPU  | Simplicité | Adapté        |
| --------------- | ---- | ---- | ---------- | ------------- |
| dict + list     | 🟢    | 🟢    | 🟢🟢🟢        | ✅ excellent   |
| dict + tuple    | 🟢🟢   | 🟢    | 🟢🟢🟢        | ⭐⭐⭐ MEILLEUR  |
| dataclass       | 🟡    | 🟢    | 🟢🟢         | OK            |
| dataclass slots | 🟢    | 🟢    | 🟡          | bien          |
| NamedTuple      | 🟢🟢   | 🟢🟢   | 🟡          | ⭐⭐⭐ excellent |
| JSON fichier    | 🟢    | 🟡    | 🟢🟢         | très bien     |
| SQLite          | 🔴    | 🔴    | 🔴          | ❌ inutile     |

------

# 🧾 Conclusion claire (adaptée à TON cas)

## 🥇 Meilleur choix (simple et efficace)

```python
DATA = {
    "wifi": ("ssid", "password"),
    "bluetooth": ("on", "off")
}
```

👉 Pourquoi :

- minimal RAM
- ultra rapide
- zéro complexité
- parfait pour statique

------

## 🥈 Alternative propre (si tu veux structurer)

👉 `NamedTuple`

- si tu veux une "forme objet"
- très optimisé mémoire

------

## 🥉 Alternative évolutive

👉 JSON + dict

- si tu veux modifier les données sans toucher au code

------

## ❌ À éviter

- SQLite → overkill total
- classes complexes → inutile ici

------

# 💡 Recommandation d’expert embarqué

Sur un Raspberry Pi Zero 2W :

👉 **La meilleure architecture =**

```python
# data.py
DATA = {
    "wifi": ("ssid", "password"),
}
```

- 

```python
from data import DATA
```

✔️ Simple
✔️ Rapide
✔️ Aucun coût inutile

------

> Je ne connais pas les "NamedTuple".
> Explique-moi ce que c'est et quels sont ses avantages / inconvénients.

---

| **Caractéristique** | **Dictionnaire (dict)** | **NamedTuple**        |
| ------------------- | ----------------------- | --------------------- |
| **Accès**           | `data["lieu"]`          | `data.lieu`           |
| **Modifiable**      | Oui ✅                   | Non ❌ (Immuable)      |
| **Poids RAM**       | Moyen ⚠️                 | Très léger ✅          |
| **Auto-complétion** | Souvent absente         | Excellente dans l'IDE |

---

> Donne-moi des exemples de scripts commentés de création et d'usage des NamedTuple.

---

C'est une excellente idée de passer à la pratique. Les `NamedTuple` se déclinent principalement en deux versions. Nous allons nous concentrer sur la version du module `typing`, car elle est la plus adaptée à **Python 3.13** grâce à sa syntaxe claire et son support du typage.

Voici deux exemples concrets pour illustrer comment structurer vos données de capteurs. 🛠️

------

### 1. Définition et usage de base

Ce script montre comment créer la structure et accéder aux données.

```python
from typing import NamedTuple

# 🏗️ Définition de la structure
class InfoCapteur(NamedTuple):
    localisation: str
    type_mesure: str
    unite: str

# 💿 Création d'une instance (objet)
salon = InfoCapteur(localisation="Salon", type_mesure="Température", unite="°C")

# 🔍 Accès aux données
print(f"Lieu : {salon.localisation}") # Accès par nom (très lisible)
print(f"Unité : {salon[2]}")          # Accès par indice (comme un tuple classique)
```

### 2. Organisation sous forme de dictionnaire

Dans votre cas (50 clés), l'idéal est de stocker ces `NamedTuple` dans un dictionnaire global.

```python
from typing import NamedTuple

class ConfigCapteur(NamedTuple):
    nom_long: str
    frequence_secondes: int
    alerte_seuil: float

# 📚 Votre base de données statique
BASE_CAPTEURS = {
    "sensor_01": ConfigCapteur("Thermostat Principal", 300, 25.5),
    "sensor_02": ConfigCapteur("Sonde Extérieure", 60, -5.0),
}

# 🚀 Exemple d'usage dans une boucle
def verifier_capteurs():
    for id_technique, config in BASE_CAPTEURS.items():
        print(f"Vérification de {config.nom_long} (ID: {id_technique})...")
        # On peut accéder directement aux attributs nommés
        if config.frequence_secondes < 100:
            print("  -> Mode haute fréquence activé.")

verifier_capteurs()
```

------

### Pourquoi est-ce avantageux pour votre code ?

Le `NamedTuple` agit comme un "contrat". Une fois défini, vous ne pouvez pas vous tromper sur le nom des champs. Si vous essayez d'écrire `config.unite_mesure` alors que vous avez défini `unite`, votre éditeur de code vous le signalera immédiatement.

Pour la suite, j'ai deux propositions pour approfondir :

1. **Exploration de l'immuabilité** : Nous pourrions voir ce qui se passe si on essaie de modifier une valeur et comment gérer les "mises à jour" de données statiques si besoin.
2. **Passage à l'échelle** : Nous pourrions voir comment charger ces 50 `NamedTuple` proprement depuis un fichier externe (comme un JSON) pour ne pas encombrer votre script principal.

---

NamedTuple n'apporte que l'appel par nom (comme un dico) mais il complexifie le code. Il nécessite une instanciation en plus...

Structure du dictionnaire :

```python
# data.py
DATA = {
    "qr_MAEL": ("Python_gtts", "Android", "iOS", "api_MAEL"),
}
```

Structure NamedTuple (à étudier)

```python
from typing import NamedTuple

# 🏗️ Définition de la structure
class InfoCapteur(NamedTuple):
    qr_MAEL: str
    Python_gtts: str
    Android: str
    iOS: str
    api_MAEL: str

# 💿 Création d'une instance (objet)
salon = InfoCapteur(localisation="Salon", type_mesure="Température", unite="°C")

# 🔍 Accès aux données
print(f"Lieu : {salon.localisation}") # Accès par nom (très lisible)
print(f"Unité : {salon[2]}")          # Accès par indice (comme un tuple classique)
```

