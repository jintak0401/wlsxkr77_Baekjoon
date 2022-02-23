from sys import stdin

input = stdin.readline

mod = 1_000_000_000


def solve(n):
    # dp[시작수][사용한 숫자들의 비트] = 개수
    dp = [[0] * (1 << 10) for _ in range(10)]

    for i in range(1, 10):
        dp[i][1 << i] = 1

    for length in range(2, n + 1):
        next_dp = [[0] * (1 << 10) for _ in range(10)]
        for i in range(10):
            for j in range(1, (1 << 10)):
                if i > 0:
                    next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i-1][j]) % mod
                if i < 9:
                    next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i+1][j]) % mod

        dp = next_dp

    ans = 0
    for i in range(10):
        ans = (ans + dp[i][(1 << 10) - 1]) % mod
    return ans


if __name__ == '__main__':
    N = int(input())
    if N < 10:
        print(0)
    else:
        print(solve(N))
