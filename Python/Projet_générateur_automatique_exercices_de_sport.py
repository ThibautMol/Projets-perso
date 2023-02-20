#!/usr/bin/python3
# coding: utf-8

""""creer 3 fonctions : 
1- proposer niveau difficulte
2- determiner dans quoi on va sortir un sample d'exo
3- determiner les repetitions en fonction du niveau de difficulte"""

import random
from random import sample


"""difficulty_level_1=False
difficulty_level_2=False
difficulty_level_3=False"""

exercices_upper_body = [{
    "nom": "élévation laterale",
    "nbr_repet": 10},
    {"nom": "curl biceps",
    "nbr_repet": 10},
    {"nom": "tractions",
    "nbr_repet": 5},
    {"nom": "pompes",
    "nbr_repet": 5}]

exercices_abdo_and_legs = [{
    "nom": "crunch",
    "nbr_repet": 20},
    {"nom": "gainage planche",
    "nbr_repet": 20},
    {"nom": "gainage lateral droit",
    "nbr_repet": 20},
    {"nom": "gainage lateral gauche",
    "nbr_repet": 20},
    {"nom": "superman",
    "nbr_repet": 20},
    {"nom" : "squats",
    "nbr_repet" : 20},
    {"nom" : "fentes avant alternées",
    "nbr_repet" : 20},
    {"nom" : "fentes arrière alternées",
    "nbr_repet" : 20}]

exercices_cardio = [{
    "nom" : "jumping jack",
    "nbr_repet": 50}, 
    {"nom" : "mountain climber",
    "nbr_repet": 30}, 
    {"nom" : "monte de genoux",
    "nbr_repet": 50},
    {"nom": "squats sautés",
    "nbr_repet": 20},
    {"nom": "corde à sauter",
    "nbr_repet": 100}]

exercices_upper_body_choose = []
exercices_abdo_and_legs_choose = []
exercices_cardio_choose = []

seance = []

"""
def difficulty_level(difficulty) :
    
    if difficulty == 1 :
        difficulty_level_1 = True
        
    elif difficulty == 2 :
         difficulty_level_2 = True

    elif difficulty == 3 :
         difficulty_level_3 = True

    else :
        print("error, value invalid")
"""


def choose_exercices_upper_body(nbr):
    global exercices_upper_body_choose
    exercices_upper_body_choose=random.sample(exercices_upper_body, nbr)
    print(exercices_upper_body_choose)


def choose_exercices_abdo_and_legs(nbr):
    global exercices_abdo_and_legs_choose
    exercices_abdo_and_legs_choose=random.sample(exercices_abdo_and_legs, nbr)
    print(exercices_abdo_and_legs_choose)
     


def choose_exercices_cardio(nbr):
    global exercices_cardio_choose
    exercices_cardio_choose=random.sample(exercices_cardio, nbr)
    print(exercices_cardio_choose)   


difficulty = int(input("Choisissez votre niveau de difficulté entre 1, 2 et 3 : "))


nbr_upper_body_exercices = int(input
                               (f"Précisez combien d'exercices vous souhaitez pour le haut du corps entre 1 et {len(exercices_upper_body)}:"))

choose_exercices_upper_body(nbr_upper_body_exercices)


nbr_abdos_exercices = int(input
                          (f"Précisez combien d'exercices vous souhaitez pour les abdos entre 1 et {len(exercices_abdo_and_legs)} :"))

choose_exercices_abdo_and_legs(nbr_abdos_exercices)


nbr_cardio_exercices = int(input
                           (f"Précisez combien d'exercices vous souhaitez pour le cardio entre 1 et {len(exercices_cardio)} :"))

choose_exercices_cardio(nbr_cardio_exercices)



for exo in exercices_upper_body_choose:
    seance.append(
        {
            "nom": exo,
            "nombre_répétitions": "nbr_repet"*difficulty
        }
    )

for exo in exercices_abdo_and_legs_choose:
    seance.append(
        {
            "nom": exo,
            "nombre_répétitions": "nbr_repet"*difficulty
        }
    )

for exo in exercices_cardio_choose:
    seance.append(
        {
            "nom": exo,
            "nombre_répétitions": "nbr_repet"*difficulty
        }
    )


"""scratch 1 :
import csv
field_names= ['nom','nbr_repet']
difficulty=2
data=[]


list1=[{"nom": "bernard", "nbr_repet": int(20)},
{"nom" : "bianca", "nbr_repet" : int(10)},
{"nom" : "henry", "nbr_repet" : int(15)}]

#list1["nbr_repet"]=int(*difficulty)

with open('routine.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(list1)

with open ("routine.csv") as donnees :
    reader = csv.DictReader(donnees, delimiter=',')
    for ligne in reader :
        nom=str(ligne['nom'])
        nbr_repet=int(nbr_repet*difficulty)
        print ("nom", nom, "nbr", nbr_repet)
    nom=(ligne['nom'])
    data.append(ligne["nom"] + " " + nbr_repet)

    print(data)"""

"""scratch 2 :

resultat=[]
difficulty=int(2)
liste=[
    {"nom": "bob",
     "nbr_repet" : int(10)},
     {"nom" : "bianca",
      "nbr_repet" : int(15)},
      {"nom" : "henri",
       "nbr_repet" : int(22)}
]
x=0
for i in range (0, (len(liste))) :

    resultat.append(liste[x])
    x+=1

print(resultat)

resultat["nbr_repet"]=int(20)
#int(*difficulty)


#nom["nom"]=int(10*difficulty)

print(resultat)"""