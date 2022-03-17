from sys import stdin

input = stdin.readline


def solve():
    x, b = map(int, input().split())
    if b == 10 or x == 0:
        return x
    xm_bp = False
    bm = False
    if b > 0 and x < 0:
        xm_bp = True
        x *= -1
    elif b < 0:
        bm = True

    ans = []
    while not 0 <= x < abs(b):
        q, r = x // b, x % b
        if bm and r:
            q += 1
            r -= b
        x = q
        ans.append(r)

    if x:
        ans.append(x)

    ret = '-' if xm_bp else ''
    ret += ''.join(map(str, ans[::-1]))
    return ret


if __name__ == '__main__':
    print(solve())

