# 最小公倍数を求める
A, B = [int(i) for i in input().split(" ")]
i = 1
while(True):

    if A*i % B ==0:
        print(A*i)
        break

    i += 1
