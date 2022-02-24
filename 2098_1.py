from sys import stdin
from math import inf

input = stdin.readline


# pos: 현재 위치 / dest: 마지막으로 도착해야하는 도시 / bit: 방문했던 도시 비트 / visited: 방문했던 도시 set
def solve(pos, dest, bit):
    global dp
    if dp[pos][bit]:
        return dp[pos][bit]

    # 모든 도시 방문
    elif bit == (1 << N) - 1:
        return arr[pos][dest] if arr[pos][dest] else inf

    ret = dp[pos][bit] if dp[pos][bit] else inf
    for city in range(N):
        if (not bit & (1 << city)) and arr[pos][city]:
            ret = min(ret, arr[pos][city] + solve(city, dest, bit | (1 << city)))

    dp[pos][bit] = ret
    return ret


if __name__ == '__main__':
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = [*map(int, input().split())]
    cities = set(i for i in range(N))
    # dp[현재위치][방문했던 도시 비트] = 거리
    dp = [[0] * (1 << N) for _ in range(N)]
    print(solve(0, 0, 1))
