import numpy as np
import matplotlib.pyplot as plt

# Eigenvalue dist for n = 100, m = 25, 50, ... 100

n = 100
m = 150

eigVals = []
xAxis = []
for i in range(1, m + 1, 25):
    eigDist = []
    for j in range(100):
        X = np.random.normal(scale=n**-0.5, size=(n, i))
        #print(X.shape)
        P = (1/n) * np.dot(X, X.T)
        eigs = np.linalg.eigvalsh(P)
        #print(eigs)
        eigs = np.unique(eigs)
        #print(eigs)
        #print(len(eigs)
        currEigs = []
        currXAxis = []
        for e in eigs:
            eigDist.append(e)
            #print(e.shape)
            eigVals.append(e)
            xAxis.append(i)

            currEigs.append(e)
            currXAxis.append(i)
    plt.hist(eigDist, bins=100)
    plt.show()

#print(eigVals)
#print(xAxis)

#plt.hist(eigVals, bins=100)
#plt.plot(xAxis, eigVals)
#plt.ylabel('some numbers')
plt.show()
