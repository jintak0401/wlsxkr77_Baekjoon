from sys import stdin
from itertools import combinations

input = stdin.readline


def solve(N: int) -> int | str:
    N -= 1
    if N >= 1023:
        return -1

    for i in range(1, 11):
        combi = list(combinations('9876543210', i))[::-1]
        if N < len(combi):
            return ''.join(combi[N])
        else:
            N -= len(combi)


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
