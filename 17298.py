from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    stack = []
    ans = [-1] * N
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            ans[stack.pop()] = num
        stack.append(i)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solve()
