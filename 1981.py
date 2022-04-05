from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [0] * (N * N)
    for i in range(N):
        arr[N*i: N*(i+1)] = [*map(int, input().split())]

    _min, _max = min(arr), max(arr)

    def adj(pos):
        r, c = pos // N, pos % N
        if 0 < r:
            yield pos - N
        if r < N - 1:
            yield pos + N
        if 0 < c:
            yield pos - 1
        if c < N - 1:
            yield pos + 1

    def possible(diff):
        for m in range(_min, _max - diff + 1):
            low_bound, up_bound = m, m + diff
            if low_bound <= arr[0] <= up_bound and low_bound <= arr[-1] <= up_bound:
                que = [0]
                visited = [False] * len(arr)
                visited[0] = True

                while que:
                    pos = que.pop()

                    for nxt in adj(pos):
                        if not visited[nxt] and low_bound <= arr[nxt] <= up_bound:
                            if nxt == len(arr) - 1:
                                return True
                            visited[nxt] = True
                            que.append(nxt)

        return False

    start, end = 0, _max - _min
    while start < end:
        mid = (start + end) // 2
        if possible(mid):
            end = mid

        else:
            start = mid + 1

    return end


if __name__ == '__main__':
    print(solve())
