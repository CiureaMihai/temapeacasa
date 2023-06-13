#Scrieți un program care utilizează o buclă
#while pentru a calcula factorialul unui număr întreg pozitiv dat n. Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.




def calcul_factorial(n):
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    return factorial

numar = int(input("Introduceți un număr întreg pozitiv: "))

if numar < 0:
    print("Numărul introdus trebuie să fie pozitiv.")
else:
    rezultat = calcul_factorial(numar)
    print("Factorialul numărului", numar, "este:", rezultat)
