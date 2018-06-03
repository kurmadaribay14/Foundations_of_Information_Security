code = raw_input("Enter plaintext: ")
print
ciphertext = ""

def hill(code): 
    Key = [[3,20,9],[10,9,4],[20,17,17]]
    code = code.lower()
    output = [[0],[0],[0]]
    counter = 0
    for item in code:
        numb = ord(item) - 97
        output[counter][0] = numb
        counter += 1

    resultat = [[0],[0],[0]]

    for i in range(len(Key)):
       for j in range(len(output[0])):
           for k in range(len(output)):
                resultat[i][0]+= Key[i][k]*output[k][j]
              
    cipheredText = ""
    for r in resultat:
       let = r[0] % 26
       val = chr(let + 97)
       cipheredText = cipheredText + val
    return cipheredText

while(code):
    plaintext = code[:3]
    code = code[3:]
    ciphertext = ciphertext + hill(plaintext)
print "The ciphertext is: ", ciphertext
print



