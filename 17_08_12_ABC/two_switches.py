
A,B,C,D = map(int, input().split(" "))

if max(A ,C) <= min(B, D):
    print(min(B, D) - max(A, C))

else:
    print(0)