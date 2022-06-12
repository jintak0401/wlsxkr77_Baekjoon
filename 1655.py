from sys import stdin
from heapq import heappush, heappushpop

input = stdin.readline


def solve():
    N = int(input())
    small, large = [], [int(input())]
    ans = [large[0]]
    for i in range(1, N):
        num = int(input())
        if i % 2:
            if num < large[0]:
                heappush(small, -num)
            else:
                heappush(small, -heappushpop(large, num))
            ans.append(-small[0])
        else:
            if num > -small[0]:
                heappush(large, num)
            else:
                heappush(large, -heappushpop(small, -num))
            ans.append(large[0])

    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()

