text=''
key=''

alphabet_pos = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,
't':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def alphabet_position(letter):
    alphabet_pos = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
    'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,
    't':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    
    pos = alphabet_pos[letter]
    return pos

def rotate(letter, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - shift) % 26 + shift)

def encrypt(text, key):
    encrypted = []    
    starting_index = 0
    for letter in text:
    # if it's alphanumerical, keep it that way
    # find alphabet position
        rotation = alphabet_position(key[starting_index])
    # if it's a space or non-alphabetical character, append and move on
        if not letter in alphabet_pos:
            encrypted.append(letter)
        elif letter.isalpha():            
            encrypted.append(rotate(letter, rotation))             

    #if we've reached last index, reset to zero, otherwise + by 1
        if starting_index == (len(key) - 1): 
            starting_index = 0
        else: 
            starting_index += 1

    return ''.join(encrypted)    

text = raw_input("Enter some text:")
key = raw_input("Enter a key:")

print(encrypt(text,key))
