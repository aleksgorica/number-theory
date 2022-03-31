from factorial import factorial


def c(n, k):
    memo = [[False]*(k+1)]*(n+1)
    print(memo)
    def c_rek(n, k):
        if (k == 0):
            if (n == 0): return 1
            return 0
        if (k > n or k < 0): return 0
        if (n == k): return 1
        if (k == 1): return factorial(n-1)
        if (memo[n][k] != False):
            return memo[n][k]
        else:
            result = c_rek(n-1, k-1) + (n-1)*c_rek(n-1, k)
            memo[n][k] = result
            return result
    return c_rek(n, k)
        


def stirling_square(n):
    square = [[0]*n]*n
    print(square)
    for i in range(n):
        for j in range(n):
            if (j > i): 
                square[i][j] = 0
                continue            
            if (i == j):
                square[i][j] = 1
                continue
            if (i == 0 or j == 0):
                square[i][j] = 0
                continue
            square[i][j] = square[i-1][j-1] + square[i-1][j]
        print(i, j, square[i])

    return square


#stevilo ekvivalencnih relacij na mnozici z n elementi s k ekvivalencnimi razredi
#stevilo vseh surjekvij k!S(n,k)
def S(n, k):
    sum = 0
    for i in range(k+1):
        value = (-1)**(k-i) * 
    memo = [[False]*(k+1)]*(n+1)
    def S_rek(n, k):
        if (k == n): return 1
        if (k == 1): return 1
        if (k == 0):
            if (n == 0): return 1
            return 0
        if (k > n or k < 0 or n < 0): return 0
    return S_rek(n,k)

#stevilo ekvivalencin relacij na [n]
def B(n):
    sum = 0
    for i in range(n+1):
        sum += S(n, i)
    return sum
