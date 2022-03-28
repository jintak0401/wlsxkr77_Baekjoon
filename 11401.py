from sys import stdin

input = stdin.readline


def solve():
    N, K = map(int, input().split())
    if K == 0:
        return 1

    mod = 1_000_000_007

    def euclidean(x, y):
        q = []
        while y:
            q.append(x // y)
            (x, y) = (y, x % y)

        q.pop()

        a, b = 0, 1
        for i in q[::-1]:
            (a, b) = (b, a - i*b)

        return a

    if K > N - K:
        K = N - K

    top, bot = N, 1
    N += 1
    for i in range(2, K+1):
        top = top * (N-i) % mod
        bot = bot * i % mod

    val = euclidean(bot, mod)
    return top * val % mod


if __name__ == '__main__':
    print(solve())
