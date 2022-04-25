from sys import stdin

input = stdin.readline


def solve():
    N, K = map(int, input().split())

    mod = N % K
    val = 10 ** len(str(N))

    for i in range(1, K + 1):
        if mod == 0:
            return i
        mod = (mod * val + N) % K

    return -1


if __name__ == '__main__':
    print(solve())
