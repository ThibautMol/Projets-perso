"""Calcul de portions pour recettes
   Permet de recalculer toute une recette en indiquant
   le nombre d'ingrédients
   la quantité de chacun
   leur unité de lecture
   le nombre de personnes de la recette initiale
   le nombre de personnes souhaitées"""

import json


def produit_en_croix(quantite, nb_personnes, nb_personnes_cible):
    return quantite * int(nb_personnes_cible) / int(nb_personnes)


def creer_recette():
    recette = {}
    recette["ingredients"] = {}
    nb_personnes = 0
    recette["nom"] = input("Nom de la recette : ")
    nb_ingredients = input("Combien d'ingredients ? ")

    for i in range(int(nb_ingredients)):
        ingredient = {}

        nom = input("Nom de l'ingrédient ? ")
        quantite = input("Quantité ? ")
        unite = input("Unité ? ")
        print()

        ingredient["quantite"] = float(quantite)
        if unite != "":
            ingredient["unite"] = unite

        recette["ingredients"][nom] = ingredient

    recette["nombre de personnes"] = int(input("Pour combien de personnes ? "))

    with open(recette["nom"] + ".json", "w") as f:
        json.dump(recette, f)


def charger_recette(nom):
    recette = {}

    with open(nom + ".json", "r") as f:
        recette = json.load(f)

    nb_pers = input("Nombre de personnes souhaitées ? ")

    for ingredient in recette["ingredients"]:
        recette["ingredients"][ingredient]["quantite"] = produit_en_croix(
            recette["ingredients"][ingredient]["quantite"], recette["nombre de personnes"], nb_pers)

    recette["nombre de personnes"] = int(nb_pers)

    with open(recette["nom"] + " pour " + str(nb_pers) + " personne" + ("s" if int(nb_pers) > 1 else "") + ".json",
              "w") as f:
        json.dump(recette, f)

    print(recette)


def main():
    print("1 - Créer une recette")
    print("2 - Charger une recette")

    input_utilisateur = input("Que voulez-vous faire ? ")

    if input_utilisateur == "1":
        creer_recette()
    elif input_utilisateur == "2":
        nom = input("Nom de la recette ? ")
        charger_recette(nom)


if __name__ == "__main__":
    main()