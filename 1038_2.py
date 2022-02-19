from sys import stdin
from itertools import combinations


input = stdin.readline

num: int


def solve() -> int | str:
    global num
    if num < 10:
        return num
    elif num >= 1023:
        return -1
    for i in range(1, 11):
        num_list = list(combinations('9876543210', i))[::-1]
        if num < len(num_list):
            return ''.join(num_list[num])
        else:
            num -= len(num_list)
    return -1


if __name__ == '__main__':
    num = int(input())
    print(solve())
