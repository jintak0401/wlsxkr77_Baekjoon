from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    N = int(input())
    wires = sorted((*map(int, input().split()), ) for _ in range(N))
    # a_wires_to[idx] = idx 번째로 작은 수의 A 전봇대 위치와 연결된 B 전봇대 위치
    a_wires_to = [0] * N
    # a_wires_order[idx] = idx 번째로 작은 수의 A 전봇대 위치
    a_wires_order = [0] * N
    for i in range(N):
        a, b = wires[i]
        a_wires_to[i] = b
        a_wires_order[i] = a

    indices = [0] * N
    dp = [a_wires_to[0]]
    for i in range(1, N):
        if a_wires_to[i] > dp[-1]:
            indices[i] = len(dp)
            dp.append(a_wires_to[i])
        else:
            idx = bisect_left(dp, a_wires_to[i])
            indices[i] = idx
            dp[idx] = a_wires_to[i]

    idx = len(dp) - 1
    jdx = N - len(dp) - 1
    ans = [0] * (jdx + 1)
    for i in range(N - 1, -1, -1):
        if indices[i] == idx:
            idx -= 1
        else:
            ans[jdx] = a_wires_order[i]
            jdx -= 1

    print(len(ans))
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
