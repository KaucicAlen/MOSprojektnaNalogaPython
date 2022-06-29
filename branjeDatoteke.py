import csv
from math import sqrt
from functions import *
import random
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification

# prebere cvs datoteko ter jo shrani v data
# with open('heart.csv', newline='') as f:
#    reader = csv.reader(f)
#    data = list(reader)
#

# naredi kopijo data, ki se lahko ureja


# prebere cvs datoteko ter jo shrani v data
with open('heart.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

pravilni = 0

newData = data.copy()
newData.pop(0)


# spremeni podatke v novem arraju
for x in newData:
    x.pop(7)
    x[0] = ageGroup(int(x[0]))
    x[3] = restingBp(int(x[3]))
    x[4] = cholesterol(int(x[4]))
    x[5] = bloodSugar(int(x[5]))
    x[8] = trening(float(x[8]))
    x[10] = stanje(int(x[10]))


stVseh = len(newData)
avgAcc = 0
avgSens = 0
avgSpec = 0
avgPrecision = 0
avgFmera = 0
avgFPR = 0

#with open("fixedData.cvs", "w") as f:
#    writer = csv.writer(f)
#    writer.writerows(newData)

#razdeli array na deset različnih, en za test in 9 za train
for x in range(10):
    truePositive = 0
    falseNegative = 0
    falsePositive = 0
    trueNegative = 0


    testArray = []
    trainArray = []

    if x == 0:
        for x in range(len(newData)):
            if x <= 90:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])
        rezultat = algoritem2(testArray, trainArray)

        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)
        

    elif x == 1:
        for x in range(len(newData)):
            if x > 91 and x <= 180:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])
        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate


        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 2:
        for x in range(len(newData)):
            if x > 181 and x <= 270:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])

        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 3:
        for x in range(len(newData)):
            if x > 271 and x <= 360:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])
        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 4:
        for x in range(len(newData)):
            if x > 361 and x <= 450:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])

        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 5:
        for x in range(len(newData)):
            if x > 451 and x <= 540:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])

        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 6:
        for x in range(len(newData)):
            if x > 541 and x <= 630:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])

        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 7:
        for x in range(len(newData)):
            if x > 631 and x <= 720:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])
        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)

    elif x == 8:
        for x in range(len(newData)):
            if x > 721 and x <= 810:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])
        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)
        
    elif x == 9:
        for x in range(len(newData)):
            if x > 811:
                testArray.append(newData[x])
            else:
                trainArray.append(newData[x])
        rezultat = algoritem2(testArray, trainArray)
        truePositive = truePositive + rezultat[0]
        trueNegative = trueNegative + rezultat[3]
        falseNegative = falseNegative + rezultat[1]
        falsePositive = falsePositive + rezultat[2]
        acc = ((truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)) * 100 #izracun acc
        sens = truePositive / (truePositive + falseNegative) #izracuna sensitivno, recall in True positive rate
        spec = trueNegative / (trueNegative + falsePositive) #izracuna specificnost
        precision = truePositive / (truePositive + falsePositive) #izracuna preciznost
        fmera = 2 * ((precision * sens) / (precision + sens)) #izracuna f mero
        falsePositiveRate = falsePositive / (falsePositive + trueNegative) #izracuna false positive rate

        avgAcc = avgAcc + acc
        avgSens = avgSens + sens
        avgSpec = avgSpec + spec
        avgPrecision = avgPrecision + precision
        avgFmera = avgFmera + fmera
        avgFPR = avgFPR + falsePositiveRate

        print("Tocnost: ",acc,"%")
        print("Sensitivnost: ",sens,"%")
        print("Specifičnost: ",spec,"%")
        print("Preciznost: ",precision,"%")
        print("F-mera: ",fmera)
        print("False Positive rate: ",falsePositiveRate)


print("avgAcc: ",avgAcc / 10,"%")
print("avgSens: ",avgSens / 10,"%")
print("avgSpec: ",avgSpec / 10,"%")
print("avgPrecision: ",avgPrecision / 10,"%")
print("avgFmera: ",avgFmera / 10)
print("avgFPR: ",avgFPR / 10)