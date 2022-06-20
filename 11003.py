from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    N, L = map(int, input().split())
    arr = [*map(int, input().split())]
    ans = [0] * N

    que = deque()

    for i in range(L):
        while que and arr[i] < que[-1]:
            que.pop()
        que.append(arr[i])
        ans[i] = que[0]

    for i in range(L, N):
        while que and arr[i] < que[-1]:
            que.pop()
        que.append(arr[i])
        if que[0] == arr[i - L]:
            que.popleft()
        ans[i] = que[0]

    print(*ans)


if __name__ == '__main__':
    solve()
