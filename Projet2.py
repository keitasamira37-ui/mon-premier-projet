import json
import os

CUR_DIR =  os.path.dirname(__file__)
LISTE_PATH = r"C:\Users\HP\Documents\python\listecourse.json"

menu = [
    "1 : Ajouter un produit",
    "2 : Vendre un produit",
    "3 : Modifier la quantité d'un produit",
    "4 : Voir la liste des produits ",
    "5 : Quitter"
]

menu_choices = ["1","2","3","4","5"]


def charger_liste(path):
    if not os.path.exists(path):
        # créer le fichier avec une liste vide
        with open(path, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

LISTE = charger_liste(LISTE_PATH)

def sauvegarde():
    with open(LISTE_PATH,"w",encoding= "utf-8") as f:
        json.dump(LISTE ,f,indent=4)
    

def Ajout():
    nom = input("Le nom du produit ?? : ")
    qte = int(input("La quantité du produit ?? : "))
    prix = int(input("Le prix du produit ?? : "))
    LISTE.append({"Produit" : nom, "Quantité": qte, "Prix " : prix})
    sauvegarde()

def vente():
    for produits in LISTE :
        prodven = input("Le nom du produit que vous voulez vendre : ")
        if (prodven == produits["Produit"]) == False:
            print("Produit non repertorié")
            prodven = input("Le nom du produit que vous voulez vendre : ")
        qteven = int(input("La quantité du produit que vous voulez vendre : "))
        if prodven == produits["Produit"] and qteven <= produits["Quantité"]:
            produits["Quantité"] = produits["Quantité"] - qteven
            achat = qteven * produits["Prix"] 
        elif (qteven <= produits["Quantité"]) == False :
            print("Pas assez de produit en stock")
    sauvegarde()
    return print(f"L'achat revient à {achat}")

def Modification():
    mod = input("Le nom du produit dont vous voulez modifier la quantité ?? : ")
    new_qte = int(input("La nouvelle quantité du produit ?? : "))
    for produits in LISTE :
        if mod not in produits["Produit"] :
            print("Produit non repertorié")
        else :
            produits["Quantité"] = new_qte
    sauvegarde()

for prod in LISTE :
        if prod["Quantité"] <= 10 :
            print(f"ALERTE : le stock du produit {prod["Produit"]} est faible")

while True:
    user_choice = ""
    while user_choice not in menu_choices:
        print("-"*30)
        print("\n".join(menu))
        user_choice = input("Choisissez une option : ")

    if user_choice == "1":
        Ajout()
    elif user_choice == "2":
        vente()
    elif user_choice == "3":
        Modification()
    elif user_choice == "4":
        print(LISTE)
    else :
        print("AUrevoir")
        break

    for prod in LISTE :
        if prod["Quantité"] <= 10 :
            print(f"ALERTE : le stock du produit {prod["Produit"]} est faible")

