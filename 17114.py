from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    len_arr = [*map(int, input().split())]
    width = len_arr[0]
    len_arr = [i for i in len_arr if i != 1]
    mul_len = [1] * (len(len_arr) + 1)
    for i in range(1, len(mul_len)): mul_len[i] = mul_len[i-1] * len_arr[i-1]
    arr = [0] * mul_len[-1]
    for i in range(0, mul_len[-1], width):
        arr[i:i+width] = input().split()

    que = deque(i for i in range(mul_len[-1]) if arr[i] == '1')
    cnt = arr.count('0')
    ans = 0

    while cnt and que:
        ans += 1
        for _ in range(len(que)):
            cur = remain = que.popleft()
            for i in range(len(len_arr) - 1, -1, -1):
                length, remain = remain // mul_len[i], remain % mul_len[i]
                if 0 < length and arr[(pos := cur - mul_len[i])] == '0':
                    que.append(pos)
                    arr[pos] = '1'
                    cnt -= 1
                if length < len_arr[i] - 1 and arr[(pos := cur + mul_len[i])] == '0':
                    que.append(pos)
                    arr[pos] = '1'
                    cnt -= 1

    return ans if cnt == 0 else -1


if __name__ == '__main__':
    print(solve())
