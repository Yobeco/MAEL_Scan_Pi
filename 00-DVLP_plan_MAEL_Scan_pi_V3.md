# Développement de MAEL Scan Pi

## I- Installation de Pi OS lite

### 1- Installer Pi OS 64 bit sur le raspberry pi 4 - 8Go

Créer une SD bootable avec "imager" sous Ubuntu

### 	a- Installer imager

```bash
sudo apt update
sudo apt upgrade
sudo apt install imager
```

### 	b- Installer Pi OS sur la SD

Configuration :

1. Configurer la connexion Wifi dés la création de l'image. _(Pas sûr que ça fonctionne...)_
2. Configurer le SSH _(Pas sûr que ça fonctionne non plus. Lire la carte SD depuis Ubuntu. et ajouter un fichier texte vide nommé `ssh` dans le dossier "boot" à la racine de la carte SD.)_

### 2- Démarrage et configurations de base de Pi OS

#### 	a- Configurer une ouverture automatique de la session par défaut. 

Avec un clavier et un écran, lancer `raspi-config > 1 System Options > S6 Auto Login`

#### 	b- **Configuration du Wifi**

1. Configurer le wifi depuis `raspi-config`.
2. Si encore ne fonctionne pas : configurer **NetworkManager** à la main : 

```bash
sudo nmcli connection delete "preconfigured"
sudo nmcli dev wifi connect "ton_ssid" password "ton_mot_de_passe"
```

#### 	c- Actualisation du système

```bash
sudo apt update
sudo apt upgrade
```
#### 	d- [Voir les informations du système](Commandes_Infos_Sys.md)

```bash
cat /etc/os-release
```

Plus joli, installer et lancer `neofech`

```bash
sudo apt install git
git clone https://github.com/dylanaraps/neofetch.git
cd neofetch
sudo make install
neofetch
neofetch --ascii_distro raspberry-pi
```

#### 	e- Activation du SSH (Si _imager_ a échoué)

_1- Activer le serveur SSH sur le RPi_

`raspi-config > 3 Interface Options > I1 SSH`

_2- Demander l'IP du RPi_

```bash
ip a show wlan0
ou
hostname -I
```

_3- Se connecter depuis l'ordinateur contrôleur Ubuntu (en utilisant l'IP du RPi) :_

```bash
ssh mael@192.168.1.21
```

Pour sortir de la connexion SSH : `exit`

Pour éteindre le RPi : `sudo poweroff`

### 3- Configurations d'optimisation

####		a- Activer la Zram pour augmenter virtuellement la RAM

Sous Pi OS **Trixie**, `rpi-swap` est présent et activé par défaut.

**`rpi-swap`** utilise Zram (comme dépendance) pour la swap, ce qui :

- Réduit les accès à la carte SD (prolongeant sa durée de vie).
- Améliore les performances en évitant les lenteurs liées au swap sur SD.
- Gère automatiquement la taille du swap et la compression (algorithme LZ4 par défaut, optimisé pour les Raspberry Pi).

**Aucune configuration supplémentaire** n’est nécessaire pour la plupart des usages.

```bash
mael@MAELpi3:~ $ sudo systemctl list-units --type swap
  UNIT           LOAD   ACTIVE SUB    DESCRIPTION                             
  dev-zram0.swap loaded active active rpi-swap managed swap device (zram+file)

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

1 loaded units listed. Pass --all to see loaded but inactive units, too.
To show all installed unit files use 'systemctl list-unit-files'.
----------------------------------------------------------------------------
mael@MAELpi3:~ $ zramctl
NAME       ALGORITHM DISKSIZE DATA COMPR TOTAL STREAMS MOUNTPOINT
/dev/zram0 zstd          416M   4K   69B   20K       4 [SWAP]
----------------------------------------------------------------------------
mael@MAELpi3:~ $ swapon --show
NAME       TYPE      SIZE USED PRIO
/dev/zram0 partition 416M   0B  100

```

####		b- Installer LOG2RAM pour économiser la SD

Seulement pour des services très gourmands en logs (ex : serveur web, base de données : des applications très verbeuses)

--> Donc pas très utile pour MAEL Scan Pi...

## II- Installation du HAT de Hauts parleurs (+ Jack)

### 1- [Configuration du Hat](https://spotpear.com/wiki/Raspberry-Pi-GPIO-Audio-amplification-PWM-Sound-Card-Speaker-Buzzer.html)

#### a- Éditer le fichier de configuration :
```bash
sudo nano /boot/firmware/config.txt
```

#### b- Ajouter cette ligne
```bash
dtoverlay=audremap,pins_18_19
```
#### c- Enregistrer la configuration :

#### Sauvegarder : `Ctrl + O` /  `Enter`

#### Quitter : `Ctrl + x`, 

#### Relancer le RPi : `sudo reboot`

#### d- Activer la sortie audio :
```bash
sudo raspi-config > 1 System Options > S2 Audio > 0 bcm2835 Headphones
```

#### e- Redémarrer encore
```bash
sudo reboot
```

### 2- Lancer la lecture d'un son

#### a- Utiliser `speaker-test` d'ALSA

```bash
# Génère un son sinusoïdal à 440 Hz (la note "La") pendant 1s
timeout 1s speaker-test -t sine -f 440  
```

#### b- Déposer un fichier son sur le RPi avec SSH

1- Savoir son chemin courant :

```bash
# (print working directory) affiche le chemin du répertoire courant.
pwd
```

2- Savoir un chemin absolu :

```bash
realpath mon_fichier.txt
```

3- Scénario d'utilisation de **scp** : `scp` `source` `destination`

4- Lancer une copie :

```bash
yonnel@YoDesktop:/chemin/complet$ scp test2b.wav mael@192.168.1.21:/home/maelscp test.mp3 mael@192.168.1.21:/home/mael
```

5- Déposer un dossier entier :

```bash
scp -r /home/yonnel/dossier mael@192.168.1.21:/home/mael
```

#### b- Jouer le son

**Avec "_aplay_" (Seulement des wav)**

```bash
mael@MAELpi3:~ $ aplay test.wav
```
> [!WARNING]
> **Son médiocre... :face_with_head_bandage: Il faut trouver une meilleure solution. Et pas chère si possible...**  
> [Micro+](https://raspiaudio.com/product/mic/) --> Bien mais cher :confused:  
> [ReSpeaker 2-Mic Pi HAT V1.0](https://docs.keyestudio.com/projects/KS0314/en/latest/docs/KS0314.html) --> Pas cher, mais alim externe + ajout de HP... :face_with_head_bandage:   

## III- [Fonctions de lecture audio MOC](http://moc.daper.net/node/87)

[Évaluation par Mistral](https://chat.mistral.ai/chat/cf412c22-5cb5-41be-a95a-3474314c53d8)

[Documentation officielle (Man page)](MOC/Commandes_MOC.md)

### 1- Lecture d'un fichier sans l'interface

```bash
# Lancer le serveur (sans interface)
mocp -S
# Jouer le fichier une fois
mocp -c && mocp -a test2.wav && mocp -p
```

| Argument                                | Fonction                                                     |
| --------------------------------------- | ------------------------------------------------------------ |
| [-S](https://www.mankier.com/1/mocp#-S) | Lancer uniquement le serveur.                                |
| [-c](https://www.mankier.com/1/mocp#-c) | Effacer la playlist.                                         |
| [-a](https://www.mankier.com/1/mocp#-a) | Ajouter les fichiers, répertoires et listes de lecture indiqués. **Ne lance pas l'interface**. |
| [-p](https://www.mankier.com/1/mocp#-p) | Commencer la lecture à partir du premier élément de la liste de lecture. |

### 2- Contrôle de la lecture

| Argument                                         | Fonction                                                     |
| ------------------------------------------------ | ------------------------------------------------------------ |
| [-G](https://www.mankier.com/1/mocp#-G) (Toggle) | Basculer entre lecture et pause.                             |
| [-k](https://www.mankier.com/1/mocp#-k) [+/-]*N* | Avancer (+) ou reculez (-) de *N* secondes dans le fichier en cours de lecture. |
| [-v](https://www.mankier.com/1/mocp#-v) [+/-]*N* | Régler le volume du mixeur. (**[-v](https://www.mankier.com/1/mocp#-v) +10**, **[-v](https://www.mankier.com/1/mocp#-v) -10**). |

Ces commandes seront lancées depuis python lui-même contrôlé par des boutons capacitifs

### 3- SOX pour la lecture lente ?



## IV- Utilisation du Hat déporté

1. Connecter les GPIO avec des câbles souples (Connecteur SHIM ?)

## V- Connexion à gTTS

1. Configuration (vitesse de lecture ?)
2. Faire lire un texte généré par gTTS

## VI- Ajout des boutons capacitifs (MPR121)

1. Configuration
2. Associer les fonctions de lecture

## VII- Ajout du lecteur de codes QR (GM861S-LED)

1. Configuration
2. Essayer plusieurs codes QR utf-8
3. Faire lire par le contenu par GTTS + MOC

## VIII- Ajout d l'écran

1. Configuration
2. Affichage du logo MAEL en couleurs
3. Affichage de texte
4. Taille du texte en fonction du nombre de caractères

## IX- Implémentation du décryptage

## X- Implémentation du "parser" de balises

## XI- Implémentation des modes

## XII- Implémentation de la persistance des fichiers

## XIII- Révision du flux complet

## IX- Créer une image de la SD quand une version est satisfaisante !

Mettre la carte SD sur un lecteur puis utiliser "Disques" (Utilitaire par défaut d'Ubuntu)
ou dd ?
