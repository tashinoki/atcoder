
from collections import deque

H, W = map(int, input().split(" "))
maze = [ list(input()) for _ in range(H)]

def calc(sh, sw):

    dist = [[float('inf')] * W for i in range(H)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    dist[sh][sw] = 0

    que = deque([[sh, sw]])
    
    # ある地点から全マスまでの距離を計算
    while que:

        sh, sw = que.pop()

        for dh, dw in directions:

            # 迷路の枠外
            if not((0 <= sh + dh < H) and (0 <= sw + dw < W)):
                continue

            # 壁チェック
            if maze[sh + dh][sw + dw] == "#":
                continue

            # 経路の探索積みチェック
            if dist[sh + dh][sw + dw] != float("inf"):
                continue

            # 基準点をxとすると、そこから到達可能な点にx+1を割り当てる
            dist[sh + dh][sw + dw] = dist[sh][sw] + 1
            que.appendleft([sh + dh, sw + dw])

    ret = 0

    for d in dist:

        for w in range(W):

            # 壁に阻まれて到達できなかった領域
            if d[w] == float("inf"):
                continue
            ret = max(ret, d[w])
    return ret

ans = 0

for sh in range(H):
    
    for sw in range(W):

        if maze[sh][sw] == "#":
            continue

        ans = max(ans, calc(sh, sw))

print(ans)