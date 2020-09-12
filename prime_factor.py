def isPrime(x):
    num = 2 ** x

    if x != 0:
        if num % x == 2 or x == 2:
            return True
    return False

def isDivisable(x, div):
    if x and div != 0:
        if int(x / div) == (x / div):
            return True
    return False

def factorize(x):
    arr = []

    i = 0
    while i <= x:
        if isPrime(i) and isDivisable(x, i):
            arr.append(i)
            x /= i
            i = 0

        if x == 1:
            break
        i += 1

    return arr

def unfactorize(x):
    mathSum = 0

    for i in x:
        if mathSum == 0:
            mathSum = i
        else:
            mathSum *= i
            
    return mathSum

print(unfactorize(factorize(255)))