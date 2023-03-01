
"""développer l'idée en créant :
-joueur contre ordinateur 
-entrer le nom du joueur1
-définir ordre de passage via du random
-créer un tableau affichant les 3 choix et une option pour mettre fin à la partie et afficher le score
-ordinateur va tirer un choix en random parmis les 3
-stocker ça dans un dictionnaire
-demander le choix pour chaque joueur
-dire le résultat de chaque partie"""

"""vrai si joueur_1 bat le joueur_2 :

faux si joueur_2 bat joueur_1 ou fait match nul contre lui."""

def bat(joueur_1, joueur_2):
    # pierre=0, feuille=1, ciseaux=2
    resultats = {(0, 1): False, (0, 2): True, (1, 0): True, (1, 2): False, (2, 0): False, (2, 1): True}
    return resultats[(joueur_1, joueur_2)]


import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2
score=0


def partie(coup_j, coup_o) :
    
    global score
    
    if coup_j==coup_o :
        pass
    
    elif coup_j==PIERRE and coup_o==FEUILLE :
        score+=-1
        
    
    elif coup_j==PIERRE and coup_o==CISEAUX :
        score+=1
        
    
    elif coup_j==FEUILLE and coup_o==PIERRE :
        score+=1
        
    
    elif coup_j==FEUILLE and coup_o==CISEAUX :
        score-=1
        
    
    elif coup_j==CISEAUX and coup_o==PIERRE :
        score-=1
        
    
    elif coup_j==CISEAUX and coup_o==FEUILLE :
        score+=1
        
    return score

# resultat=score

partie(int(input()),random.randint(0,2))



print("le score est de :", score)

