from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]

    if N == 1:
        return 'A'

    elif N == 2:
        if arr[0] == arr[1]:
            return arr[0]
        else:
            return 'A'

    else:
        a = 1
        if arr[0] != arr[1]:
            a = (arr[2] - arr[1]) // (arr[1] - arr[0])
        b = arr[1] - a * arr[0]
        for i in range(2, N):
            if a * arr[i-1] + b != arr[i]:
                return 'B'

        return a * arr[-1] + b


if __name__ == '__main__':
    print(solve())
