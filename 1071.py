from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = sorted([*map(int, input().split())])
    i = 1

    while i < N:
        if arr[i] == arr[i-1] + 1:
            start, end = i-1, i+1
            while start >= 1 and arr[start-1] == arr[i-1]:
                start -= 1
            while end < N and arr[end] == arr[i]:
                end += 1
            if end == N:
                arr[start:end] = [arr[i]] * (end - i) + [arr[i-1]] * (i - start)
                i = end
            else:
                arr[i], arr[end] = arr[end], arr[i]
                i = end + 1
        else:
            i += 1

    print(*arr)


if __name__ == '__main__':
    solve()
