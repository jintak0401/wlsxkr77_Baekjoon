from sys import stdin

input = stdin.readline


def solve():
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    # dp[i번째 학생][서있는 학생들 bit]
    total_bit = 1 << N
    # 0이 아니라 -1로 초기화하는 이유는
    # 해당 케이스일 때 가능한 경우의 수가 0인 것과
    # 구분을 해주기 위함
    dp = [[-1] * total_bit for _ in range(N)]

    def dfs(idx, visited):
        if dp[idx][visited] > -1:
            return dp[idx][visited]

        elif visited == total_bit - 1:
            return 1

        ret = 0
        for nxt in range(N):
            if (bitmask := 1 << nxt) & visited == 0 and abs(arr[idx] - arr[nxt]) > K:
                ret += dfs(nxt, visited | bitmask)

        dp[idx][visited] = ret
        return ret

    ans = 0
    for i in range(N):
        ans += dfs(i, 1 << i)

    return ans


if __name__ == '__main__':
    print(solve())
