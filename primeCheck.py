import math

def isPrime(n):
    squareRoot = math.sqrt(n)
    upperBound = math.floor(squareRoot) + 1
    print(upperBound)

    for i in range(2, upperBound):
        print(i)
        if (n % i == 0):
            print("false")
            break

    else:
        print("true")

print(isPrime(((2**148)+1)/17))
