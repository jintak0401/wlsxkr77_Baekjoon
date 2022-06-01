from sys import stdin


input = stdin.readline


def solve():
    N = int(input())
    K = int(input())

    lo, hi = 1, K
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0
        for i in range(1, (N if N < mid else mid) + 1):
            val = mid // i
            cnt += val if val < N else N

        if K <= cnt:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


if __name__ == '__main__':
    print(solve())
