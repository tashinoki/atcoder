import math
N = int(input().strip())

# 素数判定プログラム
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

while(True):

    if is_prime(N):
        print(N)
        break

    else:
        N += 1