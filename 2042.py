from sys import stdin


input = stdin.readline


def solve():
    N, M, K = map(int, input().split())

    arr = [0] * N
    for i in range(N):
        arr[i] = int(input())

    def init_tree():
        tree = [0] * (2 * N)
        # 리프 노드를 입력 받은 수열로 할당
        tree[N:2 * N] = arr
        for i in range(N - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]

        return tree

    # [start, end) 의 합을 구한다
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

    k = 0
    while k < K:
        a, b, c = map(int, input().split())
        if a == 1:
            update(b-1, c)
        else:
            k += 1
            print(query(b-1, c))


if __name__ == '__main__':
    solve()
