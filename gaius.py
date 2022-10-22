# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
from xml.etree.ElementTree import QName
# import numpy
# import scipy
def decode(w):
    r = ""
    for i in w:
        if (ord(i)<=ord('Z') and ord(i)>=ord('A')):
            r+= chr(((ord(i)-ord('A')%26)+14)%26+ord('A'))
        elif (ord(i)<=ord('z') and ord(i)>=ord('a')):
            r+= chr(((ord(i)-ord('a')%26)+14)%26+ord('a'))
        else:r+=i
    return r

res =""


a = input()

# print(a)
res = decode(a)

print(res)

# i = "U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad puzzqd."
# o = "I will be at the senate today to hear a petition from Tillius. Cassius and Brutus have been acting strange. Should be back in time for dinner."
# i = list(i)
# o = list(o)
# r = ord('I')%26 - ord('U')%26
# print(r)

# r = ord('w')%26 - ord('i')%26

# print(r)