from sys import stdin
from bisect import bisect_left


input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    dp = [arr[0]]

    for num in arr[1:]:
        if dp[-1] < num:
            dp.append(num)
        else:
            dp[bisect_left(dp, num)] = num

    return len(dp)


if __name__ == '__main__':
    print(solve())
