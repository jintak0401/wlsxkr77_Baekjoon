from sys import stdin

input = stdin.readline


def find_max_index(arr: list[int], _from: int, S: int):
    tmp = arr[_from : min(_from + S + 1, len(arr))]
    return tmp.index(max(tmp)) + _from


def solve():
    _ = int(input())
    arr = list(map(int, input().split()))
    S = int(input())
    cur = 0
    while cur != len(arr) and S != 0:
        idx = find_max_index(arr, cur, S)
        if cur != idx:
            S -= (idx - cur)
            arr.insert(cur, arr.pop(idx))
        cur += 1

    print(*arr)


if __name__ == '__main__':
    solve()
