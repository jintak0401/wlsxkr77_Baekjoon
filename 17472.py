from sys import stdin
from heapq import heappush, heappop

_input = stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(ox, oy, num):
        arr[ox][oy] = num
        land[num].append((ox, oy))
        for dx, dy in d:
            x, y = ox + dx, oy + dy
            if 0 <= x < N and 0 <= y < M and arr[x][y] == 1:
                dfs(x, y, num)

    land, land_num = {}, 2
    # 땅 그룹짓기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                land[land_num] = []
                dfs(i, j, land_num)
                land_num += 1

    total_land = land_num - 2

    # for_mst[land1] = {land1과 연결된 땅: 다리길이}
    for_mst = {}
    inf = float('inf')
    for land_num, land_pt in land.items():
        for_mst[land_num] = {}
        for ox, oy in land_pt:
            for dx, dy in d:
                x, y = ox + dx, oy + dy
                flag, target_num = False, 0
                while 0 <= x < N and 0 <= y < M:
                    if arr[x][y] == land_num:
                        break
                    elif arr[x][y] != 0:
                        flag, target_num = True, arr[x][y]
                        break
                    x, y = x + dx, y + dy

                if flag:
                    dist = abs(x - ox + y - oy) - 1
                    if 1 < dist < for_mst[land_num].get(target_num, inf):
                        for_mst[land_num][target_num] = dist

    ans, heap, connected = 0, [], set([2])
    for land_num, dist in for_mst[2].items():
        heappush(heap, (dist, 2, land_num))

    while heap:
        # 거리, 이미 연결된 땅, 새로 연결될 땅
        dist, a, b = heappop(heap)
        if b not in connected:
            ans += dist
            connected.add(b)
            for land_num, d in for_mst[b].items():
                heappush(heap, (d, b, land_num))

    return ans if len(connected) == total_land else -1


if __name__ == '__main__':
    print(solve())
