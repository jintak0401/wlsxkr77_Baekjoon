from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [0] * N
    inf = float('inf')
    for i in range(N):
        arr[i] = (*map(int, input().split()), )

    # dp[i][j] : i번째 행렬부터 j번째 행렬까지 곱셈 횟수의 최소값
    # dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i]의 row * arr[k]의 column * arr[j]의 column)
    dp = [[inf] * N for _ in range(N)]

    for i in range(N):
        dp[i][i] = 0

    for i in range(1, N):
        for j in range(N - i):
            a, b = j, i+j
            for k in range(a, b):
                dp[a][b] = min(dp[a][b], dp[a][k] + dp[k+1][b] + arr[a][0] * arr[k][1] * arr[i+j][1])

    return dp[0][N-1]


if __name__ == '__main__':
    print(solve())
