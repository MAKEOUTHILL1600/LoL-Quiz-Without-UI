print('League of Legends QUIZ')
print('Va rugam sa scrieti cu minuscule! ')
raspuns = input('Esti gata xDD (da/nu): ')
scor = 0
intrebari_totale = 10

if raspuns.lower()=='da':
    raspuns = input('1) Cine e campionul SUPERIOR?! ')
    if raspuns.lower() == 'yasuo':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('2) Ce echipa a acastigat ultima data Campionatul Mondial? ')
    if raspuns.lower() == 'drx':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('3) Cum se numeste cel mai mare rank? ')
    if raspuns.lower() == 'challenger':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('4) Care e cel mai fioros monstru din joc?! ')
    if raspuns.lower() == 'scuttler':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('5) Cine e Satana in acest joc? ')
    if raspuns.lower() == 'teemo':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('6) Cat gold costa itemul "Trinity Force"? ')
    if raspuns.lower() == '3333':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('7) Care este singurul erou care se poate atasa de alti eroi? ')
    if raspuns.lower() == 'yuumi':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('8) Care este cel mai batran erou din joc? ')
    if raspuns.lower() == 'aurelian sol':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('9) Care este singurul erou care nu face parte din povestea Runeterra? ')
    if raspuns.lower() == 'seraphine':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

    raspuns = input('10) Cu ce erou a devenit faimos Faker? ')
    if raspuns.lower() == 'zed':
        scor = scor + 1
        print('CORECT!')
    else:
        print('GRESIT!!')

print('Multumesc pentru ca ai jucat! Ai raspuns corect la ',scor," intrebari! ")
mark=(scor/intrebari_totale)*100
print('Scor obtinut: ',mark)