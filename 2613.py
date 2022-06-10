from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = [*map(int, input().split())]
    _max = max(arr)
    lo, hi = _max, sum(arr)

    def possible(val):
        cnt = 1
        acc = 0
        for num in arr:
            if acc + num <= val:
                acc += num
            else:
                cnt += 1
                acc = num

        return cnt <= M

    def divide(val):
        acc = 0
        cnt = 0
        m = M
        ret = []
        for i in range(N):
            if acc + arr[i] <= val:
                acc += arr[i]
                cnt += 1
            else:
                m -= 1
                acc = arr[i]
                ret.append(cnt)
                cnt = 1

            if N - i == m:
                break

        while m:
            ret.append(cnt)
            cnt = 1
            m -= 1

        return ret

    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            hi = mid - 1
        else:
            lo = mid + 1

    print(lo)
    print(*divide(lo))


if __name__ == '__main__':
    solve()

