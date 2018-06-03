import random
import zlib, base64
import hashlib
m = hashlib.sha1()
print "-----------------------Hash------------------------"
m.update(raw_input("Enter message: "))
print(m.hexdigest())

######RSA#########

print
print "-----------------------RSA of Hashed message------------------------"
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
    d = input("What's the private key?")
    if d == privateKey:
                  message = []
                  for item in cipherTextList:
                      decryptedLtr = chr((item**d) % statsTuple[0])
                      message.append(decryptedLtr)
       
                  print("Message:", ''.join(message))
    else:
                  print("Invalid key")

if __name__ == '__main__':
    mess = raw_input("Enter a hashed message to encrypt: ")
    k=encrypt(mess)
    print "Encrypted message: ",k
    l=getPrivateKey()
    print "Your private key: ",l

print
print "-----------------------Compression------------------------"
text = raw_input("Compression: ")
code =  base64.b64encode(zlib.compress(text,9))
print code

#############Vigenere###################

print
print "-----------------------Encryption Vigenere------------------------"
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A',	'B',	'C','D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',	'L',	'M',	'N',	'O',
           'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X', 'Y', 'Z',
           '.',',','?','1','2','3','4','5','6','7','8','9','0']


cipher = []
pos_key = []
pos_text = []
pos_cipher = 0
key = []
plain = []
letters_len = 40
import os
def find_pos(value):
        temp = []
        i=0
        while i<len(value):
                j=0
                while j<letters_len:
                        if value[i] == letters[j]:
                                temp.append(j)
                        j = j+1
                i= i+1
        return temp
        
def chek_end(m,n,size):
        if m==size and n<size:
                m=0
                return m
        if m==size and n==size:
                return m,n
        return m

def vigenere_encrypt(n):
       
        
        K = raw_input('Enter The Key ::::')
        P= raw_input('Enter The String To encrypt or decrypt ::::')
        key = map(lambda k:k.lower(),K)
        plain = map(lambda p:p.lower(),P)
        pos_key = find_pos(key)
        pos_text = find_pos(plain)                                      
        
        if len(pos_key) > len(pos_text):
                range_list = pos_key
        else :
                range_list = pos_text
        i=0
        j=0
        loop_pass = 0
        
        while i<len(range_list) and j<len(range_list) and loop_pass<len(pos_text):      
                try:
                        pos_cipher = n*pos_key[i] + pos_text[j]
                        if pos_cipher<letters_len:
                                cipher.append(letters[pos_cipher])
                        else:
                                pos_cipher = pos_cipher-letters_len
                                cipher.append(letters[pos_cipher])
                        i = i+1
                        j = j+1
                        
                        if i==len(pos_key) and j<len(pos_text):
                                i=0

                        elif j==len(pos_text) and i<len(pos_key):
                                j=0
                        loop_pass = loop_pass + 1
                except:
                        print("Oops Something went wrong")
        
        result = "" .join(cipher)
        print result
       
if __name__=='__main__':
        n = input (' 1 for encrypt \n-1 for decrypt\n:')
        vigenere_encrypt(n)
        
        pass
    

#############RSA - Session key###################

print
print "-----------------------RSA of Session key------------------------"        
if __name__ == '__main__':
    
    choice=''
    while choice != 3:
        choice = input("\nDo you want to encrypt or decrypt a session key?\nEnter 1 to Encrypt, 2 to Decrypt 3 to Exit Program: ")
        if choice == 1:
            message = raw_input("\nEnter the key to encrypt: ")
            c=encrypt(message)
            print "Encrypted message: ",c
            a=getPrivateKey()
            print "You private key: ",a
        elif choice == 2:
            decrypt(c)
        elif choice != 3:
            print ("You have entered an invalid choice. Please try again.\n\n")

################Vigenere#################################

print
print "-----------------------Decryption Vigenere------------------------"
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A',	'B',	'C','D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',	'L',	'M',	'N',	'O',
           'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X', 'Y', 'Z',
           '.',',','?','1','2','3','4','5','6','7','8','9','0']


cipher = []
pos_key = []
pos_text = []
pos_cipher = 0
key = []
plain = []
letters_len = 40
import os
def find_pos(value):
        temp = []
        i=0
        while i<len(value):
                j=0
                while j<letters_len:
                        if value[i] == letters[j]:
                                temp.append(j)
                        j = j+1
                i= i+1
        return temp
        
def chek_end(m,n,size):
        if m==size and n<size:
                m=0
                return m
        if m==size and n==size:
                return m,n
        return m

def vigenere_encrypt(n):
       
        
        K = raw_input('Enter The Key ::::')
        P= raw_input('Enter The String To encrypt or decrypt ::::')
        key = map(lambda k:k.lower(),K)
        plain = map(lambda p:p.lower(),P)
        pos_key = find_pos(key)
        pos_text = find_pos(plain)                                      
        
        if len(pos_key) > len(pos_text):
                range_list = pos_key
        else :
                range_list = pos_text
        i=0
        j=0
        loop_pass = 0
        
        while i<len(range_list) and j<len(range_list) and loop_pass<len(pos_text):      
                try:
                        pos_cipher = n*pos_key[i] + pos_text[j]
                        if pos_cipher<letters_len:
                                cipher.append(letters[pos_cipher])
                        else:
                                pos_cipher = pos_cipher-letters_len
                                cipher.append(letters[pos_cipher])
                        i = i+1
                        j = j+1
                        
                        if i==len(pos_key) and j<len(pos_text):
                                i=0

                        elif j==len(pos_text) and i<len(pos_key):
                                j=0
                        loop_pass = loop_pass + 1
                except:
                        print("Oops Something went wrong")
        
        result = "" .join(cipher)
        print result
       
if __name__=='__main__':
        n = input (' 1 for encrypt \n-1 for decrypt\n::::')
        vigenere_encrypt(n)
        pass

print
print "------------Decompression---------------------"
s=raw_input('Decompression: ')
data = zlib.decompress(base64.b64decode(s))
print data

print
print "------------RSA for Decrypt Hashed---------------------"
if __name__=='__main__':
    print("\nEnter the hashed message to decrypt: ")

    decrypt(k)

m = hashlib.sha1()
print "-----------------------Hash------------------------"
m.update(raw_input("Enter message: "))
print(m.hexdigest())
