from random import randint
def sortik():
    Numberushki = 10000
    # Dlina vsei etoi shtuki
    spisokchisel = []  # A tut koroche chisla na lutom randome prikol
    for a in range(Numberushki):
        spisokchisel.append(randint(0, 14020))  # Diapozon vsei chtuki
    print("До сортика, выглядело так, ну примерно", spisokchisel)  # tut randomnie chisla kotorie da

    for a in range(Numberushki - 1):  # nachalo nashgoi sortika
        for bi in range(Numberushki - a - 1):
            if spisokchisel[bi] > spisokchisel[bi + 1]:  # Tut esli bi chislo bolshe ono menaetsa
                spisokchisel[bi] \
                    , spisokchisel[bi + 1] = spisokchisel[bi + 1] \
                    , spisokchisel[bi]
    print("А тут после сортика", spisokchisel)

print("Можем начинать?")
print('1 - Da')
print('2 - Net')
otvet = int(input())
if otvet == 1:
    sortik()
else:
    if otvet == 2:
        print('Ny idi togda')