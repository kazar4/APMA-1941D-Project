import numpy as np
import math

# Bigram frequencies  
M = np.zeros((27,27))
with open("AustenCount.txt") as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            row = l.split()
            for j, val in enumerate(row):
                M[i,j] = int(val)

logM = np.log(M.astype(int) + 1)

# text to decode
text = ""
with open("f_9.txt") as f:
        text = f.readline()

# coversions from text to numbers
alphabet = list("abcdefghikjlmnopqrstuvwxyz ")
asciiVals = {i: val for i, val in enumerate(alphabet)}
asciiValsReverse = {val: i for i, val in enumerate(alphabet)}

# calculates score given text
def score(currentVals):
    arr = np.array(list(currentVals))
    arr = np.vectorize(asciiValsReverse.__getitem__)(arr)
    arr_unshift = arr[:len(arr) - 1]
    arr_shift = arr[1:] # shape ex (50), get to (50, 2)

    arr_unshift = np.expand_dims(arr_unshift, axis=1)
    arr_shift = np.expand_dims(arr_shift, axis=1)
    arr_combined = np.append(arr_unshift, arr_shift, axis=1)

    arr_more = np.apply_along_axis(lambda a: logM[a[0], a[1]], 1, arr_combined)

    return np.sum(arr_more)

# given a matrix for swaps, this will return the potentially decoded text
def getAnswer(text, chooser):
    newtext = ""
    for t in text:
        newtext = newtext + asciiVals[chooser[asciiValsReverse[t]]]
    
    return newtext


# chooser with no swaps
chooser = np.arange(27)

# score before starting
preScore = score(getAnswer(text, chooser))

for i in range(1,50001):
    chosen = np.random.choice(np.arange(27), 2, replace=False)
    preChooser = chooser.copy()

    chooser[chosen[0]] = preChooser[chosen[1]]
    chooser[chosen[1]] = preChooser[chosen[0]]

    calcScore = score(getAnswer(text, chooser))
    uni = np.random.uniform(size=1)[0]

    # if score is below 0 it can be ignored, and if it is above 100 it will go through
    scoreDif = 0
    if (calcScore - preScore > 0):
        if (calcScore - preScore > 100):
            scoreDif = 100
        else:
            print(calcScore - preScore)
            scoreDif = math.exp(calcScore - preScore)

    if uni < scoreDif:
        preScore = calcScore
    else:
        chooser = preChooser.copy()
    
    if i % 1000 == 0:
        print("~~~")
        print(getAnswer(text, chooser))
        print("~~~")
