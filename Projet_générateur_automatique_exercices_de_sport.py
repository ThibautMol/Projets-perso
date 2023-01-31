"""Projet générateur automatique exercices de sport"""

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

    """demander à l'utilisateur combien de zone du corps il veut cibler (bas du corps, haut du corps, abdos, cardio). 
    l'utilisateur peut choisir entre 1 et 4 type d'exo. s'il tape 0, renvoyer "merci au revoir" et terminer le programme.
    demander quel exercice il veut et compter. quand le nombre de type d'exo est choisi, on passe à la prochaine étape.
    afficher la liste : 
    1 exercice bas du corps
    2 exercices abdos
    3 exercice haut du corps
    4 cardio
    demander combien l'utilisateur veut d'exercices
    lorsqu'un nombre est choisi la phrase "quel type d'exercice choisir" revient. 
    faire un décompte en fonction du nombre de type d'exercice choisi. Quand ça arrive à 0 on change d'étape.
    enregistrer l'ordre et le type d'exo dans un fichier a côté
    lancer un choix random de chiffres en fonction du nombre d'exercices enregistrés pour déterminer les exo à faire.
    Créer une alternance entre un exo de chaque type choisi (bas du corps, haut du corps, abdos, etc) pour ne pas avoir deux exercices qui se suivent sur la même zone. 
    sortir un résumé des exo choisis avec le nom de chacuns 
          
    """