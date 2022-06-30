from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    N, M, X = map(int, input().split())
    inf = 1_000_000_000
    # 노드들에서 X를 향한 그래프
    go = [[] for _ in range(N + 1)]
    # X에서 노드들을 향한 그래프
    back = [[] for _ in range(N + 1)]
    for _ in range(M):
        _from, _to, _dist = map(int, input().split())
        go[_from].append((_to, _dist))
        # X 에서 각 노드들을 향해 가는 것은
        # 노드들에서 X를 향해 가는 것의 역연산이므로
        # _from, _to를 바꾸어서 그래프에 넣어주어서
        # 같은 dijkstra 함수로 해결할 수 있다
        back[_to].append((_from, _dist))

    def dijkstra(graph):
        heap = [(0, X)]
        cost = [inf] * (N + 1)
        cost[X] = 0
        while heap:
            cur_cost, cur_pos = heappop(heap)
            if cost[cur_pos] < cur_cost:
                continue
            for nxt_pos, nxt_cost in graph[cur_pos]:
                if (total_cost := cur_cost + nxt_cost) < cost[nxt_pos]:
                    cost[nxt_pos] = total_cost
                    heappush(heap, (total_cost, nxt_pos))

        return cost[1:]

    return max(_go + _back for _go, _back in zip(dijkstra(go), dijkstra(back)))


if __name__ == '__main__':
    print(solve())
