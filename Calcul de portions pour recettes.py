"""Calcul de portions pour recettes
   Permet de recalculer toute une recette en indiquant
   le nombre d'ingrédients
   la quantité de chacun
   leur unité de lecture
   le nombre de personnes de la recette initiale
   le nombre de personnes souhaitées"""

import json


def produit_en_croix(quantite, nb_personnes, nb_personnes_cible):
    return quantite * int(nb_personnes_cible) / int(nb_personnes) #définition du produit en croix permettant le calcul des nouvelles quantités


def creer_recette():
    recette = {}
    recette["ingredients"] = {} #dictionnaire stockant les ingrédients
    nb_personnes = 0 #définition de la variable du nombre de personnes
    recette["nom"] = input("Nom de la recette : ") #input du nom de la recette 
    nb_ingredients = input("Combien d'ingredients ? ") #input du nombre d'ingrédients déterminant le nombre de boucles par la suite

    for i in range(int(nb_ingredients)): #
        ingredient = {} #chaque boucle va définir un ingrédient et ses composants

        nom = input("Nom de l'ingrédient ? ")
        quantite = input("Quantité ? ")
        unite = input("Unité ? ")
        print()

        ingredient["quantite"] = float(quantite) #condition permettant de ne pas mettre d'unité de mesure si aucune n'est spécifiée (comme pour les oeufs par exemple)
        if unite != "":
            ingredient["unite"] = unite

        recette["ingredients"][nom] = ingredient

    recette["nombre de personnes"] = int(input("Pour combien de personnes ? ")) #définition du nombre de personnes de la recette initiale

    with open(recette["nom"] + ".json", "w") as f: #inscription de la totalité de la recette dans un fichier .json à part
        json.dump(recette, f)


def charger_recette(nom): #renvoi à la fonction permettant de charger la recette avec le nom précédement donné
    recette = {}

    with open(nom + ".json", "r") as f:
        recette = json.load(f)

    nb_personnes = input("Nombre de personnes souhaitées ? ") #demande du nombre de personnes pour le calcul des nouvelles quantités

    for ingredient in recette["ingredients"]: #démarrage de la boucle appliquant la fonction produit en croix pour chaque élément de la recette sauf l'unité de mesure
        recette["ingredients"][ingredient]["quantite"] = produit_en_croix(
            recette["ingredients"][ingredient]["quantite"], recette["nombre de personnes"], nb_personnes)

    recette["nombre de personnes"] = int(nb_personnes)

    with open(recette["nom"] + " pour " + str(nb_personnes) + " personne" + ("s" if int(nb_personnes) > 1 else "") + ".json",
              "w") as f:
        json.dump(recette, f) #rajoute un "s" à la fin du mot "personne" s'il y en a plus de 1 dans la recette

    print(recette)


def main(): #définit la fonction du menu permettant de lancer les diverses actions
    print("1 - Créer une recette")
    print("2 - Calcul de nouvelles quantités")

    input_utilisateur = input("Que voulez-vous faire ? ")

    if input_utilisateur == "1":
        creer_recette()
    
    elif input_utilisateur == "2":
        nom = input("Nom de la recette ? ")
        charger_recette(nom)


if __name__ == "__main__":
    main()