data = [565, 825, 876, 184, 1202, 524, 125, 69, 2,
        22, 35, 140, 717, 122, 38, 18, 132, 155, 16,
        741, 239, 412, 18, 29, 178, 322, 650, 246,
        110, 258, 3, 667, 92, 258, 412, 206, 138,
        309, 194, 189, 367, 397, 292, 33, 242, 644,
        493, 12, 154, 122, 121, 141, 1253, 73, 66,
        181, 332, 608, 424, 398, 623, 516, 329, 548,
        262, 1445, 110, 156, 145, 8, 906, 212, 67,
        452, 198, 150, 137, 64, 138, 255, 383, 234,
        525, 612, 211, 236, 246, 170, 192, 12, 691,
        1, 127, 51, 162, 232, 279, 5, 26, 1037]

gamma = 0.53
work_time = 1361
intensive = 451


def count_intervals(sd, inter, i):
    c = 0
    amount = 0
    while sd[c] < inter[i]:
        if i != 0:
            if sd[c] > inter[i-1]:
                amount += 1
        if i == 0:
            amount += 1
        c += 1
    return amount


def find_worktime(f, inter, w_t):
    c = 0
    p = 0
    while w_t > inter[c]:
        p += f[c]*inter[0]
        c += 1
    if c != len(f)-1:
        p += f[c+1]*(w_t-inter[c-1])
    return p


def find_last(inter, w_t):
    c = 0
    while w_t > inter[c]:
        c += 1
    return c


time_cp = sum(data)/len(data)
print('Tcp =', time_cp)
sorted_data = sorted(data)
print('sorted data =',sorted_data)
intervals = []
h = sorted_data[-1]/10
for i in range(10):
    intervals.append((sorted_data[-1]/10)*(i+1))
print('intervals = ',intervals)
f = []
for i in range(len(intervals)):
    f.append(count_intervals(sorted_data, intervals, i)/(len(sorted_data)*intervals[0]))
print('f =', f)
chance_of_work = [1]
for i in range(len(intervals)):
    chance_of_work.append(h*f[i])
print('chance of work =', chance_of_work)
d = []
for i in range(len(chance_of_work)-1):
    if chance_of_work[i+1] != chance_of_work[i]:
        d.append((chance_of_work[i+1]-gamma)/(chance_of_work[i+1]-chance_of_work[i]))
print('d =',d)
t_y = []
for i in range(len(d)):
    t_y.append(intervals[i]-intervals[i]*d[i])
print('t_y =', t_y[0])
last = find_last(intervals, intensive)
print('P =', 1 - find_worktime(f, intervals, work_time))
print('Lambda('+str(intensive)+') = '+str(f[last]/(1-find_worktime(f, intervals, intensive))))