choice=''
ciphertext = ''
plaintext2 = ''
plaintext=''
def encrypt(letter, key):

    # must be single alphabetic character
    if not letter.isalpha() or len(letter) != 1:
        return letter

    # convert to lowercase
    letter = letter.lower()

    # convert to numerical value 0 - 25
    # a = 0, b = 1, ... z = 25
    value = ord(letter) - 97

    # apply key, number of characters to shift
    value = (value + key) % 26

    # return encrypted letter
    return chr(value + 97)


def decrypt(letter, key):

    # must be single alphabetic character
    if not letter.isalpha() or len(letter) != 1:
        return letter

    # convert to lowercase
    letter = letter.lower()

    # convert to numerical value 0 - 25
    # a = 0, b = 1, ... z = 25
    value = ord(letter) - 97

    # apply key, number of characters to shift
    value = (value - key) % 26

    # return encrypted letter
    return chr(value + 97)


# number of characters to shift



while choice != 3:
    choice = input("\nDo you want to encrypt or decrypt the message?\nEnter 1 to Encrypt, 2 to Decrypt, 3 to Exit Program: ")
 
    if choice == 1:
        plaintext = raw_input('Enter the plaintext message: ')
        
        key = int(raw_input('Enter the secret key: '))
        
        for letter in plaintext:
            ciphertext += encrypt(letter, key)
        print 'ciphertext: {}\n'.format(ciphertext)
    elif choice == 2:
        ciphertext = raw_input('Enter the plaintext message: ')
        
        key = int(raw_input('Enter the secret key: '))
        
        for letter in ciphertext:
            plaintext2 += decrypt(letter, key)
        print 'plaintext2: {}'.format(plaintext2)
    elif choice != 3:
        print ("You have entered an invalid choice. Please try again.\n\n")


