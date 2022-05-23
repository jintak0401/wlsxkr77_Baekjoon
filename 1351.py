from sys import stdin

input = stdin.readline


def solve():
    N, P, Q = map(int, input().split())

    dp = {}
    dp[0] = 1

    def dfs(n):
        if n in dp:
            return dp[n]
        dp[n] = dfs(n // P) + dfs(n // Q)
        return dp[n]

    return dfs(N)


if __name__ == '__main__':
    print(solve())
