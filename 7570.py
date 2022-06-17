from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    length = [0] * (N + 1)

    for num in arr:
        length[num] = length[num - 1] + 1

    return N - max(length)


if __name__ == '__main__':
    print(solve())

