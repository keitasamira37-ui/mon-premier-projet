import json
import os

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = r"C:\Users\HP\Documents\python\contact.json" #os.path.join(CUR_DIR, "main.json")

menu = [
    "1 : Ajouter un contact",
    "2 : Afficher les contacts",
    "3 : Supprimer un contact",
    "4 : Rechercher un contact",
    "5 : Quitter"
]

Menu_choices = ["1","2","3","4","5"]

# Charger la liste
if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        try:
            LISTE = json.load(f)
        except json.JSONDecodeError:
            LISTE = []
else:
    LISTE = []

def sauvegarde():
    """Sauvegarde automatique dans le fichier JSON"""
    with open(LISTE_PATH, "w") as f:
        json.dump(LISTE, f, indent=4)

def Ajout():
    nom = input("Nom : ")
    tel = input("Téléphone : ")
    email = input("Email : ")
    LISTE.append({"nom": nom, "telephone": tel, "email": email})
    sauvegarde()  # sauvegarde automatique

def affiche():
    if not LISTE:
        print("Aucun contact enregistré.")
    else:
        for contact in LISTE:
            print(contact["nom"], contact["telephone"], contact["email"])

def recherche():
    search = input("Nom du contact à rechercher : ")
    trouve = False
    for contact in LISTE:
        if contact["nom"].lower() == search.lower():
            print(contact)
            trouve = True
    if not trouve:
        print("Contact introuvable.")

def supprime():
    search = input("Nom du contact à supprimer : ")
    for contact in LISTE:
        if contact["nom"].lower() == search.lower():
            LISTE.remove(contact)
            sauvegarde()  # sauvegarde automatique
            print("Contact supprimé.")
            break
    else:
        print("Contact introuvable.")

# Boucle principale
while True:
    user_choice = ""
    while user_choice not in Menu_choices:
        print("\n".join(menu))
        user_choice = input("Choisissez une option : ")

    if user_choice == "1":
        Ajout()
    elif user_choice == "2":
        affiche()
    elif user_choice == "3":
        supprime()
    elif user_choice == "4":
        recherche()
    elif user_choice == "5":
        print("Au revoir !")
        break
