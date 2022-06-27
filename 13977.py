from sys import stdin

input = stdin.readline


def solve():
    mod = 1_000_000_007

    fact = [1] * 4_000_001
    for i in range(2, len(fact)):
        fact[i] = fact[i-1] * i % mod

    M = int(input())
    ans = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        ans[i] = fact[a] * (((fact[a-b] * fact[b] % mod) ** (-1)) % mod) % mod

    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
