import numpy as np
import matplotlib.pyplot as plt

# Eigenvalue dist for n = 100, m = 25, 50, ... 100

n = 100
m = 150

eigVals = []
xAxis = []
k = 0
for i in range(25, m + 1, 25):
    k = k + 1
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

    plt.subplot(2, 3, k)
    plt.hist(eigDist, bins=100)
    plt.xlabel("eigenvalues")
    plt.ylabel("bin count")
    plt.title(f'n={i}')
    plt.subplots_adjust(hspace=0.5, wspace=0.5)

#print(eigVals)
#print(xAxis)

#plt.hist(eigVals, bins=100)
#plt.plot(xAxis, eigVals)
#plt.ylabel('some numbers')
plt.show()
