from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    dp = [arr[0]]
    indices = [0] * N

    for i in range(1, N):
        if arr[i] > dp[-1]:
            indices[i] = len(dp)
            dp.append(arr[i])
        else:
            idx = bisect_left(dp, arr[i])
            indices[i] = idx
            dp[idx] = arr[i]

    idx = len(dp) - 1
    for i in range(N - 1, -1, -1):
        if indices[i] == idx:
            dp[idx] = arr[i]
            idx -= 1

    print(len(dp))
    print(*dp)


if __name__ == '__main__':
    solve()
