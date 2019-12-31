
N, K = map(int, input().strip().split(" "))
R, S, P = map(int, input().strip().split(" "))
T = list(input())

point = {
    "r": P,
    "s": R,
    "p": S
}

score = 0

for i in range(N):

    tmp = i - K
    if 0 <= tmp and T[i] == T[tmp]:
        score += 0
        T[i]=""

    else:
        score+= point[T[i]]
print(score)
