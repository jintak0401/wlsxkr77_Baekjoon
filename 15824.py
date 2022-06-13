from sys import stdin

input = stdin.readline


def solve():
    mod = 1_000_000_007
    N = int(input())
    arr = [*map(int, input().split())]
    if N == 1: return 0
    arr.sort()
    power = [1] * N
    for i in range(1, N):
        power[i] = (2 * power[i-1]) % mod

    ans = 0
    for i in range(N // 2):
        ans = (ans + (power[tmp := N - 1 - i] - power[i]) * (arr[tmp] - arr[i])) % mod

    return ans


if __name__ == '__main__':
    print(solve())

