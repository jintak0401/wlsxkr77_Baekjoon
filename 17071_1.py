"""
Probliem Link: https://www.acmicpc.net/problem/17071
Solution Link: https://jintak0401.github.io/posts/boj-17071
"""
from sys import stdin

input = stdin.readline


def solve():
    N, K = map(int, input().split())

    if N == K:
        return 0

    visited = [[0] * 500_001 for _ in range(2)]
    que = [N]
    K += 1
    ans, i = 1, 2
    while K <= 500_000:
        new_que = []
        is_odd = i & 1
        for pos in que:
            for p in [pos - 1, pos + 1, 2 * pos]:
                if 0 <= p <= 500_000 and not visited[is_odd][p]:
                    visited[is_odd][p] = ans
                    new_que.append(p)

        que = new_que

        if visited[is_odd][K]:
            return ans

        ans += 1
        K += i
        i += 1

    return -1


if __name__ == '__main__':
    print(solve())
