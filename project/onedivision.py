def findPeriod(i, result, odsek):
    print(i, result, odsek)
    return result % (10 ** odsek)


def long_division(a, b, memo):
    result = 0
    count = 0
    while True:
        if a == 0:
            break
        if b > a:
            if memo[a] != -1:
                return findPeriod(i, result, count - memo[a])
            else:
                memo[a] = count
            a *= 10
            result *= 10

        else:
            result += (a // b)
            a = a % b
            count += 1
    return result


def digitlen(a):
    count = 0
    while a != 0:
        count += 1
        a //= 10
    return count


if __name__ == "__main__":

    max = 0
    num = 0
    for i in range(1, 1000):
        memo = [-1] * i

        period = long_division(1, i, memo)
        #print(i, period)
        if digitlen(period) > max:
            max = digitlen(period)
            num = i
            #print(i, period, digitlen(period), max)

    print(num)
