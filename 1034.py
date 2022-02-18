from sys import stdin

input = stdin.readline

lamps: dict[str, int] = {}
toggle_time: int


def solve() -> int:
    ret = 0
    need_toggle_time: int

    for l in lamps.keys():
        need_toggle_time = l.count('0')
        if ((need_toggle_time - toggle_time) & 1) == 0 and need_toggle_time <= toggle_time:
            ret = max(ret, lamps[l])

    return ret


if __name__ == '__main__':
    row, col = map(int, input().split())
    for _ in range(row):
        l = input()
        lamps[l] = lamps.get(l, 0) + 1
    toggle_time = int(input())
    print(solve())
