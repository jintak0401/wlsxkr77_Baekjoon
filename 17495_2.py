from sys import stdin

input = stdin.readline


def solve():
    def convert(a):
        return conv[a[0]] + int(a[1]) * 12 + (len(a) == 3)

    def trace(x, y):
        if x == 0 and y == 0:
            return
        elif x - 1 == y:
            if y == 0:
                trace(0, 0)
                print('1', end=' ')
                return
            for i in range(y - 1, -1, -1):
                if dp[x][y] == dp[i][y] + abs(l[i] - l[x]):
                    trace(i, y)
                    print('1', end=' ')
                    return

        elif y - 1 == x:
            if x == 0:
                trace(0, 0)
                print('2', end=' ')
                return
            for i in range(x - 1, -1, -1):
                if dp[x][y] == dp[x][i] + abs(r[i] - r[y]):
                    trace(x, i)
                    print('2', end=' ')
                    return

        else:
            if x > y and l[x - 1] != r[y] and dp[x][y] == dp[x - 1][y] + abs(l[x] - l[x - 1]):
                trace(x - 1, y)
                print('1', end=' ')
                return
            elif y > x and dp[x][y] == dp[x][y - 1] + abs(r[y] - r[y - 1]):
                trace(x, y - 1)
                print('2', end=' ')
                return

    conv = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    _l, _r = map(convert, input().split())

    N = int(input())
    l, r = [0] * (N + 1), [0] * (N + 1)
    l[0], r[0] = _l, _r

    arr = [*map(convert, input().split())]
    l[1:] = r[1:] = arr
    dp = [[1e9] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N + 1):
        for j in range(N + 1):
            if i or j:
                if i - 1 == j:
                    if j == 0:
                        dp[i][j] = abs(l[1] - l[0])
                    else:
                        for k in range(j - 1, -1, -1):
                            val = dp[k][j] + abs(l[i] - l[k])
                            if val < dp[i][j]:
                                dp[i][j] = val

                elif j - 1 == i:
                    if i == 0:
                        dp[i][j] = abs(r[1] - r[0])
                    else:
                        for k in range(i - 1, -1, -1):
                            val = dp[i][k] + abs(r[j] - r[k])
                            if val < dp[i][j]:
                                dp[i][j] = val

                else:
                    if i > j:
                        val = dp[i - 1][j] + abs(l[i] - l[i - 1])
                        if val < dp[i][j]:
                            dp[i][j] = val
                    elif j > i:
                        val = dp[i][j - 1] + abs(r[j] - r[j - 1])
                        if val < dp[i][j]:
                            dp[i][j] = val

    a = min(dp[i][N] for i in range(N + 1))
    b = min(dp[N][i] for i in range(N + 1))
    ans = a if a < b else b
    print(ans)

    for i in range(N):
        if ans == dp[N][i]:
            trace(N, i)
            break
        elif ans == dp[i][N]:
            trace(i, N)
            break


if __name__ == '__main__':
    solve()
