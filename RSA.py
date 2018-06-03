import random

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []    
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primeslist = get_primes(100)
def getStats():
    p = primeslist[random.randint(0,17)]
    q = primeslist[random.randint(0,17)]
    n = p*q
    phi = (p-1)*(q-1)
    e = 7
 
    return (n, phi, e)

statsTuple = getStats()
def getPrivateKey():
    newPhi = statsTuple[1]
    newE = statsTuple[2]
    def euclid(num1, num2, num3, num4):
        if num3 ==1:
            key = num4
            return key
        else:
            newNum3 = num1 - ((num1//num3)*num3)
            newNum4 = (num2 - (num4*(num1//num3)))%newPhi
            return euclid (num3, num4, newNum3, newNum4)
    return euclid(newPhi, newPhi, newE, 1)
privateKey = getPrivateKey()

def encrypt(message): 
    cipherList = []
    for ltr in message:
        encrpytedLtr = (ord(ltr)**statsTuple[2]) % statsTuple[0]
        cipherList.append(encrpytedLtr)
    return cipherList
 
def decrypt(cipherTextList):
    d = input("What's the private key? ")
    if d == privateKey:
                  message = []
                  for item in cipherTextList:
                      decryptedLtr = chr((item**d) % statsTuple[0])
                      message.append(decryptedLtr)
       
                  print("Message:", ''.join(message))
    else:
                  print("Invalid key")

if __name__ == '__main__':
    mess = raw_input("Enter a message to encrypt with your private key: ")
    c=encrypt(mess)
    print "Encrypted message: ",c
    a=getPrivateKey()
    print "Private key: ",a
    decrypt(c)
