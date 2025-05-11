import subprocess
import os

BASE_DIR = os.path.join(os.path.dirname(__file__))

def convert_with_kcc(folder_name, output_dir=None, output_format="CBZ"):
    """
    Convertit un dossier contenant des images en CBZ avec KCC (kcc-c2e) pour Kobo Libra Colour.
    
    :param folder_name: Nom du dossier (dans BASE_DIR) contenant les images à convertir
    :param output_dir: Dossier de sortie (facultatif)
    :param output_format: Format de sortie (CBZ, EPUB, MOBI, PDF, etc.)
    """
    folder_path = os.path.join(BASE_DIR, folder_name)
    print(f"📂 Dossier à convertir : {folder_path}")
    if not os.path.isdir(folder_path):
        raise ValueError(f"Le dossier spécifié n'existe pas : {folder_path}")

    cmd = [
        "python", "kcc-7.4.1/kcc-c2e.py",
        "-p", "KoLC",
        "-w",
        "-u",
        "--forcecolor",
        "-f", output_format,
        folder_path
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Conversion terminée avec succès.")
    except subprocess.CalledProcessError as e:
        print("❌ Erreur pendant la conversion :", e)

# Exemple d'utilisation
if __name__ == "__main__":
    folder = input("Nom du dossier à convertir (dans 'downloads') : ").strip()
    convert_with_kcc(folder)
