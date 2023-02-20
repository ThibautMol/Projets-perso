"""Trouve le code du cadena à 3 chiffres version liste"""

import random

list_code = []
guess_nbr1 = 0
guess_nbr2 = 0
guess_nbr3 = 0
tentatives = 0

chiffre_code_1 = random.randint(0, 9)
list_code.append(chiffre_code_1)
chiffre_code_2 = random.randint(0, 9)
list_code.append(chiffre_code_2)
chiffre_code_3 = random.randint(0, 9)
list_code.append(chiffre_code_3)

while guess_nbr1 != list_code[0]:
    guess_nbr1 = int(input("Quel est le 1er chiffre du code?"))
    tentatives += 1

while guess_nbr2 != list_code[1]:
    guess_nbr2 = int(input("Quel est le 2ième chiffre du code?"))
    tentatives += 1

while guess_nbr3 != list_code[2]:
    guess_nbr3 = int(input("Quel est le 3ième chiffre du code?"))
    tentatives += 1

print("le code était", list_code)
print("vous l'avez trouvé en", tentatives)