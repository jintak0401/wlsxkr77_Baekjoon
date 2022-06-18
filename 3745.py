from sys import stdin
from bisect import bisect_left

input_lines = stdin.readlines


def solve():
    N = 0
    for line in input_lines():
        if N == 0:
            N = int(line)
        else:
            arr = [*map(int, line.split())]
            dp = [arr[0]]
            for num in arr[1:]:
                if dp[-1] < num:
                    dp.append(num)
                else:
                    dp[bisect_left(dp, num)] = num
            print(len(dp))
            N = 0


if __name__ == '__main__':
    solve()
