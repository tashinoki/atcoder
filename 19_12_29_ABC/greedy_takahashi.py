
A, B, K = map(int, input().strip().split(" "))
# print(A, B, K)

if A > K:
    A -= K
    K = 0

else:
    K -= A
    A = 0

if B > K:
    B -= K
    K = 0

else:
    B = 0
    
print("{} {}".format(A, B))