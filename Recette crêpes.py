"""recette crêpe"""

"""Calcul automatique des quantités d'ingrédients pour la recette des crêpes
    Auteur : Molinié Thibaut
    Date : Novembre 2022
    Programme visant à calculer les quantités d'ingrédients pour faire des crêpes à partir d'une recette pour deux personnes.
    Input : nombre de personnes n
    Output : quantités pour chaque ingrédient
    """


n = float(input('nombre de personnes :')) #entrée pour le nombre de personnes inscrit dans la variable n
farine=250*n/2 #formule pour la farine
oeuf=2*n/2 #formule pour les oeufs
sucre_vanille=1*n/2 #formule pour le sucre vanillé
beurre=40*n/2 #formule pour le beurre
lait=50*n/2 #formule pour le lait

#affichage des résultats en fonction des variables et avec l'unité de mesure pour chaque élément.

print("farine :",farine,"gr")
print("oeuf",oeuf)
print("sucre vanillé",sucre_vanille,"sachets")
print("Beurre",beurre,"gr")
print("Lait",lait,"cl")