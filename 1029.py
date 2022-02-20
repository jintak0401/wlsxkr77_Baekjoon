from sys import stdin

input = stdin.readline

arr = []
dp = []
ans = 0
INF = float('inf')


def solve(owner: int = 0, price: int = 0, visited: int = 1):
    global ans

    for i in range(len(arr)):
        tmp = 1 << i

        # 이동 후 경로가 동일 경로의 이전가격보다 낮은 경우만 실행
        if (not visited & tmp) and price <= arr[owner][i] < dp[i][visited | tmp]:
            solve(i, arr[owner][i], visited | (1 << i))

    dp[owner][visited] = price

    # visited의 비트 중 1의 개수 세기
    ans = max(ans, bin(visited).count('1'))


if __name__ == '__main__':
    N = int(input())
    arr = [0] * N

    # dp[주인][경로] = 가격
    dp = [[INF] * (1 << N) for _ in range(N)]
    for i in range(N):
        arr[i] = tuple(map(int, list(input()[:-1])))

    solve()
    print(ans)
