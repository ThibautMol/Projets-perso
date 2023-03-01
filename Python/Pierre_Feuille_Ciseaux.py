
"""développer l'idée en créant :
-joueur contre ordinateur 
-entrer le nom du joueur1
-définir ordre de passage via du random
-créer un tableau affichant les 3 choix et une option pour mettre fin à la partie et afficher le score
-ordinateur va tirer un choix en random parmis les 3
-stocker ça dans un dictionnaire
-demander le choix pour chaque joueur
-dire le résultat de chaque partie"""
def bat(joueur_1, joueur_2):
    # pierre=0, feuille=1, ciseaux=2
    resultats = {(0, 1): False, (0, 2): True, (1, 0): True, (1, 2): False, (2, 0): False, (2, 1): True}
    return resultats[(joueur_1, joueur_2)]
