N = int(input())

# -1を初期値にして0と1を管理する
sg = [[-1 for i in range(N)] for j in range(N)]

for i in range(N):
  M = int(input())
  for j in range(M):
    x, y = map(int, input().split())
    sg[i][x-1] = y

X = 2**N
H = []

# ビット探索
for i in range(X):
  L = []

#   2進数の桁を表す
# 桁数はNである
  for j in range(N):
    L.append(i%2)
    i //= 2

  mj = 0
  for j in range(N):
    if L[j] == 1:
      for k in range(N):
        if j != k and (sg[j][k] == 0 and L[k] == 1 or sg[j][k] == 1 and L[k] == 0):
          mj += 1
          break
    if mj >= 1:
      break
  if mj >= 1:
    H.append(0)
  else:
    H.append(sum(L))
print(max(H))
