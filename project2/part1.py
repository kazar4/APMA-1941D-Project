import numpy as np
import matplotlib.pyplot as plt
import tenpy
from skrmt.ensemble import GaussianEnsemble

# Eigenvalue dist for n = 100, m = 25, 50, ... 100

n = 100
m = 150

for i in range(20, 101, 20):
    eigDist = []
    for j in range(100):
        
        m = np.random.normal(0, 0.02, (i, i))
        goe = (m + m.transpose())/2

        eigs = np.linalg.eigvalsh(goe)
        eigs = np.unique(eigs)

        for e in eigs:
            eigDist.append(e)

    plt.hist(eigDist, bins=100)
    plt.show()


# Checking with libraries if distribution mkes sense
#P = tenpy.linalg.random_matrix.GOE((i, i))
#goe = GaussianEnsemble(beta=1, n=i).matrix * 1/20