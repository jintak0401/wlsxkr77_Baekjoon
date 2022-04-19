from sys import stdin

input = stdin.readline


def solve():

    N, M, K = map(int, input().split())

    mod = 1_000_000_007

    arr = [int(input()) for _ in range(N)]

    def init_tree():
        tree = [0] * (2 * N)
        # 리프 노드를 입력 받은 수열로 할당
        tree[N:2 * N] = arr
        for i in range(N - 1, 0, -1):
            idx = 2*i
            tree[i] = (tree[idx] * tree[idx+1]) % mod

        return tree

    # [start, end) 의 곱을 구한다
    def query(start, end):
        ret = 1
        start += N
        end += N
        # 리프노드부터 곱해나간다
        while start < end:
            if start % 2:
                ret = (ret * tree[start]) % mod
                start += 1
            if end & 1:
                end -= 1
                ret = (ret * tree[end]) % mod
            start //= 2
            end //= 2

        return ret

    def update(idx, val):
        idx += N
        # 리프 노드 수정 후
        tree[idx] = val
        # 부모노드를 자식 노드를 이용해 수정해준다
        while idx > 1:
            nxt = idx // 2
            tree[nxt] = (tree[idx] * tree[idx ^ 1]) % mod
            idx = nxt

    tree = init_tree()
    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(b-1, c)
        else:
            print(query(b-1, c))


if __name__ == '__main__':
    solve()
