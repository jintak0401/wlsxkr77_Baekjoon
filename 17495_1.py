"""
Probliem Link: https://www.acmicpc.net/problem/17495
Solution Link: https://jintak0401.github.io/posts/boj-17495
"""
from sys import stdin

input = stdin.readline


def solve():
    conv = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

    def convert(a):
        return conv[a[0]] + int(a[1]) * 12 + (len(a) == 3)

    l, r = map(convert, input().split())
    N = int(input())

    arr = [*map(convert, input().split())]

    # dp[i][l][r]: 위치 i에서 왼손과 오른손이 l과 r에 있을 때, 마지막까지 치는 거리 합
    dp = [[[-1] * 121 for _ in range(121)] for _ in range(N+1)]

    def calc(depth, left, right):
        if depth == N:
            return 0
        elif dp[depth][left][right] != -1:
            return dp[depth][left][right]

        _l = abs(arr[depth] - left) + calc(depth+1, arr[depth], right)
        _r = abs(arr[depth] - right) + calc(depth+1, left, arr[depth])

        dp[depth][left][right] = _l if _l < _r else _r

        return dp[depth][left][right]

    calc(0, l, r)
    print(dp[0][l][r])

    _l, _r = l, r
    for i in range(N):
        l_val = abs(_l - arr[i]) + dp[i+1][arr[i]][_r]
        r_val = abs(_r - arr[i]) + dp[i+1][_l][arr[i]]

        if l_val < r_val:
            _l = arr[i]
            print(1, end=' ')
        else:
            _r = arr[i]
            print(2, end=' ')


if __name__ == '__main__':
    solve()
