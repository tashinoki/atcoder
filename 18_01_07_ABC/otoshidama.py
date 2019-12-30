
N, total = map(int, input().strip().split(" "))
bills = [-1, -1, -1]

for i in range(int(total/10000)+1):

    x = total - 10000*i

    for j in range(int(x/5000)+1):

        y = x-5000*j

        k = N - i -j

        if y-1000*k == 0:
    
            bills = [i, j, k]
            break

print(" ".join(map(str, bills)))


# osatsu, okane = map(int, input().split())
 
#1万円の枚数 : x
#5千円の枚数 : y
#千円の枚数  : z
 
# x_max = okane // 10000
 
# for x in range(x_max + 1):
#     z_max = (okane // 1000)
#     tmp = z_max - osatsu - 9 * x
#     if tmp % 4 != 0 or tmp < 0:
#         continue
#     y = tmp // 4
#     z = osatsu - x - y
#     if z < 0:
#         continue
 
#     print(x,y,z)
#     break
# else:
#     print(-1, -1, -1)
