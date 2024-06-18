import os
import argparse
from tqdm import tqdm # Pour afficher une barre de progression pendant la récupération des fichiers

ASCII_ART = r"""

 ▄████▄  ▄▄▄      ██▀███  ██▒   █▓██▓██▓   ▄▄▄    ▄▄▄█████▓▒█████  ██▀███  
▒██▀ ▀█ ▒████▄   ▓██ ▒ ██▓██░   █▓██▓██▒  ▒████▄  ▓  ██▒ ▓▒██▒  ██▓██ ▒ ██▒
▒▓█    ▄▒██  ▀█▄ ▓██ ░▄█ ▒▓██  █▒▒██▒██░  ▒██  ▀█▄▒ ▓██░ ▒▒██░  ██▓██ ░▄█ ▒
▒▓▓▄ ▄██░██▄▄▄▄██▒██▀▀█▄   ▒██ █░░██▒██░  ░██▄▄▄▄█░ ▓██▓ ░▒██   ██▒██▀▀█▄  
▒ ▓███▀ ░▓█   ▓██░██▓ ▒██▒  ▒▀█░ ░██░██████▓█   ▓██▒▒██▒ ░░ ████▓▒░██▓ ▒██▒
░ ░▒ ▒  ░▒▒   ▓▒█░ ▒▓ ░▒▓░  ░ ▐░ ░▓ ░ ▒░▓  ▒▒   ▓▒█░▒ ░░  ░ ▒░▒░▒░░ ▒▓ ░▒▓░
  ░  ▒    ▒   ▒▒ ░ ░▒ ░ ▒░  ░ ░░  ▒ ░ ░ ▒  ░▒   ▒▒ ░  ░     ░ ▒ ▒░  ░▒ ░ ▒░
░         ░   ▒    ░░   ░     ░░  ▒ ░ ░ ░   ░   ▒   ░     ░ ░ ░ ▒   ░░   ░ 
░ ░           ░  ░  ░          ░  ░     ░  ░    ░  ░          ░ ░    ░     
░                             ░                                            
                           Copyright© @Abdellah WAHBI               
"""
VERSION = "\033[1;33m alpha 1.0 \033[0m"
# Fonction pour récupérer les fichiers à partir d'un disque ou d'une image disque
def recover_files(drive_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Signatures de début et de fin de différents types de fichiers
    file_signatures = {
        b'\xff\xd8\xff': {'extension': 'jpg', 'end': b'\xff\xd9'},  # JPEG
        b'\x25\x50\x44\x46': {'extension': 'pdf', 'end': b'%%EOF'},  # PDF
        b'\x50\x4b\x03\x04': {'extension': 'docx', 'end': None},  # Word
        b'\x50\x4b\x03\x04': {'extension': 'xlsx', 'end': None},  # Excel
        b'\x50\x4b\x03\x04': {'extension': 'pptx', 'end': None},  # PowerPoint
        b'\x49\x44\x33': {'extension': 'mp3', 'end': None},  # MP3 (ID3v2)
        b'\x00\x00\x00\x18': {'extension': 'mp4', 'end': None},  # MP4
        b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a': {'extension': 'png', 'end': b'\x49\x45\x4e\x44\xae\x42\x60\x82'},  # PNG
        b'\x47\x49\x46\x38': {'extension': 'gif', 'end': b'\x00\x3b'},  # GIF
    }

    buffer_size = 1024 * 1024  # Lire par blocs de 1 Mo
    files_found = 0

    try:
        statvfs = os.statvfs(drive_path)
        total_blocks = statvfs.f_blocks * statvfs.f_frsize
        with open(drive_path, 'rb') as drive: # Initialisation de la barre de progression
            progress_bar = tqdm(total=total_blocks, unit='B', unit_scale=True, desc=f"\033[1;34mProgression: \033[0m")
            buffer = b''
            while True:
                data = drive.read(buffer_size)
                if not data:
                    break
                buffer += data
# Parcours des signatures pour trouver les fichiers
                for signature, info in file_signatures.items():
                    extension = info['extension']
                    start_index = 0
                    while True:
                        start_index = buffer.find(signature, start_index)
                        if start_index == -1:
                            break
                        if info['end']:
                            end_index = buffer.find(info['end'], start_index) + len(info['end'])
                            if end_index == len(info['end']) - 1:
                                start_index += len(signature)
                                continue
                        else:
                            end_index = len(buffer)
                        file_content = buffer[start_index:end_index]
                        file_path = os.path.join(output_folder, f"recovered_{files_found}.{extension}")
                        with open(file_path, 'wb') as file:
                            file.write(file_content)
                        files_found += 1
                        start_index = end_index

                buffer = buffer[-len(signature):] # Garder seulement la fin du buffer pour éviter les troncatures
                progress_bar.update(len(data))  # Mettre à jour la barre de progression avec la quantité lue

        print(f"\033[1;32mTotal de fichiers récupérés : {files_found}\033[0m")

    except IOError as error:
        print(f"\033[1;31mErreur lors de la lecture du disque : {error}\033[0m")
# Fonction principale
def main():   # Parser pour les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Carvilator 1.0 - Récupération de fichiers à partir d'un disque ou d'une image disque")
    parser.add_argument('-i', '--input', required=True, help="Chemin du disque ou de l'image disque à analyser")
    parser.add_argument('-o', '--output', required=True, help="Dossier où sauvegarder les fichiers récupérés")
    parser.add_argument('-v', '--version', action='version', version=f'Carvilator {VERSION}')

    args = parser.parse_args()

    print(ASCII_ART)
    print(f"Version: {VERSION}")
 # Appel de la fonction pour récupérer les fichiers
    recover_files(args.input, args.output)

if __name__ == '__main__':
    main()
