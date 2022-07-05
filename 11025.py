from sys import stdin

input = stdin.readline


def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(2, N + 1):
        ans = (ans + K) % i
    return ans + 1


if __name__ == '__main__':
    print(solve())
