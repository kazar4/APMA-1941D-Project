import numpy as np
import matplotlib.pyplot as plt

########### Part 1 GOE Ensemble #############

n = 100
k = 0
samples = 100

for i in range(20, n + 1, 20):
    k = k + 1
    eigDist = []
    for j in range(samples): # num of times sampling is done
        
        mat = np.random.normal(0, np.sqrt(2/n), (i, i))
        goe = (mat + mat.transpose())/2

        eigs = np.linalg.eigvalsh(goe)
        eigs = np.unique(eigs)

        for e in eigs:
            eigDist.append(e)

    plt.subplot(2, 3, k)
    plt.hist(eigDist, bins=100, range=(-2,2))
    plt.xlabel("eigenvalues")
    plt.ylabel("bin count")
    plt.title(f'n={i}')
    plt.subplots_adjust(hspace=0.5, wspace=0.5)

plt.show()

########## Part 2 Marchenko-Pastur ###########

n = 100
m = 150
k = 0
samples = 100

for i in range(25, m + 1, 25):
    k = k + 1
    eigDist = []
    for j in range(samples): # num of times sampling is done
        X = np.random.normal(size=(n, i))
        P = (1/n) * np.dot(X, X.T)

        eigs = np.linalg.eigvalsh(P)
        eigs = np.unique(eigs)
  
        for e in eigs:
            eigDist.append(e)

    plt.subplot(2, 3, k)
    plt.hist(eigDist, bins=100)
    plt.xlabel("eigenvalues")
    plt.ylabel("bin count")
    plt.title(f'm={i} ratio={i/n}')
    plt.subplots_adjust(hspace=0.5, wspace=0.5)

plt.show()