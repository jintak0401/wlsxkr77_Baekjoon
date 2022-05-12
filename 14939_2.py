from sys import stdin

input = stdin.readline


def solve():
    ans = 101

    origin = []
    for i in range(10): origin.extend(input()[:-1])

    power = [0] * 11
    power[0] = 1
    for i in range(1, len(power)): power[i] = 2 * power[i-1]

    def hit(board, idx):
        r, c = idx // 10, idx % 10
        adjacent = [
            idx,
            idx - 10 if 0 < r else -1,
            idx + 10 if r < 9 else -1,
            idx - 1 if 0 < c else -1,
            idx + 1 if c < 9 else -1
        ]
        for adj in adjacent:
            if adj != -1:
                board[adj] = '#' if board[adj] == 'O' else 'O'

    for btn in range(power[10]):
        arr = [*origin]
        cnt = 0
        # 0번째 행 누르기
        for i in range(10):
            if btn & power[i]:
                cnt += 1
                hit(arr, i)

        # 1~9 행에서 윗 칸에 불이 켜져있으면 누르기
        for i in range(10, 100):
            if arr[i-10] == 'O':
                cnt += 1
                hit(arr, i)

        # 마지막(9) 행에 불이 켜져있으면 불가능
        if 'O' not in arr[90:] and cnt < ans:
            ans = cnt

    return ans if ans != 101 else -1


if __name__ == '__main__':
    print(solve())
