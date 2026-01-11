<!-- multilingual suffix: fr, en -->

<!--[fr]-->
![MAEL](https://github.com/Yobeco/MAEL_Phono_fouille/blob/main/readme_assets/Logo-MAEL-120.png "Logo du projet MAEL")

<!--[en]-->
![MAEL](https://github.com/Yobeco/MAEL_Phono_fouille/blob/main/readme_assets/Logo-MAEL-120.png "MAEL project logo")

<!--[fr]-->
# MAEL Scan Pi

<!--[en]-->
# MAEL Scan Pi

<!--[fr]-->
*Une application appartenant au [__projet MAEL__](https://github.com/Yobeco/MAEL_Project)*   
Copyright (c) 2024 Yonnel Bécognée

<!--[en]-->
*An application belonging to the [__MAEL project__](https://github.com/Yobeco/MAEL_Project)*   
Copyright (c) 2024 Yonnel Bécognée

<!--[fr]-->
[![License: Libre Non Commerciale](https://img.shields.io/badge/license-GNU%20GENERAL%20PUBLIC%20LICENSE%20V3-white.svg)](./LICENSE)

<!--[en]-->
[![License: Libre Non Commerciale](https://img.shields.io/badge/license-GNU%20GENERAL%20PUBLIC%20LICENSE%20V3-white.svg)](./LICENSE)

<!--[common]-->
[![Python](https://img.shields.io/badge/Python-V3.10%2B-blue?logo=python&logoColor=yellow)](https://www.python.org/)

<!--[common]-->
[![SQLite](https://img.shields.io/badge/SQLite-V3.50.4%2B-003366?logo=sqlite&logoColor=99CCFF)](https://sqlite.org/)

<!--[fr]-->
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-009900.svg)](#contributing) [![Beginner friendly](https://img.shields.io/badge/Beginner%20friendly-FF8000)]()

<!--[en]-->
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-009900.svg)](#contributing) [![Beginner friendly](https://img.shields.io/badge/Beginner%20friendly-FF8000)]()

<!--[fr]-->
[![Status: Active](https://img.shields.io/badge/status-active-009900.svg)]()

<!--[en]-->
[![Status: Active](https://img.shields.io/badge/status-active-009900.svg)]()

<!--[common]-->
## :fr: [Français](https://github.com/Yobeco/MAEL_Scan_pi) | :gb: English

<!--[common]-->
---

<!--[common]-->
---

<!--[common]-->
![](./readme_assets/Cartes.jpg)

<!--[common]-->
![](./readme_assets/Ouvert.jpg)

<!--[common]-->
![](./readme_assets/Ferme.jpg)

<!--[common]-->
![](./readme_assets/Dessous.jpg)

<!--[fr]-->
## A- Description :eye:

<!--[en]-->
## A- Description :eye:

<!--[fr]-->
**MAEL Scan Pi** est une application embarquée sur Raspberry  Pi <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" /> qui permet à l'élève de flasher les code QR créés par son professeur avec **MAEL Gen** et d'écouter leur contenu :speaker: sans utiliser de téléphone portable.   
Son interface est conçue pour être utilisée par un enfant, dés 4 ans :baby:.

<!--[en]-->
**MAEL Scan Pi** is an embedded application on Raspberry Pi <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" /> that allows students to scan QR codes created by their teacher with **MAEL Gen** and listen to their content :speaker: without using a mobile phone.   
Its interface is designed to be used by a child from age 4 :baby:.

<!--[fr]-->
L'objectif de la version sans téléphone est de :

<!--[en]-->
The purpose of the phone-free version is to:

<!--[fr]-->
- ne pas mettre un téléphone dans les mains (surtout pour lesplus jeunes élèves). :no_mobile_phones:
- créer une bel objet incarnant le début d'un apprentissage important (Contrat pédagogique).

<!--[en]-->
- avoid giving a phone to the hands (especially for younger students) :no_mobile_phones:
- create a nice object representing the beginning of an important learning process (Pedagogical contract).

<!--[fr]-->
**MAEL Scan Pi** permet aux élèves ne possédant aucun "parlant" chez lui d'écouter la langue étudiée dans un contexte pédagogique élaboré par son professeur :100:. Il permet donc au professeur de **booster son enseignement d'une langue** :chart_with_upwards_trend:.

<!--[en]-->
**MAEL Scan Pi** allows students without any “speaker” at home to listen to the language being studied within a pedagogical context prepared by their teacher :100:. It thus allows the teacher to **boost language teaching** :chart_with_upwards_trend:.

<!--[fr]-->
**Potentiellement 55 langues sont implémentables !** :astonished:

<!--[en]-->
**Potentially 55 languages can be implemented!** :astonished:

<!--[common]-->
:fr: :gb: :es: :portugal: :brazil: :it: :de: :ru: :jp: :cn: :kr: ...

<!--[common]-->
---

<!--[common]-->
---

<!--[fr]-->
## B- Fonctionnalités :clipboard:

<!--[en]-->
## B- Features :clipboard:

<!--[fr]-->
Voir le projet [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan)

<!--[en]-->
See the [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan) project

<!--[common]-->
---

<!--[common]-->
---

<!--[fr]-->
## C- Comment utiliser MAEL Scan ? :blush:

<!--[en]-->
## C- How to use MAEL Scan? :blush:

<!--[fr]-->
L'utilisation devra s'approcher au mieux de la version téléphone.  
Voir le projet [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan)

<!--[en]-->
Usage should mimic the phone version as closely as possible.  
See the [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan) project

<!--[common]-->
---

<!--[common]-->
---

<!--[fr]-->
## D- Principe de fonctionnement :gear:

<!--[en]-->
## D- Operating principle :gear:

<!--[fr]-->
*(Pour aider à la compréhension du code)*

<!--[en]-->
*(To aid code comprehension)*

<!--[common]-->
---

<!--[common]-->
---

<!--[fr]-->
Le principe de fonctionnement sera le même que le projet [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan) sur téléphone.

<!--[en]-->
The operating principle will be the same as the [**MAEL Scan**](https://github.com/Yobeco/MAEL_Scan) phone project.

<!--[fr]-->
Cependant, MAEl Scan Pi possède des propriétés hardware particulières :

<!--[en]-->
However, MAEL Scan Pi has specific hardware properties:

<!--[fr]-->
### "MAEL Scan Pi" V1

<!--[en]-->
### "MAEL Scan Pi" V1

<!--[fr]-->
| Fonction | Solution choisie |
|--------|--------------------|
| Carte mère | Raspberry Pi 4 8Go <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Système dexploitation | [Pi OS Debian V13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) <img src="https://cdn.simpleicons.org/debian/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Synthèse vocale | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) |
| Lecture audio | aplay (linux Bash) |
| UPS (gestion des batteries) | MakerFocus Raspberry Pi 4 Battery Pack UPS |
| Amplificateur audio | LM386  |
| Scanner les codes QR | module caméra V2.1 <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Reconnaissance des codes QR | OpenCV <img src="https://cdn.simpleicons.org/opencv/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Écran | WaveShare 2.7inch E-Ink Display HAT |
| Boitier | Boitier recyclé d'un vieux modem |

<!--[en]-->
| Function | Chosen solution |
|--------|--------------------|
| Motherboard | Raspberry Pi 4 8GB <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Operating system | [Pi OS Debian V13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) <img src="https://cdn.simpleicons.org/debian/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Text-to-speech | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) |
| Audio playback | aplay (Linux Bash) |
| UPS (battery management) | MakerFocus Raspberry Pi 4 Battery Pack UPS |
| Audio amplifier | LM386 |
| QR code scanner | Camera module V2.1 <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| QR code recognition | OpenCV <img src="https://cdn.simpleicons.org/opencv/FFFF" width="24" height="24" style="vertical-align: middle;" />|
| Display | WaveShare 2.7inch E-Ink Display HAT |
| Case | Recycled old modem case |

<!--[fr]-->
**Qualités :**

<!--[en]-->
**Strengths:**

<!--[fr]-->
- Prototype pour découvrir les difficultés :face_with_peeking_eye:

<!--[en]-->
- Prototype to explore difficulties :face_with_peeking_eye:

<!--[fr]-->
**Défauts :**

<!--[en]-->
**Weaknesses:**

<!--[fr]-->
- Encombrant :package:
- Boitier peu ergonomique
- Difficile de scanner les codes QR (Il faut prendre une photo, l'envoyer à OpenCV qui peine à lire le code QR...) :face_with_diagonal_mouth:
- Parasites très génants dans le haut-parleur (LM386 sensible, sans pré-ampli)

<!--[en]-->
- Bulky :package:
- Case not ergonomic
- QR codes hard to scan (must take a photo, send it to OpenCV which struggles to read the QR code...) :face_with_diagonal_mouth:
- Strong interference in the speaker (LM386 sensitive, without preamp)

<!--[fr]-->
⟶ Démantelé pour créer la version 2

<!--[en]-->
⟶ Dismantled to create version 2

<!--[common]-->
---

<!--[fr]-->
### "MAEL Scan Pi" V2

<!--[en]-->
### "MAEL Scan Pi" V2

<!--[fr]-->
| Fonction | Solution actuelle | Prix |
|--------|--------------------|:--------:|
| Carte mère | Raspberry Pi 4 8Go <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />| 104$ |
| Système d’exploitation | [Pi OS Debian 13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) <img src="https://cdn.simpleicons.org/debian/FFFF" width="24" height="24" style="vertical-align: middle;" />| |
| Synthèse vocale | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) |  |
| Lecture audio | aplay (linux Bash) |  |
| UPS (gestion des batteries) | MakerFocus Raspberry Pi 4 Battery Pack UPS | 33$ |
| Amplificateur audio | PAM8403 Mini Module | 1$ |
| Scanner les codes QR | Useful Sensors Tiny Code Reader | 11$ |
| Éclairage des codes QR | 2 LED |  |
| Écran avec 4 boutons | WaveShare 2.7inch E-Ink Display HAT | 23$ |
| Boîtier | Boîtier recyclé d'un vieux modem |  |
|  | Total : | +- 172$ |

<!--[en]-->
| Function | Current solution | Price |
|--------|--------------------|:--------:|
| Motherboard | Raspberry Pi 4 8GB <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />| $104 |
| Operating system | [Pi OS Debian 13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) <img src="https://cdn.simpleicons.org/debian/FFFF" width="24" height="24" style="vertical-align: middle;" />| |
| Text-to-speech | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) | |
| Audio playback | aplay (Linux Bash) | |
| UPS (battery management) | MakerFocus Raspberry Pi 4 Battery Pack UPS | $33 |
| Audio amplifier | PAM8403 Mini Module | $1 |
| QR code scanner | Useful Sensors Tiny Code Reader | $11 |
| QR code lighting | 2 LEDs | |
| Display with 4 buttons | WaveShare 2.7inch E-Ink Display HAT | $23 |
| Case | Recycled old modem case | |
|  | Total: | +- $172 |

<!--[fr]-->
**Qualités :**

<!--[en]-->
**Strengths:**

<!--[fr]-->
- Fonctionnel : codes QR facilement scannés :slightly_smiling_face:
- Synthèse vocale embarquée (pas besoin de connexion internet)
- Bonne autonomie :battery:
- Son de meilleure qualité :musical_note: :+1:

<!--[en]-->
- Functional: QR codes easily scanned :slightly_smiling_face:
- Embedded text-to-speech (no internet connection required)
- Good battery life :battery:
- Better sound quality :musical_note: :+1:

<!--[fr]-->
**Défauts :**

<!--[en]-->
**Weaknesses:**

<!--[fr]-->
- Encombrant
- Boitier peu ergonomique
- Code QR de 254 octets max soit 40 caractères ASCII (moins si accents, caractères étrangers...). C'est une limite harware :straight_ruler: du Tiny sensor. **Insuffisant** ! 
- Quelques défauts parfois dans la voix Piper TTS :neutral_face: (Créer notre propre modèle de voix ? C'est possible)

<!--[en]-->
- Bulky
- Case not very ergonomic
- QR code limited to 254 bytes, i.e. 40 ASCII characters (less with accents or foreign characters...). This is a hardware limitation :straight_ruler: of the Tiny sensor. **Insufficient**!
- Occasional flaws in the Piper TTS voice :neutral_face: (Creating our own voice model? It is possible)

<!--[fr]-->
⟶ Fonctionnel mais le code est encore brouillon

<!--[en]-->
⟶ Functional, but the code is still messy

<!--[common]-->
---

<!--[fr]-->
### "MAEL Scan Pi" V3

<!--[en]-->
### "MAEL Scan Pi" V3

<!--[fr]-->
En cours de construction

<!--[en]-->
Under construction

<!--[fr]-->
| Fonction | Solution prévue | Prix |
|--------|--------------------|:--------------------:|
| Carte mère | Raspberry Pi zero 2W 512 Mo (+ Zram) <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />| 22$ |
| Système d’exploitation | [Pi OS Debian Lite V13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) <img src="https://cdn.simpleicons.org/debian/FFFF" width="24" height="24" style="vertical-align: middle;" />|  |
| Synthèse vocale | GTTS (ou Service de synthèse vocale hébergée sur MAEL Phrase) |  |
| Lecture audio | MOC (Music On Consol) + SOX |  |
| UPS (gestion des batteries) | Uninterruptible Power Supply UPS HAT For Raspberry Pi Zero | 24$ |
| ~~Amplificateur audio~~ | ~~Audio Tech (B) Speaker Tech pour Raspberry Pi zero~~ Son de médiocre qualité :neutral_face: | ~~4$~~ |
| Amplificateur audio | [mic+](https://raspiaudio.com/product/mic/) (DAC + Ampli / HP + Sortie Jack) | 35$ |
| Scanner les codes QR | GM861S-LED | 10$ |
| Éclairage des codes QR | Intégré au module GM861S |  |
| Écran | 2.13inch E-Paper HAT (B), 250x122, Red/Black/White, SPI Interface | 15$ |
| 6 Boutons "Touch" | MPR121 V12 - Capacitive Touch Sensor | 2$ |
| Boîtier impression 3D | PET de bouteilles | ? |
|  | Total : | +- 104$ |

<!--[en]-->
| Function | Planned solution | Price |
|--------|--------------------|:--------------------:|
| Motherboard | Raspberry Pi Zero 2W 512 MB (+ Zram) <img src="https://cdn.simpleicons.org/raspberrypi/FFFF" width="24" height="24" style="vertical-align: middle;" />| $22 |
| Operating system | [Pi OS Debian Lite V13 (trixie)](https://www.raspberrypi.com/software/operating-systems/) <img src="https://cdn.simpleicons.org/debian/FFFF" width="24" height="24" style="vertical-align: middle;" />| |
| Text-to-speech | GTTS (or text-to-speech service hosted on MAEL Phrase) | |
| Audio playback | MOC (Music On Console) + SOX | |
| UPS (battery management) | Uninterruptible Power Supply UPS HAT for Raspberry Pi Zero | $24 |
| ~~Audio amplifier~~ | ~~Audio Tech (B) Speaker Tech for Raspberry Pi Zero~~ Poor sound quality :neutral_face: | ~~$4~~ |
| Audio amplifier | [mic+](https://raspiaudio.com/product/mic/) (DAC + amp / speaker + jack output) | $35 |
| QR code scanner | GM861S-LED | $10 |
| QR code lighting | Integrated into the GM861S module | |
| Display | 2.13inch E-Paper HAT (B), 250x122, Red/Black/White, SPI interface | $15 |
| 6 "Touch" buttons | MPR121 V12 – Capacitive Touch Sensor | $2 |
| 3D-printed case | PET from bottles | ? |
|  | Total: | +- $104 |

<!--[fr]-->
Comme il n'existe pas (encore) d'écran *3.52inch e-Paper Display (B), e-Ink Display, 360x240, Red/Black/White* qui soit tactile pour afficher les boutons sur l'écran, j'ai opté pour des capteurs type "touch sensor" qui seront à l'intérieur du boîtier.   
Et j'ai donc choisi un écran plus petit (et moins cher) mais en 3 couleurs :black_circle::white_circle::red_circle:. Parfait pour le logo de MAEL :smile:.  
J'ai fait un test : un gros code QR (150px) peut contenir +- 120 caractères. Cet écran de 5cm x 2.5cm afficherait ce texte en taille 11px, ce qui est encore acceptable. (Il faudra faire des essais avec une taille de caractère qui est calculée en fonction du nombre de caractères à afficher...)

<!--[en]-->
As there is no (yet) *3.52inch e-Paper Display (B), e-Ink Display, 360x240, Red/Black/White* that is touch-enabled to display buttons directly on the screen, I opted for "touch sensor" type sensors placed inside the case.   
I therefore chose a smaller (and cheaper) screen, but with 3 colors :black_circle::white_circle::red_circle:. Perfect for the MAEL logo :smile:.  
I ran a test: a large QR code (150px) can contain approximately 120 characters. This 5cm x 2.5cm screen would display this text at 11px, which is still acceptable. (Tests will be needed with a font size calculated based on the number of characters to display...)

<!--[common]-->
![Model3D_1](readme_assets/Model3D_1.png)

<!--[common]-->
![Model3D_2](readme_assets/Model3D_2.png)

<!--[fr]-->
**Qualités :**

<!--[en]-->
**Strengths:**

<!--[fr]-->
- Plus petit et léger :snowflake:
- Un boîtier imprimé en 3D <img src="https://cdn.simpleicons.org/blender/FFFF" width="24" height="24" style="vertical-align: middle;" /> prévu
- Écran 3 couleurs !
- 6 boutons tactiles (capacitifs, dans le boîtier directement)
- Sortie audio Jack ! :headphones:
- Ajout d'une fonctionnalité : possibilité de scanner un code QR généré par un téléphone :iphone: pour partager une connexion internet Wifi.

<!--[en]-->
- Smaller and lighter :snowflake:
- Planned 3D-printed case <img src="https://cdn.simpleicons.org/blender/FFFF" width="24" height="24" style="vertical-align: middle;" />
- 3-color screen!
- 6 touch buttons (capacitive, directly inside the case)
- Jack audio output! :headphones:
- Added feature: ability to scan a QR code generated by a phone :iphone: to share an internet Wi-Fi connection.

<!--[fr]-->
**Défauts :**

<!--[en]-->
**Weaknesses:**

<!--[fr]-->
- Devra être connecté pour la voix de synthèse.

<!--[en]-->
- Will require a connection for text-to-speech.

<!--[fr]-->
⟶ J'ai une partie du hardware :hammer_and_wrench:   
Mais il est parfois cher :money_with_wings: et long :calendar: de faire parvenir du matériel au Nicaragua :nicaragua: (où je vis).

<!--[en]-->
⟶ I already have part of the hardware :hammer_and_wrench:.   
However, it is sometimes expensive :money_with_wings: and slow :calendar: to get hardware shipped to Nicaragua :nicaragua: (where I live).

<!--[fr]-->
:eye: [**Voir l'avancement de la configuration de MAEL Scan Pi V3**](https://github.com/Yobeco/MAEL_Scan_Pi/blob/main/00-DVLP_plan_MAEL_Scan_pi_V3.md)  

<!--[en]-->
:eye: [**See the progress of the MAEL Scan Pi V3 configuration**](https://github.com/Yobeco/MAEL_Scan_Pi/blob/main/00-DVLP_plan_MAEL_Scan_pi_V3.md)  

<!--[fr]-->
1. Configuration de l'OS
2. Utilitaires CLI
3. Installation des modules...

<!--[en]-->
1. OS configuration  
2. CLI utilities  
3. Module installation...

<!--[fr]-->
### :mechanical_arm: Besoin d'un spécialiste en création de PCB :ring_buoy:

<!--[en]-->
### :mechanical_arm: Need a PCB design specialist :ring_buoy:

<!--[fr]-->
Les connexions internes ont besoin d'un petit [connecteur (PCB)](Connexions_GPIO_Shim.md) qu'il faudrait fabriquer sur mesure.

<!--[en]-->
The internal connections require a small custom-made [connector (PCB)](Connexions_GPIO_Shim.md).

<!--[common]-->
---

<!--[fr]-->
## E- Fonctionnalités à développer :rocket:

<!--[en]-->
## E- Features to be developed :rocket:

<!--[fr]-->
Les mêmes que pour **MAEL Scan**, mais à développer en Python <img src="https://cdn.simpleicons.org/python/FFFF" width="24" height="24" style="vertical-align: middle;" /> sur Raspberry.

<!--[en]-->
Same as for **MAEL Scan**, but to be developed in Python <img src="https://cdn.simpleicons.org/python/FFFF" width="24" height="24" style="vertical-align: middle;" /> on Raspberry Pi.

<!--[fr]-->
### :+1: Proposez votre aide pour developper _MAEL Scan Pi_

<!--[en]-->
### :+1: Offer your help to develop _MAEL Scan Pi_

<!--[fr]-->
**Peut-être qu'un FabLab :nut_and_bolt: pourrait participer ? :grin:**

<!--[en]-->
**Maybe a FabLab :nut_and_bolt: could participate? :grin:**

<!--[common]-->
---

<!--[fr]-->
## F- Participez au projet MAEL :open_hands:

<!--[en]-->
## F- Take part in the MAEL project :open_hands:

<!--[fr]-->
:ring_buoy: Pour **obtenir des informations** concernant le fonctionnement de **MAEL Scan Pi** :+1: écrivez-moi ici :

<!--[en]-->
:ring_buoy: To **get information** about how **MAEL Scan Pi** works :+1:, write to me here:

<!--[common]-->
### :mailbox_with_mail: ***[mael@lvh.edu.ni](mailto:mael@lvh.edu.ni)***

<!--[fr]-->
### :star2: Contributeurs

<!--[en]-->
### :star2: Contributors

<!--[fr]-->
Un grand merci à toutes les personnes qui vont contribuer à ce projet !

<!--[en]-->
A big thank you to everyone who will contribute to this project!

<!--[fr]-->
| Avatar | Nom                | GitHub                          | Rôle                     |
|--------|--------------------|---------------------------------|--------------------------|
| [<img src="https://github.com/YoBeco.png" width="50" style="border-radius: 50%;">](https://github.com/YoBeco) | Bécognée Yonnel | [@Yobeco](https://github.com/Yobeco)   | Mainteneur                     |
| [<img src="https://github.com/Nail-yk.png" width="50" style="border-radius: 50%;">](https://github.com/Nail-yk) | Padawan | [@Nail-yk](https://github.com/Nail-yk) | Traduction de la documentation |
| ... | ... | ... | Développeur (euse) |
| ... | ... | ... | Bricoleur (euse) |

<!--[en]-->
| Avatar | Name               | GitHub                          | Role                     |
|--------|--------------------|---------------------------------|--------------------------|
| [<img src="https://github.com/YoBeco.png" width="50" style="border-radius: 50%;">](https://github.com/YoBeco) | Bécognée Yonnel | [@Yobeco](https://github.com/Yobeco)   | Maintainer                |
| [<img src="https://github.com/Nail-yk.png" width="50" style="border-radius: 50%;">](https://github.com/Nail-yk) | Padawan | [@Nail-yk](https://github.com/Nail-yk) | Documentation translation |
| ... | ... | ... | Developer |
| ... | ... | ... | Maker |

<!--[common]-->
---

<!--[fr]-->
## G- Installation :arrow_heading_down:

<!--[en]-->
## G- Installation :arrow_heading_down:

<!--[fr]-->
Mon code source du prototype V2 est encore trop désordonné pour que j'ose le mettre sur le dépôt. :disappointed:   
En fait, je passe directement à la version 3...

<!--[en]-->
The source code of the V2 prototype is still too messy for me to dare publish it in the repository. :disappointed:   
In fact, I am moving directly to version 3...
