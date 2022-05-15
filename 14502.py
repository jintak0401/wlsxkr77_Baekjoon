from sys import stdin
from itertools import combinations

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    length = N * M
    arr = [0] * length
    for i in range(0, length, M):
        arr[i:i + M] = [*map(int, input().split())]

    blanks = []
    virus = []
    for i in range(length):
        if arr[i] == 0:
            blanks.append(i)
        elif arr[i] == 2:
            virus.append(i)

    not_wall = len(blanks) + len(virus) - 3
    ans = 0
    for blank in combinations(blanks, 3):
        que = virus.copy()
        brr = arr.copy()
        infection = 0
        for pos in blank:
            brr[pos] = 1
        while que:
            idx = que.pop()
            infection += 1
            r, c = idx // M, idx % M
            adj = [
                idx - M if 0 < r else -1,
                idx + M if r < N - 1 else -1,
                idx - 1 if 0 < c else -1,
                idx + 1 if c < M - 1 else -1
            ]
            for nxt in adj:
                if nxt != -1 and brr[nxt] == 0:
                    brr[nxt] = 2
                    que.append(nxt)

        cur = not_wall - infection
        if ans < cur:
            ans = cur

    return ans


if __name__ == '__main__':
    print(solve())
