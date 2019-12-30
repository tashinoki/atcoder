
N, K = map(int, input().strip().split(" "))
R, S, P = map(int, input().strip().split(" "))
T = list(input())
action = [-1] * N
point = {
    "r": R,
    "s": S,
    "p": P
}

i = 0
start = 0
while(True):

    if not -1 in action:
        break

    try:
        index = start + i * K
        enemy_cmd = T[index]
        action(index).append

    except:
        start += 1
        i = 0
        continue