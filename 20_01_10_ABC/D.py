
N, M = map(int, input().split(" "))

a = list(set(map(int, input().split(" "))))
g = a.copy()

while not any(x%2 for x in g): g = [i //2 for i in g]

if not all(x%2 for x in g): print(0); exit(0)

def gcd(a, b):

    while b:

        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


tot = 1

for x in a: tot = lcm(tot, x//2)
print((M//tot+1)//2)

# s = a[0]
# for i in range(1, len(a)):
#     s = s * a[i] // math.gcd(s, a[i])

# if s > M:
#     print(0)

# else:
#     m = s // 2
#     print((M-m)//s + 1)

# s = []
# step = 1

# def division(a, step):
#     flag = True
#     for i in a:
#         # print(step)
#         f = str(step / i).split(".")[1]
#         if f != "5":
#             flag = False
#             break

#     # print(step, flag)
#     return flag


# while(len(s) != 2):

#     if step > M:
#         print(0)
#         sys.exit()

#     if division(a, step):
#         s.append(step)
#     step += 2

# print(s)
# d = s[1] - s[0]

# print(2+(M-s[1])//d)