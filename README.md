![MAEL](https://github.com/Yobeco/MAEL_Phono_fouille/blob/main/readme_assets/Logo-MAEL-120.png "Logo du projet MAEL")

# MAEL Scan

*Une application appartenant au [__projet MAEL__](https://github.com/Yobeco/MAEL_Project)*   
Copyright (c) 2022 Yonnel Bécognée

[![License: Libre Non Commerciale](https://img.shields.io/badge/license-GNU%20GENERAL%20PUBLIC%20LICENSE%20V3-white.svg)](./LICENSE)

[![Python](https://img.shields.io/badge/Python-V3.10%2B-blue?logo=python&logoColor=yellow)](https://www.python.org/)

[![SQLite](https://img.shields.io/badge/SQLite-V3.50.4%2B-003366?logo=sqlite&logoColor=99CCFF)](https://sqlite.org/)

[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-009900.svg)](#contributing) [![Beginner friendly](https://img.shields.io/badge/Beginner%20friendly-FF8000)]()

[![Status: Active](https://img.shields.io/badge/status-active-009900.svg)]()

## :fr: [Français](https://github.com/Yobeco/MAEL_Scan_pi) | :gb: English

---

![](https://github.com/Yobeco/MAEL_Project/blob/main/readme_assets/MAEL-Scan2-seul-350px.png)


## A- Description :eye:

**MAEL Scan Pi** est une application embarquée sur Raspberry  Pi <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />) qui permet à l'élève de flasher les code QR créés par son professeur avec **MAEL Gen** et d'écouter leur contenu :speaker:.   
Son interface est conçue pour être utilisée par un enfant, dés 4 ans :baby:.   

L'objectif de la version sans téléphone est de :

- ne pas mettre un téléphone dans les mains (surtout pour lesplus jeunes élèves).
- créer une bel objet incarnant le début d'un apprentissage important (Contrat pédagogique)

**MAEL Scan** permet aux élèves ne possédant aucun "parlant" chez lui d'écouter la langue étudiée dans un contexte pédagogique élaboré par son professeur :100:. Elle permet donc au professeur de **booster son enseignement d'une langue** :chart_with_upwards_trend:.

**Potentiellement 55 langues sont implémentables !** :astonished:

:fr: :gb: :es: :portugal: :brazil: :it: :de: :ru: :jp: :cn: :kr: ...

---

## B- Fonctionnalités :clipboard:

Voir le projet [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan)

---

## C- Comment utiliser MAEL Scan ? :blush:

Voir le projet [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan)

---

## D- Principe de fonctionnement :gear:

*(Pour aider à la compréhension du code)*

---

Le principe de fonctionnement sera le même que le projet [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan) sur téléphone.

Cependant, MAEl Scan Pi possède des propriétés hardware :

### "MAEL Scan Pi" V1

| Fonction | Solution trouvée |
|--------|--------------------|
| Carte mère | Raspberry Pi 4 8Go |
| Système dexploitation | [Pi OS Debian V13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) |
| Synthèse vocale | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) |
| Lecture audio | aplay (linux Bash) |
| UPS (gestion des batteries) | MakerFocus Raspberry Pi 4 Battery Pack UPS |
| Amplificateur audio | LM386  |
| Scanner les codes QR | module caméra V2.1 |
| Reconnaissance des codes QR | OpenCV |
| Écran | WaveShare 2.7inch E-Ink Display HAT |
| Boitier | Boitier recyclé d'un vieux modem |

**Qualités :**

- Prototype pour découvrir les difficultés

**Défauts :**

- Encombrant
- Boitier peu ergonomique
- Difficile de scanner les codes QR (Il faut prendre une photo, l'envoyer à OpenCV qui peine à lire le code QR...)
- Parasites très génants dans le haut-parleur (LM386 sensible, sans pré-ampli)

⟶ Démantelé pour créer la version 2

### "MAEL Scan Pi" V2

| Fonction | Solution actuelle |
|--------|--------------------|
| Carte mère | Raspberry Pi 4 8Go |
| Système dexploitation | [Pi OS Debian 13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) |
| Synthèse vocale | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) |
| Lecture audio | aplay (linux Bash) |
| UPS (gestion des batteries) | MakerFocus Raspberry Pi 4 Battery Pack UPS |
| Amplificateur audio | XS9871 Mini Module de classe AB  |
| Scanner les codes QR | Useful Sensors Tiny Code Reader |
| Éclairage des codes QR | 2 LED |
| Écran | WaveShare 2.7inch E-Ink Display HAT |
| Boitier | Boitier recyclé d'un vieux modem |

**Qualités :**

- Fonctionnel : codes QR facilement scannés
- Synthèse vocale embarquée (pas besoin de connexion internet)
- Bonne autonomie
- Son de meilleure qualité

**Défauts :**

- Encombrant
- Boitier peu ergonomique
- Code QR de 254 octets max soit 40 caractères ASCII (moins si accents, caractères étrangers...). C'est une limite harware du Tiny sensor. **Insuffisant** !
- Quelques défauts parfois dans la voix Piper TTS (Créer notre propre modèle de voix ? C'est possible)

⟶ Fonctionnel mais le code est encore brouillon

### "MAEL Scan Pi" V3

En cours de construction

| Fonction | Solution prévue |
|:--------:|--------------------|
| Carte mère | Raspberry Pi zero 2W 512 Mo (+ Zram) |
| Système dexploitation | [Pi OS Debian Lite V13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) |
| Synthèse vocale | GTTS (ou Service de synthèse vocale hébergée sur MAEL Phrase) |
| Lecture audio | aplay (linux Bash) |
| UPS (gestion des batteries) | Uninterruptible Power Supply UPS HAT For Raspberry Pi Zero |
| Amplificateur audio | RPi Speaker HAT PWM Sound Card GPIO Audio Amplification
 |
| Scanner les codes QR | GM861S-LED |
| Éclairage des codes QR | intégré au module GM861S |
| Écran | Waveshare 3.52inch e-Paper Display (B), e-Ink Red/Black/White |


**Qualités :**

- Plus petit et léger
- Boitier imprimé en 3D
- Écran couleur
- Sortie audio Jack !

**Défauts :**

- Devra être connecté pour la voix de synthèse
- Des boutons à connecter à la carte mère au lieu d'un écran tactile. Plus compliqué !

⟶ J'ai une partie du hardware

---

## E- Fonctionnalités à développer :rocket:

Les mêmes que pour **MAEL Scan**

### :+1: Proposez votre aide pour developper _MAEL Scan Pi_


---

## F- Participez au projet MAEL :open_hands:

:sos: Pour **obtenir de l'aide** concernant l'utilisation de MAEL ou pour **paticiper au développement** :computer:, écrivez-moi ici :

### :mailbox_with_mail: ***[mael@lvh.edu.ni](mailto:mael@lvh.edu.ni)***

### :star2: Contributeurs

Un grand merci à toutes les personnes qui vont contribuer à ce projet !

 | Avatar | Nom                | GitHub                          | Rôle                     |
 |--------|--------------------|---------------------------------|--------------------------|
 | ![Bécognée Yonnel](https://github.com/Yobeco.png?size=50) | Bécognée Yonnel | [@Yobeco](https://github.com/Yobeco) | Mainteneur |
 | ... | ... | ... | Développeur |
 | ... | ... | ... | Développeuse |
 | ... | ... | ... | Traductrice |

---

## G- Installation :arrow_heading_down:

Seule la version Android <img src="https://cdn.simpleicons.org/android/FFFF" width="24" height="24" style="vertical-align: middle;" /> *MIT App Inventor* est fonctionnelle pour le moment.   
:inbox_tray: Pour essayer **MAEL Scan** [Télécharger le fichier MAEL_Scan_V5_0.apk](https://raw.githubusercontent.com/Yobeco/MAEL_Scan/main/binary_exec/MAEL_Scan_V5_0.apk)


