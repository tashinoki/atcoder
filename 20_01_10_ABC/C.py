import itertools

N = int(input())

permu = [i+1 for i in range(N)]
s = 0
flag = False

P = tuple([int(i) for i in input().split(" ")])
Q = tuple([int(i) for i in input().split(" ")])

if P==Q:
    print(s)
else:
    for i, value in enumerate(itertools.permutations(permu)):

        if value == P or value == Q:
            # print(i)
            if flag:
                s -= i
                break
            else:
                s += i
                flag = True

    print(abs(s))

