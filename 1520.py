from sys import stdin, setrecursionlimit as SRL
SRL(100_000)

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    length = N * M
    arr = [0] * length
    idx = 0
    for _ in range(N):
        arr[idx:idx+M] = [*map(int, input().split())]
        idx += M

    dp = [-1] * length

    def dfs(cur):
        if dp[cur] != -1:
            return dp[cur]

        val = 0
        r, c = cur // M, cur % M
        adj = [
            cur - M if 0 < r else -1,
            cur + M if r < N - 1 else -1,
            cur - 1 if 0 < c else -1,
            cur + 1 if c < M - 1 else -1,
        ]
        for nxt in adj:
            if nxt != -1 and arr[nxt] < arr[cur]:
                if nxt == length - 1:
                    val += 1
                else:
                    val += dfs(nxt)

        dp[cur] = val
        return dp[cur]

    dfs(0)
    return dp[0]


if __name__ == '__main__':
    print(solve())
