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

# import scipy
N = get_number()
M = get_number()

arr = []
for i in range(N):
    arr.append(get_number())

if M == 1:
    sum = 0
    for j in range(N):
        sum += pow(2,arr[j],1000000007)
    print(sum % (10**9 + 7))
else:
    print(pow(2,max(arr),1000000007))