from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    N, M, H = map(int, input().split())
    floor = N * M
    total_len = floor * H
    arr = [0] * total_len
    for i in range(0, total_len, N):
        arr[i:i+N] = input().split()

    que = deque(i for i in range(total_len) if arr[i] == '1')
    cnt = arr.count('0')
    ans = 0

    while cnt and que:
        ans += 1
        for _ in range(len(que)):
            cur = que.popleft()
            h, remain = cur // floor, cur % floor
            r, c = remain // N, remain % N
            if 0 < r and arr[(pos := cur - N)] == '0':
                que.append(pos)
                arr[pos] = '1'
                cnt -= 1
            if r < M - 1 and arr[(pos := cur + N)] == '0':
                que.append(pos)
                arr[pos] = '1'
                cnt -= 1
            if 0 < c and arr[(pos := cur - 1)] == '0':
                que.append(pos)
                arr[pos] = '1'
                cnt -= 1
            if c < N - 1 and arr[(pos := cur + 1)] == '0':
                que.append(pos)
                arr[pos] = '1'
                cnt -= 1
            if 0 < h and arr[(pos := cur - floor)] == '0':
                que.append(pos)
                arr[pos] = '1'
                cnt -= 1
            if h < H - 1 and arr[(pos := cur + floor)] == '0':
                que.append(pos)
                arr[pos] = '1'
                cnt -= 1

    return ans if cnt == 0 else -1


if __name__ == '__main__':
    print(solve())
