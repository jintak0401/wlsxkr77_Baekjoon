from sys import stdin

input = stdin.readline


def solve():
    N, C = map(int, input().split())
    arr = [*map(int, input().split())]

    w1, w2 = [0], [0]

    for w in arr[:N // 2]:
        tmp = [weight for x in w1 if (weight := x + w) <= C]
        w1 += tmp

    for w in arr[N // 2:]:
        tmp = [weight for x in w2 if (weight := x + w) <= C]
        w2 += tmp

    w1.sort()
    w2.sort()

    j = len(w2) - 1
    ans = 0
    for i in range(len(w1)):
        if j < 0: break
        while w1[i] + w2[j] > C: j -= 1
        ans += j + 1
    return ans


if __name__ == '__main__':
    print(solve())
