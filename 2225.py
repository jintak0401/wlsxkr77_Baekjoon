from sys import stdin

input = stdin.readline


def solve():
    mod = 1_000_000_000
    N, K = map(int, input().split())
    arr = [1] + [0] * N

    for _ in range(1, K + 1):
        for i in range(1, N + 1):
            arr[i] = (arr[i] + arr[i-1]) % mod

    return arr[-1]


if __name__ == '__main__':
    print(solve())
