import numpy as np
import sdeint
import matplotlib.pyplot as plt

n = 20
B = np.diag(np.random.random_sample(n))
P = np.diag(np.random.random_sample(n))
tspan = np.linspace(0.0, 1, 1000)
x0 = np.zeros(n)

def f(x, t):
    return np.sqrt(P).dot(x)

def G(x, t):
    return np.ones_like(B)

result = sdeint.itoint(f, G, x0, tspan)

##### Create First Plot #####
plt.scatter(np.arange(result.shape[0]), np.linalg.norm(result, axis=1), s = 3)

result = sdeint.itoint(f, G, x0, tspan)
plt.scatter(np.arange(result.shape[0]), np.linalg.norm(result, axis=1), s = 3)

result = sdeint.itoint(f, G, x0, tspan)
plt.scatter(np.arange(result.shape[0]), np.linalg.norm(result, axis=1), s = 3)

plt.title('Norms of Vector SDE Matrix along time points')
plt.ylabel('Norms of timepoint vectors')
plt.xlabel('Timepoints')
plt.show()

##### Create Second Plot #####
arr = []
for i in range(0, 50):
    arr.append(sdeint.itoint(f, G, x0, tspan))
arr = np.array(arr)
arr = np.mean(arr, axis=0)
plt.scatter(np.arange(result.shape[0]), np.linalg.norm(arr, axis=1), s = 7)

plt.title('Mean Norms of Vector SDE Matrix along time points for 50 trajectories')
plt.ylabel('Mean Norms of timepoint vectors')
plt.xlabel('Timepoints')
plt.show()