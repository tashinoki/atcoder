
N = int(input())
s = 0
dominator = 10

if N % 2 == 0:

    while(N>=dominator):
        s += N // dominator
        dominator *= 5

print(s)