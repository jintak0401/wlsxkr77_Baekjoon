from sys import stdin

input = stdin.readline


def solve():
    R, C, M = map(int, input().split())
    length = R * C
    sharks = {}
    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        pos = (r - 1) * C + (c - 1)
        s %= 2 * (R - 1 if d <= 2 else C - 1)
        sharks[pos] = [s, d, z]

    def move_sharks():
        nxtSharks = {}
        for pos in sharks.keys():
            s, d, z = sharks[pos]

            if d <= 2:
                nxtPos = pos % C
                x = pos // C
                l = R
                mul = C
            else:
                nxtPos = (pos // C) * C
                x = pos % C
                l = C
                mul = 1
            _2l = l * 2

            if d == 1 or d == 4:
                if s <= x: nxtPos += mul * (x - s)
                elif s <= x + l - 1:
                    nxtPos += mul * (s - x)
                    d = 2 if d == 1 else 3
                else: nxtPos += mul * (_2l + x - 2 - s)

            else:
                if s <= l - 1 - x: nxtPos += mul * (x + s)
                elif s <= _2l - 2 - x:
                    nxtPos += mul * (_2l - x - s - 2)
                    d = 1 if d == 2 else 4
                else: nxtPos += mul * (s + x + 2 - _2l)

            if nxtPos not in nxtSharks or nxtSharks[nxtPos][2] < sharks[pos][2]:
                sharks[pos][1] = d
                nxtSharks[nxtPos] = sharks[pos]

        return nxtSharks

    def get_sharks(line):
        for i in range(line, length, C):
            if i in sharks:
                return i
        return -1

    ans = 0
    for i in range(C):
        pos = get_sharks(i)
        if pos != -1:
            ans += sharks[pos][2]
            del sharks[pos]
        sharks = move_sharks()

    return ans


if __name__ == '__main__':
    print(solve())
