from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    time = [0] * (N + 1)
    out_degree = [[] for _ in range(N + 1)]
    dp = [-1] * (N + 1)
    for i in range(1, N + 1):
        t, *need, _ = map(int, input().split())
        time[i] = t
        out_degree[i] = need
        if not need:
            dp[i] = t

    def dfs(node):
        if dp[node] != -1:
            return dp[node]

        dp[node] = max(dfs(nxt) for nxt in out_degree[node]) + time[node]
        return dp[node]

    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = dfs(i)

    print(*ans[1:], sep="\n")


if __name__ == '__main__':
    solve()
