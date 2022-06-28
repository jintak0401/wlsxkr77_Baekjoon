from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = [*map(int, input().split())]

    if N <= M:
        return N

    K = N // M
    if N % M == 0:
        K -= 1
    lo, hi = min(arr) * K, max(arr) * K

    while lo < hi:
        mid = (lo + hi) // 2
        if sum(mid // t + 1 for t in arr) < N:
            lo = mid + 1
        else:
            hi = mid

    return [i for i, t in enumerate(arr, 1) if lo % t == 0][N - 1 - sum(lo // t + 1 for t in arr)]


if __name__ == '__main__':
    print(solve())