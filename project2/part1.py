import numpy as np
import matplotlib.pyplot as plt
#import tenpy
#from skrmt.ensemble import GaussianEnsemble

# Eigenvalue dist for n = 100, m = 25, 50, ... 100

n = 100
m = 150
k = 0

for i in range(20, 101, 20):
    k = k + 1
    eigDist = []
    for j in range(100):
        
        m = np.random.normal(0, np.sqrt(2/n), (i, i))
        goe = (m + m.transpose())/2

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


# Checking with libraries if distribution mkes sense
#P = tenpy.linalg.random_matrix.GOE((i, i))
#goe = GaussianEnsemble(beta=1, n=i).matrix * 1/20