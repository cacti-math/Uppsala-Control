import numpy as np

File = 'instance.txt'

n = np.genfromtxt(File, dtype=int, max_rows=1)-1
dist = np.genfromtxt(File, skip_header=1)
for i in range(n+1):
    dist[i][i] = float('inf')

dist = np.array(dist)

# memoization for top down recursion
memo = [[(-1, []) for _ in range(1 << (n + 1))] for _ in range(n + 1)]


def fun(i, mask):
    if mask == ((1 << i) | 3):
        return dist[1][i], [1, i]

    if memo[i][mask][0] != -1:
        return memo[i][mask]

    res = 10 ** 9
    best_path = []
    for j in range(1, n + 1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            temp_res, temp_path = fun(j, mask & (~(1 << i)))
            temp_res += dist[j][i]
            if temp_res < res:
                res = temp_res
                best_path = temp_path + [i]

    memo[i][mask] = (res, best_path)
    return res, best_path


ans = 10 ** 9
final_path = []
for i in range(1, n + 1):
    temp_ans, temp_path = fun(i, (1 << (n + 1)) - 1)
    temp_ans += dist[i][1]
    if temp_ans < ans:
        ans = temp_ans
        final_path = temp_path + [1]

print("The cost of most efficient tour =", ans)
print(final_path)

# This code is a modified version of program of Serjeel Ranja
# www.geeksforgeeks.org/travelling-salesman-problem-using-
dynamic-programming/amp/
