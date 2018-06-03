
def qwerty(code):
    b=[]
    for i in range(0, len(code)):
        b.append(ord(code[i])-97)
    return b
def hill(code,decryptionKey): 
    output = []
    for i in range(0, len(code)):
        b=[]
        b.append(ord(code[i])-97)
        output.append(b)
    result = [[0],[0],[0]]

    for i in range(len(decryptionKey)):
       for j in range(len(output[0])):
           for k in range(len(output)):
               result[i][0] += decryptionKey[i][k] * output[k][j]
    unCiphered = ''
    
    for r in result:
       numeric_letter = r[0] % 26
       unCiphered = unCiphered + chr(numeric_letter + 97)
    return unCiphered

def main():
    text = raw_input("Enter ciphertext:").upper()
    abc = raw_input("Enter key:").upper()
    qw=[]
    plaintext = ''
    while(abc):
        ciphertext = abc[:3]
        abc = abc[3:]
        qw.append(qwerty(ciphertext))
    while(text):
        ciphertext = text[:3]
        text = text[3:]
        plaintext = plaintext + hill(ciphertext,qw)
    print plaintext

main()
          
