from sys import stdin
from heapq import heapreplace, heappush

input = stdin.readline


def solve():
    N = int(input())
    lecture = sorted(tuple(map(int, input().split())) for _ in range(N))
    classroom = [0]
    for start, end in lecture:
        if classroom[0] <= start:
            heapreplace(classroom, end)
        else:
            heappush(classroom, end)

    return len(classroom)


if __name__ == '__main__':
    print(solve())