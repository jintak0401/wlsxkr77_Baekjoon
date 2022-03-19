from sys import stdin
from itertools import accumulate


input = stdin.readline


def solve():
    N, M = map(int, input().split())

    m_inf = -float('inf')
    dp = [*accumulate(map(int, input().split()))]
    for _ in range(N - 1):
        line = (*map(int, input().split()), )
        # 이전 칸 (왼쪽으로부터 오는경우면 왼쪽 칸, 오른쪽으로부터 오는 경우면 오른쪽 칸, 양 끝칸일 경우 -inf)
        prev = m_inf
        # l_dp[i]: (i-1)번째 칸(왼쪽)과 위에서 내려오는 것을 비교하여 더 큰 값
        # r_dp[i]: (i+1)번째 칸(오른쪽)과 위에서 내려오는 것을 비교하여 더 큰 값
        l_dp, r_dp = [0] * M, [0] * M
        for i, val in enumerate(dp):
            l_dp[i] = prev = max(prev, val) + line[i]
        prev = m_inf
        for i, val in reversed([*enumerate(dp)]):
            r_dp[i] = prev = max(prev, val) + line[i]

        dp = [max(l_dp[i], r_dp[i]) for i in range(M)]

    return dp[M-1]


if __name__ == '__main__':
    print(solve())

