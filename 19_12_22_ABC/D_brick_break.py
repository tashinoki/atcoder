
n = int(input())
a = list(map(int, input().split()))
 
count = 1
k = 0       #break time
 
for i in range(n):
    if a[i] == count:
        count += 1
    else:
        k += 1
 
if k == n:
    k = -1
 
print(k)