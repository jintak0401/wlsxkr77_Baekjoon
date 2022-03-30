from sys import stdin

input = stdin.readline


def solve():

    N = int(input())
    arr = [int(input()) for _ in range(N)] + [0]
    stack = [-1]
    ans = 0
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            height = arr[stack.pop()]
            width = i - stack[-1] - 1
            area = width * height
            if ans < area:
                ans = area
        stack.append(i)
    return ans


if __name__ == '__main__':
    print(solve())
