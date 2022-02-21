from sys import stdin
from math import inf, isinf

input = stdin.readline

cost = []
dp = []
ans = 0
total = set()


def solve(status, alive):
    if dp[status] >= 0:
        return dp[status]

    elif len(alive) >= P:
        dp[status] = 0
        return 0

    val = inf

    # i -> 꺼져있는 발전소
    for i in total - alive:
        _cost = min(cost[j][i] for j in alive)
        val = min(val, _cost + solve(status | (1 << i), alive | {i}))

    dp[status] = val
    return val


if __name__ == '__main__':
    N = int(input())

    cost = [0] * N
    total = set(i for i in range(N))

    # 상태 -> 발전소가 켜져있는 곳을 1, 꺼져있는 곳을 0으로한 비트
    # dp[상태] = 현재 상태에서 추가적으로 드는 비용
    dp = [-1] * (1 << N)
    for i in range(N):
        cost[i] = list(map(int, input().split()))

    on = input().rstrip()
    alive = set()
    status = 0
    for i in range(len(on)):
        if on[i] == 'Y':
            alive.add(i)
            status |= (1 << i)
    P = int(input())

    # 켜져있는 발전소가 없는데 P > 0 이면 불가능하므로 -1 출력
    if len(alive) == 0 and P != 0:
        print(-1)
    else:
        ans = solve(status, alive)
        print(ans if not isinf(ans) else -1)
