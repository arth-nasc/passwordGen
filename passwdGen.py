import string
import random

lowerC=list(string.ascii_lowercase)
upperC=list(string.ascii_uppercase)
punc=list(string.punctuation)

def passGen(passLength=8,specialChars=False):
    passw=[]
    specRoll=False
    for i in range(passLength):
        roll=random.randint(1,3)
        bitRoll=random.randint(0, 1)
        specRoll=(specRoll^bitRoll)
        if roll==1:
            passw.append(random.choice(lowerC))
        if roll==2:
            passw.append(random.choice(upperC))
        if roll==3:
            passw.append(random.choice(string.digits))
        if specialChars and specRoll:
            passw.append(random.choice(punc))
            specRoll=False 
    return ''.join(passw)
