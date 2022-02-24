from sys import stdin

input = stdin.readline


# pos: 현재 위치 / dest: 마지막으로 도착해야하는 도시 / bit: 방문했던 도시 비트 / visited: 방문했던 도시 set
def solve(n):

    inf = float('inf')
    cost = [0] * n
    for i in range(n):
        cost[i] = [*map(int, input().split())]

    # dp[도시][0번 도시를 제외한 visited_bit] = 최소거리
    # [도시]에서 출발하여 visited_bit에서 [도시]를 제외한 모든 도시를 거친 후 0번도시로 돌아간 비용
    # 1번도시 bit: 0 / 2번 도시 bit: 10 / 3번 도시 bit: 100
    dp = [[inf] * (1 << (n-1)) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not cost[i][j]:
                cost[i][j] = inf

    for i in range(1, n):
        dp[i][0] = cost[i][0]

    def get_min(pos, visited):
        ret = inf
        for city in range(1, n):
            # i번 도시에 해당하는 비트
            # ex) city = 2 --> 10(2)
            city_bit = 1 << (city - 1)
            if visited & city_bit:
                # ex) visited = 110(2) --> visited & (~city) = 100(2)
                # 뒤쪽 수식의 의미: pos에서 i번 도시를 거친 뒤
                # visited에서 i번 도시를 제외한 도시를 거친 후 0번도시로 돌아간 비용
                _cost = cost[pos][city] + dp[city][visited & (~city_bit)]
                if ret > _cost:
                    ret = _cost
        return ret

    for visited in range(1, len(dp[0]) - 1):
        for city in range(1, n):
            city_bit = 1 << (city - 1)
            if not city_bit & visited:
                dp[city][visited] = get_min(city, visited)

    return get_min(0, len(dp[0]) - 1)


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
