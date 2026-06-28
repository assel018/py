import re

def ZeroOrMoreB():
    txt = input()
    x = re.findall("ab*", txt)
    print(x)
#ZeroOrMoreB()
# zero or more "b" following "a"

def TwoOrThree():
    txt = input()
    x = re.findall("ab{2,3}", txt)
    print(x)
#TwoOrThree()
# two or three "b" following "a"

def sequenceOfLowerLetters():
    txt = input()
    pattern = r"[a-z]+(?:_[a-z]+)+"
    x = re.findall(pattern,txt)
    print(x)
#sequenceOfLowerLetters()

def findAa():
    txt = input()
    x = re.findall("[A-Z][a-z]+", txt)
    print(x)
# findAa()

def startWithAEndWithB():
    txt = input()
    x = re.findall("^a.*b$", txt)
    print(x)
#startWithAEndWithB()

def replace():
    txt = input()
    x = txt
    pattern = r"[ ,.]"
    print(re.sub(pattern, ":", txt))
#replace()

def snakeToCamel():
    txt = input()
    x = txt.split("_")
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    for x in x:
        print(x, end="")
snakeToCamel()

def splitUpper():
    txt = input()
    x = re.split(r"(?=[A-Z])", txt)
    print(x)
#splitUpper()

def splitUpper2():
        txt = input()
        x = re.sub(r"([A-Z])", r" \1", txt).strip()
        print(x)
#splitUpper2()

def camelToSnake():
    txt = input()    
    x = re.sub(r"([A-Z])", r"_\1", txt).lower()

    if x.startswith("_"):
        x = x[1:]
    print(x)
#camelToSnake()

