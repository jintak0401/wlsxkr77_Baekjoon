from sys import stdin


input = stdin.readline

num: int
combi = [[0],
         [0, 1],
         [0, 2, 1],
         [0, 3, 3, 1],
         [0, 4, 6, 4, 1],
         [0, 5, 10, 10, 5, 1],
         [0, 6, 15, 20, 15, 6, 1],
         [0, 7, 21, 35, 35, 21, 7, 1],
         [0, 8, 28, 56, 70, 56, 28, 8, 1],
         [0, 9, 36, 84, 126, 126, 84, 36, 9, 1],
         [0, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
         ]
acc = [10, 55, 175, 385, 637, 847, 967, 1012, 1022, 1023]


def solve() -> int:
    global num

    if num < 10:
        return num
    elif num >= acc[-1]:
        return -1

    # 몇 자리 수인지 판별
    # 5 -> 0의 자리수 / 321 -> 2의 자리수
    digit = 0
    while True:
        if num < acc[digit]:
            break
        digit += 1

    ans = 0
    num -= acc[digit-1]
    for i in range(digit, 0, -1):
        val = i
        while True:
            if num >= combi[val][i]:
                num -= combi[val][i]
                val += 1
            else:
                ans = ans * 10 + val
                break

    ans = ans * 10 + num
    return ans


if __name__ == '__main__':
    num = int(input())
    print(solve())
