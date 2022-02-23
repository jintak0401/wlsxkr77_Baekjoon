from sys import stdin

input = stdin.readline


def solve(arr):
    arr.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            height = arr[stack.pop()]
            width = i - stack[-1] - 1
            ans = max(ans, width * height)
        stack.append(i)
    return ans


if __name__ == '__main__':
    while True:
        n, *arr = map(int, input().split())
        if not n:
            break
        print(solve(arr))
