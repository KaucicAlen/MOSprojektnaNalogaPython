
import numpy

#razdeli starosti v skupine A-K
def ageGroup(x):
    if x >= 25 and x <= 29:
        return "ageGroup A"
    if x >= 30 and x <= 34:
        return "ageGroup B"
    if x >= 35 and x <= 39:
        return "ageGroup C"
    if x >= 40 and x <= 44:
        return "ageGroup D"
    if x >= 45 and x <= 49:
        return "ageGroup E"
    if x >= 50 and x <= 54:
        return "ageGroup F"
    if x >= 55 and x <= 59:
        return "ageGroup G"
    if x >= 60 and x <= 64:
        return "ageGroup H"
    if x >= 65 and x <= 69:
        return "ageGroup I"
    if x >= 70 and x <= 74:
        return "ageGroup J"
    if x >= 75 and x <= 79:
        return "ageGroup K"

#razdeli trening v 
def trening(x):
    if x >= 0 and x <= 1:
        return "TreningGroup A"
    if x >= 1.1 and x <= 2:
        return "TreningGroup B"
    if x >= 2.1 and x <= 3:
        return "TreningGroup C"
    if x >= 3.1 and x <= 4:
        return "TreningGroup D"
    if x >= 4.1 and x <= 5:
        return "TreningGroup E"
    if x >= 5.1 and x <= 6:
        return "TreningGroup F"
    if x >= 6.1 and x <= 7:
        return "TreningGroup G"
    

    
#razdeli blood pressure v skupine
def restingBp(x):
    if x <= 120:
        return "Normal BP"
    if x >= 121 and x <= 129:
        return "Eleveted BP"
    if x >= 130 and x <= 139:
        return "High BP stage 1"
    if x >= 140:
        return "High BP stage 2"
    

#razdeli kolesterol v skupine
def cholesterol(x):
    if x <= 200:
        return "Desirable"
    if x >= 201 and x <= 239:
        return "Borderline high"
    if x >= 240:
        return "High"

#razdeli kolesterol v skupine
def bloodSugar(x):
    if x == 1:
        return "Okay"
    if x == 0:
        return "Not okay"

#razdeli stanje v skupine
def stanje(x):
    if x == 1:
        return "Pozitiven"
    if x == 0:
        return "Negativen"

        


def algoritem(testPolje, trainPolje, pozitivni, negativni):
    vsiPrimerki = len(trainPolje)
    vsiPozitivni = pozitivni
    vsiNegativni = negativni

    vodilnaPozitivnaCifra = vsiPozitivni / vsiPrimerki
    vodilnaNegativnaCifra = vsiNegativni / vsiPrimerki
    
    obrnjenaVodilnaPozitivnaCifra = vsiPrimerki / vsiPozitivni
    obrnjenaVodilnaNegativnaCifra = vsiPrimerki / vsiNegativni


    #presteje kolikokrat se iskan atribut pojavi
    poljeStIskani = []

    for y in testPolje:
        count = 0
        data = y
        for x in trainPolje:
            if x.count(data) == 1:
                count = count + 1
        #print("Število vseh: " , count)
        poljeStIskani.append(count)


    #presteje kolikokrat se iskan atribut pojavi ko je rezultat pozitiven
    poljeStIskaniPozitivno = []

    for y in testPolje:
        count = 0
        data = y
        for x in trainPolje:
            if x.count(data) == 1:
                if x[10] == "Pozitiven":
                    count = count + 1
        #print("Število pozitivnih: " , count)
        poljeStIskaniPozitivno.append(count)

    #presteje kolikokrat se iskan atribut pojavi ko je rezultat negativen
    poljeStIskaniNegativni = []

    for y in testPolje:
        count = 0
        data = y
        for x in trainPolje:
            if x.count(data) == 1:
                if x[10] == "Negativen":
                    count = count + 1
        #print("Število negativnih: " , count)
        poljeStIskaniNegativni.append(count)



    poljeStIskani.pop()
    poljeStIskaniPozitivno.pop()
    poljeStIskaniNegativni.pop()    

    #print(poljeStIskani)
    #print(poljeStIskaniPozitivno)
    #print(poljeStIskaniNegativni)

    #izracun cifer za formulo pozitivni
    poljeIzracunaneCifrePozitivni = []
    dolzina = len(poljeStIskani)

    for i in range(dolzina):
        if poljeStIskani[i] == 0:
            poljeStIskani[i] = 1
        rezultat = poljeStIskaniPozitivno[i] / poljeStIskani[i]
        rezultat = rezultat * obrnjenaVodilnaPozitivnaCifra
        poljeIzracunaneCifrePozitivni.append(rezultat)




    rezultatIzracunanihCiferPozitivni = numpy.prod(poljeIzracunaneCifrePozitivni)

    koncniRezultatPozitiven = vodilnaPozitivnaCifra * rezultatIzracunanihCiferPozitivni
    
    #izracun cifer za formulo negativni
    poljeIzracunaneCifreNegativni = []
    dolzina = len(poljeStIskani)

    for i in range(dolzina):
        rezultat = poljeStIskaniNegativni[i] / poljeStIskani[i]
        rezultat = rezultat * obrnjenaVodilnaNegativnaCifra
        poljeIzracunaneCifreNegativni.append(rezultat)




    rezultatIzracunanihCiferNegativni = numpy.prod(poljeIzracunaneCifreNegativni)

    koncniRezultatNegativen = vodilnaNegativnaCifra * rezultatIzracunanihCiferNegativni


    if koncniRezultatPozitiven > koncniRezultatNegativen:
        return "Pozitiven"
    else:
        return "Negativen"
   
        


def algoritem2(testArray, trainArray):
    #presteje stevilo pozitivnih in negativnih primerkov
    pozitivni = 0   
    negativni = 0  

    truePositive = 0
    falseNegative = 0
    falsePositive = 0
    trueNegative = 0

    stVseh = len(testArray)

    for x in trainArray:
        if x[10] == "Pozitiven":
            pozitivni = pozitivni + 1
        else:
            negativni = negativni + 1

    for x in testArray:
        vrednostPredikcije = algoritem(x, trainArray, pozitivni, negativni)
        print("Predikcija: " , vrednostPredikcije , " Prvotno: " , x[10])
        if x[10] == "Pozitiven":
            if vrednostPredikcije == "Pozitiven":
                truePositive = truePositive + 1
            elif vrednostPredikcije == "Negativen":
                falseNegative = falseNegative + 1
        elif x[10] == "Negativen":
            if vrednostPredikcije == "Pozitiven":
                falsePositive = falsePositive + 1
            elif vrednostPredikcije == "Negativen":
                trueNegative = trueNegative + 1

    return truePositive, falseNegative, falsePositive, trueNegative, vrednostPredikcije
        







