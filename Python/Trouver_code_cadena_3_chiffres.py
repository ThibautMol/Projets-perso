"""Trouver code cadena 3 chiffres"""

import random
code=random.randint(0,999)
combinaison=000

for i in range (0,9) :
    combinaison +=1
    for j in range (0,9) :
        combinaison +=1
        for k in range (0,9) :
            combinaison +=1
            if code==combinaison :
                break
print("le code était", code)
