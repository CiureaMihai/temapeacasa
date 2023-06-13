#Scrieți un program care utilizează o buclă while pentru a genera secvența Fibonacci până la un număr dat de termeni.
#Secvența Fibonacci este o serie de numere în care fiecare număr este suma celor două numere precedente. Secvența începe cu 0 și 1.


def generare_fibonacci(numar_termeni):
    secventa = []
    termen1 = 0
    termen2 = 1

    if numar_termeni == 0:
        return secventa
    elif numar_termeni == 1:
        secventa.append(termen1)
        return secventa
    elif numar_termeni == 2:
        secventa.append(termen1)
        secventa.append(termen2)
        return secventa

    secventa.append(termen1)
    secventa.append(termen2)
    numar_termeni -= 2

    while numar_termeni > 0:
        termen_nou = termen1 + termen2
        secventa.append(termen_nou)
        termen1 = termen2
        termen2 = termen_nou
        numar_termeni -= 1

    return secventa

numar_termeni = int(input("Introduceți numărul de termeni pentru secvența Fibonacci: "))

if numar_termeni <= 0:
    print("Numărul de termeni trebuie să fie un număr pozitiv.")
else:
    secventa_fibonacci = generare_fibonacci(numar_termeni)
    print("Secvența Fibonacci cu", numar_termeni, "termeni este:")
    print(secventa_fibonacci)