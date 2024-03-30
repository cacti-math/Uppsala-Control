import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
### Here modify the name of the instance if it is different than instance.txt:
File = 'instance.txt'

size = np.genfromtxt(File, dtype=int, max_rows=1)
D = np.genfromtxt(File, skip_header=1)
for i in range(size):
    D[i][i] = float('inf')

D = np.array(D)
ord1 = D.argsort(axis=None, kind='mergesort')
ord2 = np.unravel_index(ord1, D.shape)
L = np.vstack(ord2).T
n = 4  # there are four nodes in example graph (graph is 1-based)

T = []
T.append(list(L[0]))
weight = D[L[0][0]][L[0][1]]

originDestiny = [[x,x] for x in list(range(size))]
originDestiny[L[0][0]][1] = L[0][1]
originDestiny[L[0][1]][0] = L[0][0]

for u in range(size):
    D[u][L[0][1]] = float('inf')
    D[L[0][0]][u] = float('inf')
np.delete(L, 0)

flgs = size - 1
for i in range(len(L)):
    if flgs == 1:
         break
    if (D[L[i][0]][L[i][1]] != float('inf') and L[i][1] != originDestiny[L[i][0]][0]):
        originDestiny[originDestiny[L[i][1]][1]][0] = originDestiny[L[i][0]][0]
        originDestiny[originDestiny[L[i][0]][0]][1] = originDestiny[L[i][1]][1]
        flgs = flgs - 1
        T.append(list(L[i]))
        weight += D[L[i][0]][L[i][1]]
        for u in range(size):
            D[u][L[i][1]] = float('inf')
            D[L[i][0]][u] = float('inf')

Solution = []
Solution.append(T[0][0])
Solution.append(T[0][1])
T.remove(T[0])
while T != []:
    for x in T:
        if x[0] == Solution[-1]:
            Solution.append(x[1])
            T.remove(x)
        elif x[1] == Solution[0]:
            Solution.insert(0, x[0])
            T.remove(x)


weight += D[Solution[-1]][Solution[0]]
Solution.append(Solution[0])
Solution = np.array(Solution)
Solution += 1
print("Greedy:")
print(Solution)
print(weight)
print()