from sys import stdin
from itertools import combinations

input = stdin.readline


def solve():
    T = int(input())
    inf = float('inf')
    for _ in range(T):
        N = int(input())
        if N == 2:
            pt1 = (*map(int, input().split()), 2)
            pt2 = (*map(int, input().split()), 2)
            print(((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5)
        else:
            arr = [0] * N
            arr[0] = (*map(int, input().split()),)
            sum_x, sum_y = -arr[0][0], -arr[0][1]
            for i in range(1, N):
                arr[i] = (*map(int, input().split()),)
                sum_x += arr[i][0]
                sum_y += arr[i][1]

            def get_sum(start_pt):
                dx, dy = 0, 0
                for pt in start_pt:
                    dx += pt[0]
                    dy += pt[1]
                x, y = sum_x - 2*dx, sum_y - 2*dy
                return (x ** 2 + y ** 2) ** 0.5

            ans = inf

            for start_pt in combinations([arr[i] for i in range(1, N)], N//2 - 1):
                val = get_sum(start_pt)
                if val < ans:
                    ans = val
            print(ans)


if __name__ == '__main__':
    solve()
