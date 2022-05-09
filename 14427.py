from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    M = int(input())
    inf = float('inf')

    def init_tree():
        _2N = 2 * N
        tree = [0] * _2N
        tree[N:_2N] = [i for i in range(N)]
        for i in range(N-1, 0, -1):
            _2N = i * 2
            if arr[tree[_2N]] <= arr[tree[_2N + 1]]:
                tree[i] = tree[_2N]
            else:
                tree[i] = tree[_2N + 1]

        return tree

    def query(start, end):
        ret = start
        std_val = inf
        start += N
        end += N

        while start < end:
            if start % 2:
                if arr[tree[start]] < std_val or (arr[tree[start]] == std_val and tree[start] < ret):
                    ret = tree[start]
                    std_val = arr[ret]
                start += 1
            if end % 2:
                end -= 1
                if arr[tree[end]] < std_val or (arr[tree[end]] == std_val and tree[end] < ret):
                    ret = tree[end]
                    std_val = arr[ret]
            start //= 2
            end //= 2

        return ret

    def update(idx, val):
        arr[idx] = val
        idx += N
        while idx > 1:
            tmp = idx // 2
            if arr[tree[idx]] == arr[tree[idx ^ 1]]:
                tree[tmp] = tree[idx] if tree[idx] < tree[idx ^ 1] else tree[idx ^ 1]
            elif arr[tree[idx]] < arr[tree[idx ^ 1]]:
                tree[tmp] = tree[idx]
            else:
                tree[tmp] = tree[idx ^ 1]
            idx = tmp

    tree = init_tree()
    for _ in range(M):
        a, *b = map(int, input().split())
        if a == 1:
            update(b[0]-1, b[1])
        else:
            print(query(0, N) + 1)


if __name__ == '__main__':
    solve()
