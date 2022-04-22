from sys import stdin

input = stdin.readline


def solve():
    C, N = map(int, input().split())

    arr = [[*map(int, input().split())] for _ in range(N)]

    dp = [0] * (C + 1)
    for target in range(1, C + 1):
        dp[target] = min(cost + dp[target-customer] if customer < target else cost
                         for cost, customer in arr)

    return dp[C]


if __name__ == '__main__':
    print(solve())
