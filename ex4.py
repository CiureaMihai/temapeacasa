#Scrieți un program care utilizează o buclă while pentru a verifica dacă un număr întreg pozitiv dat n este un număr prim. Un număr prim este un număr
#întreg pozitiv mai mare decât 1 care nu are divizori pozitivi în afară de 1 și el însuși. Programul ar trebui să afișeze dacă numărul este prim sau nu.


def este_numar_prim(n):
    if n <= 1:
        return False

    divizor = 2

    while divizor * divizor <= n:
        if n % divizor == 0:
            return False
        divizor += 1

    return True

numar = int(input("Introduceți un număr întreg pozitiv: "))

if este_numar_prim(numar):
    print(numar, "este un număr prim.")
else:
    print(numar, "nu este un număr prim.")