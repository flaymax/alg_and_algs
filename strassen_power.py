import numpy as np 
import math

def to_the_power(matr, n):
    if n == 1:
        return matr
    if n % 2 == 1:
        return alg_strassen(to_the_power(matr, n - 1), matr)
    return alg_strassen(to_the_power(matr, int(n/2)), to_the_power(matr, int(n/2)))

    
def alg_strassen(matr_1, matr_2):
    
    if len(matr_1[0]) <= 8:
        tupled = list(zip(*matr_2))
        return [[sum((l * r) % 9 for l, r in zip(row, col)) % 9 for col in tupled] for row in matr_1]
    
    m = len(matr_1[0]) // 2
    
    ################### splittting
    
    A11= [row[:m] for row in matr_1[:m]]
    B11= [row[:m] for row in matr_2[:m]]
    A12= [row[m:] for row in matr_1[:m]]
    B12= [row[m:] for row in matr_2[:m]]
    A21= [row[:m] for row in matr_1[m:]]
    B21= [row[:m] for row in matr_2[m:]]
    A22= [row[m:] for row in matr_1[m:]]
    B22= [row[m:] for row in matr_2[m:]]
    
    M1 = alg_strassen(matrix_sum(A11, '+', A22), matrix_sum(B11, '+', B22))
    M2 = alg_strassen(matrix_sum(A21, '+', A22), B11)
    M3 = alg_strassen(A11, matrix_sum(B12, '-', B22))
    M4 = alg_strassen(B22, matrix_sum(B21, '-', B11))
    M5 = alg_strassen(matrix_sum(A11, '+', A12), B22)
    M6 = alg_strassen(matrix_sum(A21, '-', A11), matrix_sum(B11, '+', B12))
    M7 = alg_strassen(matrix_sum(A12, '-', A22), matrix_sum(B21, '+', B22))

    C11 = matrix_sum(matrix_sum(M1, '+', M4), '+', matrix_sum(M7, '-', M5))
    C12 = matrix_sum(M3, '+', M5)
    C21 = matrix_sum(M2, '+', M4)
    C22 = matrix_sum(matrix_sum(M1, '-', M2), '+', matrix_sum(M3, '+', M6))
    
    ################### merging
    
    n = len(C11[0])
    matrix = [[0 for j in range(2 * n)] for i in range(2 * n)] 

    for i in range(n):
        matrix[i][:n] = C11[i]
    
        matrix[i][n:] = C12[i]
        matrix[i + n][:n] = C21[i]
        matrix[i + n][n:] = C22[i]
        

    return matrix

def matrix_sum(matr_1, oper, matr_2):
    n = len(matr_1[-1])
    if oper == '+':
        return [[(matr_1[i][j] + matr_2[i][j]) % 9 for j in range(n)] for i in range(n)]
    else:
        return [[(matr_1[i][j] - matr_2[i][j]) % 9 for j in range(n)] for i in range(n)]
        

input_matr = []
first_row = list(map(int, input().split()))
n = len(first_row)
#input_matr.append(first_row)

#for i in range(n - 1):
#    input_matr.append(list(map(int, input().split())))
#print(input_matr)
degree = 2 ** int(math.ceil(math.log2(n)))
matrix = [[0 for j in range(degree)] for i in range(degree)]
for i, element in enumerate(first_row):
        matrix[0][i] = element

for i in range(n - 1):
        row = list(map(int, input().split()))
        for j, k in enumerate(row):
            matrix[i + 1][j] = k
        
ans = to_the_power(matrix, n)
if len(first_row)==1:
    print(first_row[0] % 9, end='')
else:
    for i in range(len(ans[:n])):
        for j in range(len(ans[:n])):
            if j == len(ans[:n])-1:
                print(ans[i][j], end='')
            else:
                print(ans[i][j], end=' ')
        if i==len(ans[:n]):
            pass
        else:
            print('')