"""
Probliem Link: https://www.acmicpc.net/problem/2842
Solution Link: https://jintak0401.github.io/posts/boj-2842
"""
from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    N_2 = N * N
    area = [0] * N_2
    height = [0] * N_2
    idx = 0
    for i in range(N):
        area[idx:idx+N] = [*input()[:-1]]
        idx += N

    idx = 0
    for i in range(N):
        height[idx:idx+N] = [*map(int, input().split())]
        idx += N

    p_pos = area.index('P')
    k_pos = [i for i in range(N_2) if area[i] == 'K']
    k_len = len(k_pos)
    fatigue = sorted(set(height))

    # _min: 'P'와 'K'의 높이중 최소 높이
    # _max: 'P'와 'K'의 높이중 최대 높이
    _min, _max = min(height[i] for i in k_pos), max(height[i] for i in k_pos)
    if height[p_pos] < _min:
        _min = height[p_pos]
    elif _max < height[p_pos]:
        _max = height[p_pos]

    def possible():
        low_bound, up_bound = fatigue[start], fatigue[end]

        # 'P'와 'K'가 있는 높이가 해당 범위가 아닌 경우 return False
        if not low_bound <= _min <= up_bound or not low_bound <= _max <= up_bound:
            return False

        que = [p_pos]
        visited = [False] * N_2
        visited[p_pos] = True
        cnt = 0
        while que:
            pos = que.pop()

            up, down = pos - N, pos + N
            r, c = pos // N, pos % N
            adj = [
                pos + 1 if c < N - 1 else -1,
                down if r < N - 1 else -1,
                down - 1 if r < N - 1 and 0 < c else -1,
                down + 1 if r < N - 1 and c < N - 1 else -1,
                up if 0 < r else -1,
                up - 1 if 0 < r and 0 < c else -1,
                up + 1 if 0 < r and c < N - 1 else -1,
                pos - 1 if 0 < c else -1,
            ]

            for nxt in adj:
                if nxt != -1 and not visited[nxt] and low_bound <= height[nxt] <= up_bound:
                    if area[nxt] == 'K':
                        cnt += 1
                        if cnt == k_len:
                            return True

                    visited[nxt] = True
                    que.append(nxt)

        return False

    start, end, ans = 0, 0, fatigue[-1] - fatigue[0]

    while start < len(fatigue):
        if possible():
            diff = fatigue[end] - fatigue[start]
            if diff < ans:
                ans = diff
            start += 1

        elif end < len(fatigue) - 1:
            end += 1

        else:
            break

    return ans


if __name__ == '__main__':
    print(solve())
