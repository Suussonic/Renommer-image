import os
import random
import string

# Extensions d'images prises en charge
EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp",
    ".webp", ".tiff", ".tif", ".ico"
}

# Dossier actuel
DOSSIER = os.getcwd()

def nom_aleatoire(longueur=10):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=longueur))

for fichier in os.listdir(DOSSIER):
    ancien_chemin = os.path.join(DOSSIER, fichier)

    # Vérifie qu'il s'agit bien d'un fichier image
    if not os.path.isfile(ancien_chemin):
        continue

    extension = os.path.splitext(fichier)[1].lower()

    if extension not in EXTENSIONS:
        continue

    # Génère un nom unique
    while True:
        nouveau_nom = nom_aleatoire(10) + extension
        nouveau_chemin = os.path.join(DOSSIER, nouveau_nom)

        if not os.path.exists(nouveau_chemin):
            break

    os.rename(ancien_chemin, nouveau_chemin)

    print(f"{fichier} -> {nouveau_nom}")

print("\nTerminé !")