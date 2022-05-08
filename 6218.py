from sys import stdin

input = stdin.readline


def solve():

    N, Q = map(int, input().split())

    arr = [int(input()) for _ in range(N)]

    def init_tree():
        _2N = 2 * N
        tree = [0] * _2N
        # 리프 노드를 입력 받은 수열로 할당
        tree[N:_2N] = [[arr[i], arr[i]] for i in range(N)]
        for i in range(N - 1, 0, -1):
            idx = 2 * i
            tree[i] = [
                tree[idx][0] if tree[idx][0] < tree[idx+1][0] else tree[idx+1][0],
                tree[idx][1] if tree[idx][1] > tree[idx+1][1] else tree[idx+1][1],
            ]

        return tree

    def query(start, end):
        _max, _min = -1, 1_000_001
        start += N
        end += N
        while start < end:
            if start % 2:
                if tree[start][0] < _min:
                    _min = tree[start][0]
                if tree[start][1] > _max:
                    _max = tree[start][1]
                start += 1
            if end % 2:
                end -= 1
                if tree[end][0] < _min:
                    _min = tree[end][0]
                if tree[end][1] > _max:
                    _max = tree[end][1]
            start //= 2
            end //= 2

        return _min, _max

    tree = init_tree()
    for _ in range(Q):
        a, b = map(int, input().split())
        minval, maxval = query(a - 1, b)
        print(maxval - minval)


if __name__ == '__main__':
    solve()
