"""
Probliem Link: https://www.acmicpc.net/problem/18809
Solution Link: https://jintak0401.github.io/posts/boj-18809
"""
from sys import stdin
from itertools import combinations

input = stdin.readline


def solve():
    N, M, G, R = map(int, input().split())
    _len = N * M
    arr = [0] * _len
    idx = 0
    for i in range(N):
        arr[idx:idx+M] = [*map(int, input().split())]
        idx += M

    spot = [x for x, y in enumerate(arr) if y == 2]
    for pos in spot:
        arr[pos] = 1

    already = {}
    ans = 0
    for _spot in combinations(spot, G + R):
        _spot = set(_spot)
        for r_spot in combinations(_spot, R):
            tmp_g = tuple(_spot - set(r_spot))
            if R == G:
                if r_spot in already.get(tmp_g, []):
                    continue

                if r_spot not in already.keys():
                    already[r_spot] = set()
                already[r_spot].add(tmp_g)
            r_spot = [*r_spot]

            g_spot = list(tmp_g)
            _arr = [*arr]

            for r in r_spot:
                _arr[r] = 0

            for g in g_spot:
                _arr[g] = 0

            ans_val = 0
            step = 2

            while g_spot and r_spot:
                if g_spot:
                    new_g_spot = []
                    for g in g_spot:
                        if 0 <= _arr[g]:
                            x, y = g // M, g % M
                            adj = [g - M if 0 < x else -1,
                                   g + M if x < N - 1 else -1,
                                   g - 1 if 0 < y else -1,
                                   g + 1 if y < M - 1 else -1,
                                   ]
                            for nxt in adj:
                                if nxt != -1:
                                    if _arr[nxt] == 1:
                                        new_g_spot.append(nxt)
                                        _arr[nxt] = step
                    g_spot = new_g_spot

                if r_spot:
                    new_r_spot = []
                    for r in r_spot:
                        x, y = r // M, r % M
                        adj = [r - M if 0 < x else -1,
                               r + M if x < N - 1 else -1,
                               r - 1 if 0 < y else -1,
                               r + 1 if y < M - 1 else -1,
                               ]
                        for nxt in adj:
                            if nxt != -1:
                                if _arr[nxt] == step:
                                    ans_val += 1
                                    _arr[nxt] = -step
                                elif _arr[nxt] == 1:
                                    _arr[nxt] = -step
                                    new_r_spot.append(nxt)
                    r_spot = new_r_spot

                step += 1

            if ans < ans_val:
                ans = ans_val

    return ans


if __name__ == '__main__':
    print(solve())
