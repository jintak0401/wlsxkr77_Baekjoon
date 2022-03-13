from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(1, N + 1):
        arr[i] = int(input())
    tree = [0] * (4 * N + 1)

    def init_tree(left, right, node):
        if left == right:
            tree[node] = (arr[left], arr[left])
            return tree[node]
        else:
            mid = (left + right) // 2
            l_minmax = init_tree(left, mid, 2 * node)
            r_minmax = init_tree(mid + 1, right, 2 * node + 1)
            min_val = l_minmax[0] if l_minmax[0] < r_minmax[0] else r_minmax[0]
            max_val = l_minmax[1] if l_minmax[1] > r_minmax[1] else r_minmax[1]
            tree[node] = (min_val, max_val)
            return tree[node]

    def get_minmax(left, right, node, start, end):
        if end < left or right < start:
            return 1_000_000_001, 0
        elif start <= left and right <= end:
            return tree[node]
        else:
            mid = (left + right) // 2
            l_minmax = get_minmax(left, mid, 2 * node, start, end)
            r_minmax = get_minmax(mid + 1, right, 2 * node + 1, start, end)
            min_val = l_minmax[0] if l_minmax[0] < r_minmax[0] else r_minmax[0]
            max_val = l_minmax[1] if l_minmax[1] > r_minmax[1] else r_minmax[1]
            return min_val, max_val

    init_tree(1, N, 1)
    for _ in range(M):
        start, end = map(int, input().split())
        print(*get_minmax(1, N, 1, start, end))


if __name__ == '__main__':
    solve()
