from sys import stdin

input = stdin.readline

arr = []


def is_square(num: int) -> bool:
    sqrt = num ** 0.5
    return sqrt % 1 == 0


def solve(cur_pos: tuple = None, direction: tuple = None) -> int:
    r, c = cur_pos
    dr, dc = direction
    ret = -2
    cur_num = ''
    if dr == 0 and dc == 0:
        cur_num += arr[r][c]
        num = int(cur_num)
        return num if is_square(num) else -2

    while 0 <= r < row and 0 <= c < col:
        cur_num += arr[r][c]
        num = int(cur_num)
        if is_square(num) and num > ret:
            ret = num
        r += dr
        c += dc

    return ret


if __name__ == '__main__':
    row, col = map(int, input().split())
    for _ in range(row):
        arr.append(input()[:-1])
    ans = -1
    for r1 in range(row):
        for c1 in range(col):
            for r2 in range(row):
                for c2 in range(col):
                    ans = max(ans, solve(cur_pos=(r1, c1), direction=(r2 - r1, c2 - c1)))
    print(ans)
