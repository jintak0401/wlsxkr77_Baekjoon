from sys import stdin

input = stdin.readline


def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])


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


def find(disjoint_set, a):
    if disjoint_set[a] < 0:
        return a
    else:
        disjoint_set[a] = find(disjoint_set, disjoint_set[a])
        return disjoint_set[a]


def union(disjoint_set, x, y):
    x = find(disjoint_set, x)
    y = find(disjoint_set, y)
    if x == y:
        return
    elif disjoint_set[x] < disjoint_set[y]:
        disjoint_set[x] += disjoint_set[y]
        disjoint_set[y] = x
    else:
        disjoint_set[y] += disjoint_set[x]
        disjoint_set[x] = y


def solve():
    N = int(input())
    lines = [0] * N
    disjoint_set = [-1] * N
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        lines[i] = ((x1, y1), (x2, y2))
        for j in range(i):
            if is_intersect(lines[j], lines[i]):
                union(disjoint_set, i, j)

    biggest_group, count = 0, 0
    for i in range(N):
        if disjoint_set[i] < 0:
            count += 1
        if biggest_group > disjoint_set[i]:
            biggest_group = disjoint_set[i]
    return count, -biggest_group


if __name__ == '__main__':
    print(*solve(), sep='\n')
