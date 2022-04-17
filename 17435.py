"""
Probliem Link: https://www.acmicpc.net/problem/17435
Solution Link: https://jintak0401.github.io/posts/boj-17435
"""
from sys import stdin

input = stdin.readline


def solve():
    m = int(input())

    # log2(500_000) + 1 = 19
    length = 19

    # move[i][j]: f_2^i(j)
    move = [[0] * (m + 1) for _ in range(length)]
    move[0][1:m+1] = [*map(int, input().split())]

    for i in range(1, length):
        for j in range(1, m + 1):
            move[i][j] = move[i-1][move[i-1][j]]

    Q = int(input())
    for _ in range(Q):
        n, x = map(int, input().split())
        idx = 0
        while (1 << idx) <= n:
            if n & (1 << idx):
                x = move[idx][x]
            idx += 1
        print(x)


if __name__ == '__main__':
    solve()
