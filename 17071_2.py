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

    bound = int((-1 + (1 - 8 * (K - 500_000)) ** 0.5) / 2)
    max_pos = K + (bound * (bound + 1)) // 2
    ans = 1
    visited = [[0] * (max_pos + 1) for _ in range(2)]
    que = [N]
    for i in range(1, bound + 1):
        K += i
        new_que = []
        is_odd = i & 1
        for pos in que:
            # pos - 1
            p = pos - 1
            if 0 <= p and not visited[is_odd][p]:
                visited[is_odd][p] = ans
                new_que.append(p)

            # 2 * pos <= max_pos 인 경우, pos + 1 <= max_pos 이다
            p = 2 * pos
            if p <= max_pos:
                # 2 * pos
                if not visited[is_odd][p]:
                    visited[is_odd][p] = ans
                    new_que.append(p)

                # pos + 1
                p = pos + 1
                if not visited[is_odd][p]:
                    visited[is_odd][p] = ans
                    new_que.append(p)

            # pos + 1
            elif pos < max_pos and not visited[is_odd][pos + 1]:
                p = pos + 1
                visited[is_odd][p] = ans
                new_que.append(p)

        que = new_que

        if visited[is_odd][K]:
            return ans

        ans += 1

    return -1


if __name__ == '__main__':
    print(solve())
