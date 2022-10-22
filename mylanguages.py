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
class mynode :
    def __init__(self,dat,left,right):
        self.id = id
        self.dat = dat
        self.yes = left
        self.no = right
        self.type = 'node'
class myleaf :
    def __init__(self,Lang):
        self.id = id
        self.lang = Lang
        self.type= 'leaf'
nodn = get_number()
phrasen = get_number()

nodes = {}
inter = []
for i in range(nodn):
    stri = input().replace('\r','').split(' ')
    if (stri[0] == 'I'):
        nodes[stri[1]] = mynode(stri[2],stri[3],stri[4])
        inter.append(stri[3])
        inter.append(stri[4])
    else:
        nodes[stri[1]] = myleaf(stri[2])

root = 0
for i in nodes:
    if i not in inter:
        root = i
# print(f"root = {root}")
# print(inter)

def recursion(n,phrase):
    global languages
    if nodes[n].type == 'leaf':
        languages.add(nodes[n].lang)
        return
    if(nodes[n].dat in phrase):
        # print(f"{nodes[n].dat} not in {phrase}")
        recursion(nodes[n].yes,phrase)
    else:
        # print(f"{nodes[n].dat} not in {phrase}")
        recursion(nodes[n].yes,phrase)
        recursion(nodes[n].no,phrase)
# for n in nodes:
#     if nodes[n].type == 'node':
#         # print (f"{n}: {nodes[n].dat} {nodes[n].yes} {nodes[n].no}")
#     elif nodes[n].type == 'leaf':
#         # print (f"{n}: {nodes[n].lang}")
for _ in range(phrasen):
# u f b
    languages = set()
    recursion(root,input())
    languagesl = sorted(languages)
    print(' '.join(languagesl))

