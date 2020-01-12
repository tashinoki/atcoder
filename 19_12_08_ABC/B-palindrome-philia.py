S = list(input())

half = len(S) // 2
count = 0

before = S[:half]
after = S[-half:]

after.reverse()

for i, d in enumerate(before):

    if d != after[i]:
        count+=1

print(count)