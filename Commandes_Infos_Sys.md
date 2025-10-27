# Commandes pour info. système

- Date du système : `date`
- Temps depuis le dernier allumage : `uptime`
- Informations sur les utilisateurs : `w`
- Informations sur le CPU `more /proc/cpuinfo`
- Informations sur la mémoire : `more /proc/meminfo`
- Informations sur la mémoire diponible : `free -h`
- Informations sur les systèmes de fichiers : `df -h`
- Taille d'un fichier ou dosier : `du -sh`

Voici plusieurs commandes utiles pour obtenir des informations logicielles et matérielles sur ton Raspberry Pi. Ces commandes te permettront d’avoir une vue d’ensemble de ton système :

------

### **1. Informations matérielles (Hardware)**

#### **Modèle du Raspberry Pi**

```
cat /proc/device-tree/model
```

ou

```
cat /sys/firmware/devicetree/base/model
```

#### **Architecture du processeur**

```
uname -m
```

#### **Informations détaillées sur le CPU**

```
lscpu
```

#### **Température du CPU**

```
vcgencmd measure_temp
```

#### **Informations sur la mémoire (RAM)**

```
free -h
```

#### **Espace disque**

```
df -h
```

#### **Liste des périphériques USB connectés**

```
lsusb
```

#### **Liste des périphériques PCI (si applicable)**

```
lspci
```

#### **Informations sur le GPU**

```
vcgencmd get_mem arm && vcgencmd get_mem gpu
```

------

### **2. Informations logicielles (Software)**

#### **Version du noyau Linux**

```
uname -a
```

#### **Version de Raspberry Pi OS**

```
cat /etc/os-release
```

#### **Liste des paquets installés (apt)**

```
apt list --installed | grep -i raspberrypi
```

#### **Version de Python installée**

```
python3 --version
```

#### **Informations sur le firmware**

```
vcgencmd version
```

#### **Liste des services actifs**

```
systemctl list-units --type=service --state=running
```

------

### **3. Informations réseau**

#### **Adresse IP locale**

```
hostname -I
```

#### **Informations sur les interfaces réseau**

```
ifconfig
```

ou

```
ip a
```

------

### **4. Informations système générales**

#### **Uptime (temps depuis le dernier démarrage)**

```
uptime
```

#### **Informations sur le matériel et le système d’exploitation**

```
sudo lshw -short
```

*(Nécessite l’installation de `lshw` : `sudo apt install lshw`)*

------

### **5. Informations sur les périphériques connectés**

#### **Liste des disques et partitions**

```
lsblk
```

#### **Liste des périphériques bloc (disques, cartes SD, etc.)**

```
sudo fdisk -l
```

------

### **6. Informations sur le processeur et la charge système**

#### **Utilisation du CPU et des processus**

```
top
```

*(Appuie sur `q` pour quitter)*

------

Tu peux exécuter ces commandes directement dans le terminal de ton Raspberry Pi. Si tu veux des détails sur une commande spécifique ou si tu cherches une information précise, n’hésite pas à me le dire !
