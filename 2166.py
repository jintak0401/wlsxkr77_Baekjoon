from sys import stdin


input = stdin.readline


def solve():
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = (*map(int, input().split()), )

    ans = 0
    for i in range(-1, N - 1):
        ans += (arr[i][0] * arr[i+1][1]) - (arr[i+1][0] * arr[i][1])

    return round(abs(ans)/2, 1)


if __name__ == "__main__":
    print(solve())
