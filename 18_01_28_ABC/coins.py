from pprint import pprint
five_handred = int(input())
handred = int(input())
fifty = int(input())

target = int(input())

count = 0

for i in range(min(five_handred, int(target/500)) + 1):

    y = target - 500 * i

    for j in range(min(handred, int(y/100)) + 1):

        z = y - 100 * j

        if int(z/50) <= fifty:
            count += 1

        else:
            pass

print(count)

# pprint({
#     "name": "kinoshita",
#     "age": 23
# })

# a,b,c,x=map(int,open(0))
# print(sum(500*i+100*j+50*k==x for i in range(a+1)for j in range(b+1)for k in range(c+1)))
