from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    T = int(input())
    inf = float('inf')
    for _ in range(T):
        N, M, K = map(int, input().split())
        arr = [[] for _ in range(N + 1)]
        for i in range(K):
            # u: 출발 / v: 도착 / c: 비용 / d: 시간
            u, v, c, d = map(int, input().split())
            # (시간, 비용, 도착)
            arr[u].append((d, c, v))

        if M == 0:
            print('Poor KCM')

        # (소요시간, 비용, 공항)
        que = deque([(0, 0, 1)])
        # visited[공항][비용] = 시간
        visited = [[inf] * (M + 1) for _ in range(N + 1)]

        while que:
            # c_ : current
            c_time, c_money, c_airport = que.popleft()

            if visited[c_airport][c_money] < c_time:
                continue

            # n_ : next
            for n_time, n_money, n_airport in arr[c_airport]:
                cost = c_money + n_money
                time = c_time + n_time
                if cost <= M and time < visited[n_airport][cost]:
                    for _cost in range(cost, M + 1):
                        if time < visited[n_airport][_cost]:
                            visited[n_airport][_cost] = time
                        else:
                            break
                    que.append((time, cost, n_airport))

        print(visited[N][M] if visited[N][M] != inf else 'Poor KCM')


if __name__ == '__main__':
    solve()
