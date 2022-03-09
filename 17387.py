from sys import stdin

input = stdin.readline


def ccw(a, b, c):
    op = a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[1]*b[0] - b[1]*c[0] - c[1]*a[0]
    if op > 0:
        return 1
    elif op < 0:
        return -1
    else:
        return 0


def is_intersect(line1, line2):
    a, b = line1[0], line1[1]
    c, d = line2[0], line2[1]
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0


def solve():
    line1 = (*map(int, input().split()), )
    line2 = (*map(int, input().split()), )
    line1 = ((line1[0], line1[1]), (line1[2], line1[3]))
    line2 = ((line2[0], line2[1]), (line2[2], line2[3]))
    if is_intersect(line1, line2):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(solve())
