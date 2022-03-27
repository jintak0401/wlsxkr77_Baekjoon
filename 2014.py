from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():

    K, N = map(int, input().split())
    arr = [*map(int, input().split())]

    heap = [*arr]

    for _ in range(N - 1):
        val = heappop(heap)
        for p in arr:
            heappush(heap, val * p)
            if val % p == 0:
                break

    return heap[0]


if __name__ == '__main__':
    print(solve())
