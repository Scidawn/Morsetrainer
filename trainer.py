from alphabet import morsecode as mc
from alphabet import examplesentences as exmp
import random
import string

playing = True
specialchars = {"ü":"ue","ö":"oe","ä":"ae","ß":"ss"}

def encrypt(msg):
    encryption = ""
    msg = msg.translate(str.maketrans('', '', string.punctuation))

    for letter in msg:
        if letter != ' ':
            try:
                encryption+= mc.get(letter.upper())+" "
            except:
                #raise Exception("Unsupported Chars")
                continue
        else:
            encryption+='/ '
    return encryption.strip()

def decrypt(msg):
    decryption = ""
    letters = msg.split(' ')
    for letter in letters:
        if letter != '/':
            key = next(key for key, value in mc.items() if value == letter)
            decryption+= key
        else:
            decryption+=' '
    return decryption

def train(mode):
    word = random.choice(random.choice(exmp).translate(str.maketrans('', '', string.punctuation)).split())  #word mode
    #word = random.choice(exmp).translate(str.maketrans('', '', string.punctuation))                         #sentence mode
    for char in specialchars:
        word = word.replace(char, specialchars.get(char))
    if mode == 'e':
        print(word)
        usertranslation = input()
        solution = encrypt(word)
        if usertranslation.strip() == solution.strip():
            print("Nice one")
        else:
            print("The correct answer would have been\n"+ solution)
    elif mode == 'd':
        print(encrypt(word))
        usertranslation = input()
        solution = word
        if usertranslation.lower().strip() == solution.lower().strip():
            print("Nice one")
        else:
            print("The correct answer would have been\n"+ solution)
    else:
        print("this mode is not supported.\naccepted answers are \'e\' and \'d\'.")


#print(encrypt("hallo welt"))
#print(decrypt('.-. --- -... --- - ... / .-. ..- .-.. .'))
print("here's your task: ")
while playing:
    train('e')
    train('d')
