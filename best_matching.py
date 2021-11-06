import random

def triangular(matrix, field):
    for i in range(1, len(matrix)):
        idx = -999
        col = i - 1
        for l in range(i - 1, len(matrix)):
            if matrix[l][col] != 0:
                idx = l
                break
        if idx == -999:
            continue
        elif i - 1 != idx:
            matrix[idx], matrix[i-1] = matrix[i-1], matrix[idx]
        a = matrix[i - 1][col]
        for j in range(i, len(matrix)):
            b = matrix[j][col]
            if b == 0:
                continue
            new = []
            for n, m in zip(matrix[j], matrix[i - 1]):
                n_ = (n - (m * field[a] * b) % mod) % mod
                if n_ >= 0:
                    new.append(n_)
                else:
                    new.append(mod + n_)
            matrix[j] = new
    #print(matrix)
    #assert
    return matrix      


edges = []
node = -1
mod = 7933 # module

with open("read.txt") as f:
    n = int(f.readline().replace('\n', ''))
    print(n)
    for i in range(n):
        line = f.readline().replace('\n', '')
        print(line)
        node_1, node_2 = [int(x) for x in line.split(' ')]
        node = sorted([node_1, node_2, node])[-1]
        edges.append((node_1, node_2))
f.close()

"""n = int(input())
for i in range(n):
    line = input()
    node_1, node_2 = [int(x) for x in line.split(' ')]
    node = sorted([node_1, node_2, node])[-1]
    edges.append((node_1, node_2))"""
# input matrix
matrix = [[0 for _ in range(node + 1)] for _ in range(node + 1)]
for node_1, node_2 in edges:
    matrix[node_1][node_2] = random.randint(1, mod - 1)
field = [-1  for i in range(mod)]
for i in range(mod):
    if i<=1:
        continue
        #assert i * field[i] //
    else:
        field[i] = mod - (field[mod % i] * (mod // i)) % mod
tri_matrix = triangular(matrix, field)
flag = 0
for i in range(len(tri_matrix)):
    if tri_matrix[i][i] == 0:
        flag = 1
        break
if not flag:
    print('yes')
else:
    print('no')