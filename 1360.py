from sys import stdin

input = stdin.readline


def solve():

    N = int(input())

    arr = [input()[:-1].split() for _ in range(N)]

    for element in arr:
        if element[0] == 'undo':
            element[1] = int(element[1])
        element[2] = int(element[2])

    ans = ''
    until = arr[-1][2] + 1
    for i in range(len(arr) - 1, -1, -1):
        oper, a, time = arr[i]
        if time < until:
            if oper == 'type':
                ans += a
                until = time

            else:
                until = time - a

    return ans[::-1]


if __name__ == '__main__':
    print(solve())
