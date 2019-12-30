
n, a, b = map(int, input().strip().split(" "))

print(sum(i for i in range(1, n+1) if a <= sum(map(int, list(str(i)))) <= b))

# n, a, b = map(int, input().strip().split(" "))
 
# total = 0
 
# for i in range(n):
 
#     sum = 0
#     for j in str(i + 1):
 
#         sum += int(j)
 
#     if sum >= a and sum <= b:
#         total += (i + 1)
 
 
# print(total)