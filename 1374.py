from sys import stdin
from heapq import heappop, heappush

input = stdin.readline


def solve():
    N = int(input())
    classroom = [0]
    for start, end in sorted(tuple(map(int, input().split()))[1:] for _ in range(N)):
        if classroom[0] <= start:
            heappop(classroom)
        heappush(classroom, end)

    return len(classroom)


if __name__ == '__main__':
    print(solve())