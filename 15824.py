from sys import stdin

input = stdin.readline


def solve(N, arr):
    mod = 1_000_000_007
    if N == 1: return 0
    arr.sort()
    power = [1] * N
    power[0] = 0
    power[1] = 2
    for i in range(2, N):
        power[i] = (2 * power[i-1]) % mod
        power[i-1] -= 1
    power[-1] -= 1

    ans = 0
    for i in range(N // 2):
        ans = (ans + (power[tmp := N - 1 - i] - power[i]) * (arr[tmp] - arr[i])) % mod

    return ans


if __name__ == '__main__':
    print(solve())

