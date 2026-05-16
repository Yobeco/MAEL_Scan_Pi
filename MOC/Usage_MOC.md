# Comment installer et utiliser MOC

## 1- Installation sur Trixie lite

```bash
sudo apt update
sudo apt upgrade
sudo apt install moc


# Si erreur : "Can't load plugin libmp3_decoder: file not found"
# Trouver la position de la bibliothèque :
dpkg -L moc | grep libmp3_decoder
--> /usr/lib/arm-linux-gnueabihf/moc/decoder_plugins/libmp3_decoder.so

# Vérifier les dépendences
ldd /usr/lib/arm-linux-gnueabihf/moc/decoder_plugins/libmp3_decoder.so
-->
/usr/lib/arm-linux-gnueabihf/libarmmem-${PLATFORM}.so => /usr/lib/arm-linux-gnueabihf/libarmmem-v6l.so (0xb6f90000)
	libmad.so.0 => /lib/arm-linux-gnueabihf/libmad.so.0 (0xb6f79000)
	libid3tag.so.0 => /lib/arm-linux-gnueabihf/libid3tag.so.0 (0xb6fd6000)
	libc.so.6 => /lib/arm-linux-gnueabihf/libc.so.6 (0xb6dd0000)
	/lib/ld-linux-armhf.so.3 (0xb6fb0000)
	libz.so.1 => /lib/arm-linux-gnueabihf/libz.so.1 (0xb6db8000)
	
# Vérifier les permissions du fichier

ls -la /usr/lib/arm-linux-gnueabihf/moc/decoder_plugins/libmp3_decoder.so
# Le résultat doit montrer les permissions -rw-r--r--. Si les droits de lecture (r) manquent pour l'utilisateur ou le groupe, c'est la cause du problème.
	
# Simuler le chargement de la bibliothèque avec Python pour dignostiquer le problème
python3 -c "import ctypes; ctypes.CDLL('/usr/lib/arm-linux-gnueabihf/moc/decoder_plugins/libmp3_decoder.so')"

--> Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import ctypes; ctypes.CDLL('/usr/lib/arm-linux-gnueabihf/moc/decoder_plugins/libmp3_decoder.so')
                   ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/ctypes/__init__.py", line 390, in __init__
    self._handle = _dlopen(self._name, mode)
                   ~~~~~~~^^^^^^^^^^^^^^^^^^
OSError: libmad.so.0: cannot enable executable stack as shared object requires: Invalid argument

# Cette erreur de sécurité indique que la bibliothèque libmad a été compilée avec une pile exécutable (execstack), une pratique désuète que les noyaux Linux modernes refusent pour des raisons de sécurité.
# Pour corriger cela, modifier l'attribut de la pile exécutable dans le binaire de libmad. 

sudo apt install patchelf
sudo patchelf --clear-execstack /lib/arm-linux-gnueabihf/libmad.so.0

mocp -x
mocp
```

## 2- Commandes de base

### a- Lancer le serveur en arrière-plan

```bash
mocp -S
```

### b- Vider la playlist, ajouter le fichier et lire sans interface.

```bash
mocp -l path/to/your/file.mp3
```

### c- Avancer ou reculer de *x* secondes

```bash
mocp -k 5
mocp -k -5
```

### d- Bascule Pause / Play

```bash
mocp -G
```

