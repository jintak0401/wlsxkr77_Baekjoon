from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())

    arr = [int(input()) for _ in range(N)]

    def init_tree():
        tree = [0] * (2 * N)
        tree[N:2*N] = arr
        for i in range(N - 1, 0, -1):
            l, r = i << 1, (i << 1) | 1
            tree[i] = tree[l] if tree[l] < tree[r] else tree[r]
        return tree

    inf = float('inf')
    def query(start, end):
        nonlocal tree
        ret = inf
        start += N
        end += N
        while start < end:
            if start & 1:
                if tree[start] < ret:
                    ret = tree[start]
                start += 1
            if end & 1:
                end -= 1
                if tree[end] < ret:
                    ret = tree[end]
            start >>= 1
            end >>= 1

        return ret

    tree = init_tree()
    for _ in range(M):
        a, b = map(int, input().split())
        print(query(a-1, b))


if __name__ == '__main__':
    solve()
