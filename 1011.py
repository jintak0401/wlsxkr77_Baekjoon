from math import ceil
from sys import stdin

input = stdin.readline


def solve(diff):
    n = ceil((diff ** 0.5) - 1)
    if n * (n + 1) < diff:
        return 2 * n + 1
    else:
        return 2 * n


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        x, y = map(int, input().split())
        print(solve(y - x))
