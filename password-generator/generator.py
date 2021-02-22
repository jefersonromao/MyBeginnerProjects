import random

def uppercaseLetter():
    upperLetter = chr(random.randint(65, 90))

    return upperLetter

def lowercaseLetter():
    lowerLetter = chr(random.randint(97, 122))

    return lowerLetter


def numbers():
    number = chr(random.randint(48, 57))

    return number


def symbols():
    symbol = chr(random.randint(33, 46))

    return symbol

lower = lowercaseLetter()
upper = uppercaseLetter()
number = numbers()
symbol = symbols()

password = lowercaseLetter() + uppercaseLetter() + uppercaseLetter() + lowercaseLetter() + numbers() + lowercaseLetter() + numbers() + lowercaseLetter()
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(password)

