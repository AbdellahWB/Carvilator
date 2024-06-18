      Carvilator - File carving script 
        Copyright© @Abdellah WAHBI                         
# Carvilator 1.0

Carvilator est un script de récupération de fichiers (file carving) à partir d'un disque ou d'une image disque. Il supporte plusieurs types de fichiers, dont les images JPEG, les documents PDF, les fichiers MP3, et bien d'autres.

## Fonctionnalités

- Récupération de fichiers JPEG, PDF, DOCX, XLSX, PPTX, MP3, MP4, PNG et GIF à partir de disques ou d'images disques.
- Utilisation d'une barre de progression pour afficher l'état de la récupération.
- Sauvegarde automatique des fichiers récupérés dans un dossier spécifié.

## Installation

Pour utiliser Carvilator, suivez les étapes suivantes :

1. **Cloner le dépôt GitHub :**

   - git clone https://github.com/votre-utilisateur/carvilator.git
   - cd carvilator
   - python3 carvilator.py
  
  Installer les dépendances :

Assurez-vous d'avoir tqdm installé. Vous pouvez l'installer via pip :

   - pip install tqdm
Utilisation
Carvilator nécessite deux arguments : le chemin vers le disque ou l'image disque à analyser et le dossier où sauvegarder les fichiers récupérés.

Exemple d'utilisation :

   - python carvilator.py -i /path/to/disk/image -o /path/to/output/folder
Options
   -i, --input : Chemin du disque ou de l'image disque à analyser (obligatoire).
   -o, --output : Dossier où sauvegarder les fichiers récupérés (obligatoire).
   -v, --version : Affiche la version de Carvilator.
Exemple

   - python carvilator.py -i /dev/sdX -o /home/user/recovered_files
     
Ce script analysera le disque /dev/sdX et sauvegardera les fichiers récupérés dans le dossier /home/user/recovered_files.

Remerciements
Merci d'utiliser Carvilator pour vos besoins de récupération de fichiers. Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.

![image](https://github.com/AbdellahWB/Carvilator/assets/99265207/ab32cbb3-7b5f-4fb0-ba54-3d673ad42b80)
