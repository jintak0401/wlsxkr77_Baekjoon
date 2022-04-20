from sys import stdin

input = stdin.readline


def solve():

    def init_tree():
        tree = [0] * (2 * N)
        tree[N:2 * N] = [1 if a > 0 else (-1 if a < 0 else 0) for a in arr]
        for i in range(N - 1, 0, -1):
            idx = 2 * i
            tree[i] = (tree[idx] * tree[idx + 1])

        return tree

    # [start, end) 의 쿼리를 구한다
    def query(start, end):
        ret = 1
        start += N
        end += N
        # 리프노드부터 구해나간다
        while start < end:
            if start % 2:
                ret *= tree[start]
                start += 1
            if end & 1:
                end -= 1
                ret *= tree[end]
            start //= 2
            end //= 2

        return '+' if ret > 0 else ('-' if ret < 0 else '0')

    def update(idx, val):
        idx += N
        # 리프 노드 수정 후
        tree[idx] = 1 if val > 0 else (-1 if val < 0 else 0)
        # 부모노드를 자식 노드를 이용해 수정해준다
        while idx > 1:
            nxt = idx // 2
            tree[nxt] = (tree[idx] * tree[idx ^ 1])
            idx = nxt

    while True:
        try:
            N, K = map(int, input().split())

            arr = [*map(int, input().split())]

            tree = init_tree()

            for _ in range(K):
                a, *target = input().split()
                b, c = map(int, target)

                if a == 'C':
                    update(b-1, c)
                else:
                    print(query(b-1, c), end='')

            print()
        except Exception:
            break


if __name__ == '__main__':
    solve()
