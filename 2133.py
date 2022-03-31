from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    if N & 1:
        return 0

    N >>= 1
    dp = [0, 3] + [2] * (N - 1)
    for i in range(2, N + 1):
        dp[i] += 3 * dp[i-1]
        for j in range(2, i):
            dp[i] += 2 * dp[i-j]

    return dp[N]


if __name__ == '__main__':
    print(solve())
