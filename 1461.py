from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = sorted([0] + [*map(int, input().split())])

    pivot = bisect_left(arr, 0)
    ans = 0
    for i in range(0, pivot, M):
        ans += (-arr[i]) * 2

    for i in range(N, pivot, -M):
        ans += arr[i] * 2

    ans -= arr[N] if (-arr[0]) < arr[N] else (-arr[0])

    return ans


if __name__ == '__main__':
    print(solve())

