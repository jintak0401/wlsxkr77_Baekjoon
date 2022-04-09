"""
Probliem Link: https://www.acmicpc.net/problem/1194
Solution Link: https://jintak0401.github.io/posts/boj-1194
"""

from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    _len = N * M
    arr = [0] * _len
    for i in range(N):
        idx = i * M
        arr[idx:idx+M] = input()[:-1]

    start = arr.index('0')

    def adj(pos):
        r, c = pos // M, pos % M
        if 0 < r and arr[pos-M] != '#':
            yield pos-M
        if r < N - 1 and arr[pos+M] != '#':
            yield pos+M
        if 0 < c and arr[pos-1] != '#':
            yield pos-1
        if c < M - 1 and arr[pos+1] != '#':
            yield pos+1

    visited = [[False] * 64 for _ in range(_len)]

    # (pos, key)
    que = [(start, 0)]
    visited[start][0] = True

    ans = 1
    while que:
        new_que = []
        for pos, org_key in que:
            for nxt in adj(pos):
                cell = ord(arr[nxt])
                key = org_key

                # 문인 경우
                if 65 <= cell <= 70:
                    # 해당하는 열쇠가 없는 경우
                    if not key & (1 << (cell - 65)):
                        continue

                # 키인 경우
                elif 97 <= cell <= 102:
                    key |= 1 << (cell - 97)

                # '1'인 경우
                elif cell == 49:
                    return ans

                if not visited[nxt][key]:
                    visited[nxt][key] = True
                    new_que.append((nxt, key))

        que = new_que
        ans += 1

    return -1


if __name__ == '__main__':
    print(solve())
