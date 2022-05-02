from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]

    arr.sort(key=lambda x: (-x[1], x[0]))

    done = [0] * 1000
    ans = 0

    for d, w in arr:
        for i in range(d-1, -1, -1):
            if done[i] == 0:
                done[i] = w
                ans += w
                break

    return ans


if __name__ == '__main__':
    print(solve())
