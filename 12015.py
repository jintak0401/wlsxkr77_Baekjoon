from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    dp = [arr[0]]

    for i in range(1, N):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])] = arr[i]

    return len(dp)


if __name__ == '__main__':
    print(solve())
