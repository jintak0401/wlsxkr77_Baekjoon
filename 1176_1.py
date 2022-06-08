from sys import stdin

input = stdin.readline


def solve():
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    # dp[i번째 학생][서 있는 학생들 bit]
    total_bit = 1 << N
    dp = [[0] * total_bit for _ in range(N)]

    for i in range(N):
        dp[i][1 << i] = 1

    # 이미 서있는 학생들 bit
    for i in range(1, total_bit):
        # j: 앞에 서는 학생
        for j in range(N):
            # k: 뒤에 서는 학생
            for k in range(N):
                if i & (tmp := (1 << k)) == 0 and abs(arr[j] - arr[k]) > K:
                    dp[k][i | tmp] += dp[j][i]

    return sum(dp[i][-1] for i in range(N))


if __name__ == '__main__':
    print(solve())
