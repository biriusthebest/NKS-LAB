import copy

connections = [

    [1],  # 0
    [2],  # 1
    [3, 4],  # 2
    [4, 5],  # 3
    [5, 6],  # 4
    [6, 7],  # 5
    [7, 8],  # 6
    [],  # 7
    [],  # 8

]

p = [0.16, 0.89, 0.96, 0.17, 0.43, 0.54, 0.20, 0.80, 0.76]


def get_table():
    k = []
    for c in range(2**len(p)):
        b = ''
        while c > 0:
           b = str(c%2)+b
           c = c//2
        while len(b) < len(p):
            b = '0'+b
        k.append(b)
    return k


def find_work(b):
    c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = []
    for i in range(len(b)):
        a.append([])
        for j in range(len(b[i])):
            if int(b[i][j]) == 1:
                a[i].append(c[j])
    return a


def look_correction(list, ins):
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] += 1
        if ins:
            list[i].insert(0, 1)
            paths_end[i].insert(0, 0)
    return list


def get_status(a, b):
    stat = []
    stat2 = []
    for i in a:
        for j in b:
            stat.append(j in i)
        k = False
        for j in stat:
            if j:
                k = True
        stat2.append(k)
        stat.clear()
    k = False
    for i in stat2:
        if not i:
            k = True
    return k


def pop_lust(a):
    i = 2
    while i < len(a):
        if a[i] in connections[a[i-2]]:
            a.pop(i-1)
        i += 1
    return a


def path_finder(r):
    global c
    if len(r) != 0:
        for i in r:
            paths.append(i)
            path_finder(connections[i])
        if len(paths) != 0:
            paths.pop(-1)

    else:
        paths_end.append(copy.deepcopy(paths))
        paths.pop(-1)


paths = []
paths_end = []
c = 1
path_finder(connections[0])
for i in paths_end:
    pop_lust(i)
c = 0
while c < len(paths_end):
    k = 0
    while k < len(paths_end):
        if c != k and paths_end[c] == paths_end[k]:
            paths_end.pop(k)
        k += 1
    c += 1
paths_copy = copy.deepcopy(paths_end)
paths_copy = look_correction(paths_copy, True)
print('Робочі шляхи =', paths_copy)
component_status = get_table()
all_components = find_work(component_status)
p_sum = 0
table = []
p_table= []
for i in range(len(all_components)):
    if get_status(paths_end, all_components[i]):
        p_tmp = 1
        table.append(component_status[i])
        for j in range(len(component_status[i])):
            if component_status[i][j] == '1':
                p_tmp *= 1 - p[j]
            else:
                p_tmp *= p[j]
        p_table.append(p_tmp)
        p_sum += p_tmp
print('P =', p_sum)
print(' E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |  E9 | P')
for i in range(len(table)):
    for j in table[i]:
        if j == '0':
            print('  + |', end='')
        else:
            print('  - |', end='')
    print('',p_table[i])