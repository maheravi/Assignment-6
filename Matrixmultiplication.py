import random


def Matrix_multiplication(A, B):
    result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def Matrix_Gen(a, b, c):
    M1 = [[random.randint(0, 10) for i in range(b)] for j in range(a)]
    M2 = [[random.randint(0, 10) for i in range(c)] for j in range(b)]
    return M1, M2


n = int(input('Enter the first number: '))
m = int(input('Enter the second number: '))
k = int(input('Enter the third number: '))

[M1, M2] = Matrix_Gen(n, m, k)
result = Matrix_multiplication(M1, M2)
print('The result of Multiplying two matrices is: ')
for i in result:
    print(i)