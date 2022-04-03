from sys import stdin
from itertools import combinations as cb
from random import randrange
from math import gcd, prod

input = stdin.readline


def miller_rabin(n, a):
    d = n - 1
    while not d & 1:
        d >>= 1
        if pow(a, d, n) == n - 1:
            return True
    if pow(a, d, n) == 1:
        return True
    return False


def is_prime(n):
    small_prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    return n in small_prime or all(miller_rabin(n, a) for a in small_prime)


def solve():
    N = int(input())
    if 1 <= N <= 2:
        return 1
    elif is_prime(N):
        return N - 1

    primes = set()

    def pollard_rho(n):
        nonlocal primes
        if is_prime(n):
            return primes.add(n)
        # 2의 배수
        if not n & 1:
            primes.add(2)
            return pollard_rho(n // 2)

        x = y = randrange(2, n)
        c = randrange(1, n)
        d = 1
        while d == 1:
            x = ((x ** 2) % n + c) % n
            y = ((y ** 2) % n + c) % n
            y = ((y ** 2) % n + c) % n
            d = gcd(abs(x - y), n)
            if d == n:
                return pollard_rho(n)

        pollard_rho(n // d)
        pollard_rho(d)

    pollard_rho(N)
    ans = N
    for i in range(1, len(primes) + 1):
        val = sum(N // prod(combi) for combi in cb(primes, i))
        ans += -val if i & 1 else val

    return ans


if __name__ == '__main__':
    print(solve())
