
S = input()

words = ["dream", "erase", "dreamer", "eraser"]
index = 1

while(S):

    if index > len(S):
        print("NO")
        break

    if S[-index:] in words:

        S = S[:-index]
        index = 1
        continue

    index += 1

if not S:
    print("YES")

