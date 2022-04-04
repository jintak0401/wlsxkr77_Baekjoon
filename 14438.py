from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    M = int(input())
    inf = float('inf')

    tree = []

    def init_tree():
        nonlocal tree
        tree = [0] * (N << 1)
        tree[N: N << 1] = arr
        for i in range(N-1, 0, -1):
            idx = i << 1
            if tree[idx] < tree[idx | 1]:
                tree[i] = tree[idx]
            else:
                tree[i] = tree[idx | 1]

        return tree

    # [start, end) 범위의 최소를 구해준다
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

    def update(idx, val):
        idx += N
        tree[idx] = val
        while idx > 1:
            if tree[idx] < tree[idx ^ 1]:
                tree[idx >> 1] = tree[idx]
            else:
                tree[idx >> 1] = tree[idx ^ 1]
            idx >>= 1

    init_tree()
    # tree는 0-based 이어서 index에서 1씩 빼준다
    for _ in range(M):
        a, b, c = map(int, input().split())
        if a == 1:
            update(b-1, c)
        else:
            print(query(b-1, c))


if __name__ == '__main__':
    solve()
