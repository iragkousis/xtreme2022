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
import numpy
import scipy

def recursive(phrase, n_id, info, yes_node, no_node, nodes_leaves_id, res):
    if n_id in nodes_leaves_id:
        res.append(info[n_id])
    elif info[n_id] in phrase:
        recursive(phrase, yes_node[str(n_id)],info, yes_node, no_node, nodes_leaves_id, res)
    else:
        recursive(phrase, yes_node[str(n_id)], info, yes_node, no_node, nodes_leaves_id, res)
        recursive(phrase, no_node[str(n_id)], info, yes_node, no_node, nodes_leaves_id, res)

n_nodes, phrases = input().split()
n_nodes = int(n_nodes)
phrases = int(phrases)

nodes_leaves_id = []
nodes_internal = []
root = []
nodes = []
info = {}
yes_node = {}
no_node = {}
for i in range(n_nodes):
    new_node = input().split()
    nodes.append(new_node)
    info[new_node[1]] = new_node[2]
    if new_node[0] == 'I':
        yes_node[new_node[1]] = new_node[3]
        no_node[new_node[1]] = new_node[4]
        root.append(new_node[1])
    else:
        nodes_leaves_id.append(new_node[1])

for i in nodes:
    if i[0] == 'I':
        if i[3] in root:
            root.remove(i[3])
        if i[4] in root:
            root.remove(i[4])

#print(yes_node[str(root[0])])

for p in range(phrases):
    phrase = input()
    res = []
    recursive(phrase, root[0], info, yes_node, no_node, nodes_leaves_id, res)
    res.sort()
    res = " ".join(res)
    print(res)