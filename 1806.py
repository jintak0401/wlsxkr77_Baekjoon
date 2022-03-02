from sys import stdin


input = stdin.readline


def solve():
    N, S = map(int, input().split())
    arr = [*map(int, input().split())]
    inf = float('inf')
    left, _sum, ans = 0, 0, inf

    for right in range(N):
        _sum += arr[right]
        while _sum - arr[left] >= S:
            _sum -= arr[left]
            left += 1

        if _sum >= S and ans > right - left + 1:
            ans = right - left + 1

    return ans if ans != inf else 0


print(solve())
