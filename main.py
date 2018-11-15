
cyfry = []
##### Wczytanie pliku
with open('res/cyfry.txt') as plik_cyfry:
    for line in plik_cyfry:
        cyfry.append(int(line))


##### zad A
parzyste = 0;
for liczba in cyfry:
    if liczba % 2 == 0:
        parzyste += 1
print("A - parzyste: " + str(parzyste))

##### zad B
najwieksza = None
najmniejsza = None
suma_cyfr = []

def suma_liczby(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

i = 0
for liczba in cyfry:
    suma_cyfr.append(suma_liczby(liczba))

najmniejsza = suma_cyfr[0]
najmniejsza_index = 0
najwieksza = suma_cyfr[0]
najwieksza_index = 0

i = 0
for liczba in suma_cyfr:
    if liczba > najwieksza:
        najwieksza = liczba
        najwieksza_index = i
    if liczba < najmniejsza:
        najmniejsza = liczba
        najmniejsza_index = i
    i += 1
print("B - najwieksza: " + str(cyfry[najwieksza_index]))
print("B - najmniejsza: " + str(cyfry[najmniejsza_index]))


##### zad C


