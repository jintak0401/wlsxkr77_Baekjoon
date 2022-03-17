from sys import stdin

input = stdin.readline


def solve():
    N, Q = map(int, input().split())
    arr = [*map(int, input().split())]

    def init_tree():
        # 리프 노드를 입력 받은 수열로 할당
        tree = [0] * N + arr
        for i in range(N - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]

        return tree

    # [start, end) 범위의 합을 구한다
    def query(start, end):
        ret = 0
        start += N
        end += N
        # 리프노드부터 더해나간다
        while start < end:
            if start & 1:
                ret += tree[start]
                start += 1
            if end & 1:
                end -= 1
                ret += tree[end]
            start >>= 1
            end >>= 1

        return ret

    def update(idx, val):
        idx += N
        # 리프 노드 수정 후
        tree[idx] = val
        # 부모노드를 자식 노드를 이용해 수정해준다
        while idx > 1:
            tree[idx >> 1] = tree[idx] + tree[idx ^ 1]
            idx >>= 1

    tree = init_tree()
    for _ in range(Q):
        x, y, a, b = map(int, input().split())
        if x > y:
            x, y = y, x
        print(query(x - 1, y))
        update(a - 1, b)


if __name__ == '__main__':
    solve()
