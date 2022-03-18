from sys import stdin
from heapq import heappop, heappush

input = stdin.readline


def solve():
    N, M, K = map(int, input().split())
    road = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        road[a].append((b, c))
        road[b].append((a, c))

    inf = float('inf')
    # (현재 도시까지 온 비용, 현재 도시, 도로포장을 한 횟수)
    heap = [(0, 1, 0)]

    # dp 리스트를 1차원 배열로 하면 얼마나 빨라질까라는 생각에 해봅니다
    dp = [inf] * (K + 1) * (N + 1)
    dp[K + 1] = 0

    while heap:
        cur_cost, cur_city, count = heappop(heap)
        if cur_cost > dp[(K + 1) * cur_city + count]:
            continue

        for next_city, next_cost in road[cur_city]:
            # 도로포장을 하는 경우
            dp_idx = (K + 1) * next_city + count + 1
            if count < K and cur_cost < dp[dp_idx]:
                dp[dp_idx] = cur_cost
                heappush(heap, (cur_cost, next_city, count + 1))

            # 도로포장을 안하는 경우
            dp_idx -= 1
            total_cost = cur_cost + next_cost
            if total_cost < dp[dp_idx]:
                dp[dp_idx] = total_cost
                heappush(heap, (total_cost, next_city, count))

    return min(dp[N * (K + 1):])


if __name__ == '__main__':
    print(solve())

