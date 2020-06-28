import math
import random
import time


# euler totient of n
def euler_totient_function(p,q):
    euler = (p-1)*(q-1)
    return euler


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(a,a%b)

#choose an e such that e is coprime to the phi(N)
def chooseE(eulertotientfunc):
    #randomValue = random.seed(time.time())
    #randomMod = randomValue % eulertotientfunc

    randomMod = random.randint(1,eulertotientfunc)
    print(randomMod)
    print("gcd", str(gcd(randomMod, eulertotientfunc)))

    if(gcd(randomMod, eulertotientfunc)==1):
        #coprime
        return randomMod
    else:
        #run function again if not coprime
        return chooseE(eulertotientfunc)

def modInverse(a, m):
    a = a % m
    for x in range(1,m):
        if((a * x) % m == 1):
            return x
    return 1


#2 prime numbers p and q
#p = ((2**148)+1)/17
#q = ((2**64)+1)/274177
p = 7919
q = 7723
N=p*q

phiN = euler_totient_function(p, q)
#publicKey = chooseE(phiN)
publicKey = 2**16+1
privateKey = modInverse(publicKey,phiN)

print("p: ", p)
print("q: ", q)
print("N: ", N)
print("phi(N): ", phiN)
print("publicKey: ", publicKey)
print("privateKey: ", privateKey)
