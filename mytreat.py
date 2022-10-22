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
        try:
            return int(data)
        except ValueError:
            return float(data)
    except:
        pass
# numpy and scipy are available for use

cases = get_number()


for _ in range(cases):
    group = {}
    trans = get_number()
    for _ in range(trans):
        stri = input().split(' ')
        name = stri[0].replace('\r','')
        if name not in group:
            group[name] = 0
        group[name]-= int(stri[1])
        for name in stri[2:]:
            name = name.replace('\r','')
            if name not in group:
                group[name] = 0
            group[name] += 1
    meals = 0
    for name in group:

        meals += abs(group[name])
    # print(group)
    days = 10000000

    for name in group:
        if group[name] < days:
            days = group[name]
    print(meals//2, abs(days))


