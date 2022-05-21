from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    N = int(input())
    arr = sorted((*map(int, input().split()),) for _ in range(N))
    arr = [arr[i][1] for i in range(N)]
    dp = [arr[0]]

    for i in range(1, N):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])] = arr[i]

    return N - len(dp)


if __name__ == '__main__':
    print(solve())
