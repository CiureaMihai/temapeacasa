#Scrieți un program care generează un număr aleatoriu între 1 și 100 și permite utilizatorului să ghicească numărul.
#Programul ar trebui să furnizeze feedback ("mai mare" sau "mai mic") până când utilizatorul ghicește
#numărul corect. Programul ar trebui, de asemenea, să țină evidența numărului de încercări necesare pentru ca utilizatorul să ghicească corect.

import random

numar_aleatoriu = random.randint(1, 100)
numar_incercari = 0
ghicit = False

print("Ghiciți numărul între 1 și 100.")

while not ghicit:
    ghiceste = int(input("Introduceți un număr: "))
    numar_incercari += 1

    if ghiceste == numar_aleatoriu:
        ghicit = True
        print("Felicitări! Ați ghicit numărul corect în", numar_incercari, "încercări.")
    elif ghiceste < numar_aleatoriu:
        print("Numărul este mai mare. Încercați din nou.")
    else:
        print("Numărul este mai mic. Încercați din nou.")