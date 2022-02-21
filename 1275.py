from sys import stdin

input = stdin.readline

tree = []
arr = []
quiz = []


# start, end: 트리 내 범위
def init_tree(start, end, node):
    global tree
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init_tree(start, mid, 2 * node) + init_tree(mid + 1, end, 2 * node + 1)
    return tree[node]


# start, end: 트리 내 범위
# left, right: 구하고자 하는 합의 범위
def get_sum(start, end, node, left, right):
    # 범위 밖
    if right < start or end < left:
        return 0

    elif left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return get_sum(start, mid, 2 * node, left, right) + get_sum(mid + 1, end, 2 * node + 1, left, right)


# target: 바꿀 노드
# start, end: 트리 내 범위
def update_tree(start, end, node, target, diff):
    global tree

    tree[node] += diff

    if start == end:
        return

    mid = (start + end) // 2

    if start <= target <= mid:
        update_tree(start, mid, 2 * node, target, diff)
    else:
        update_tree(mid + 1, end, 2 * node + 1, target, diff)


def solve():
    global tree, arr

    tree = [0] * (N * 4)
    init_tree(0, N - 1, 1)

    for i in range(Q):
        left, right, change_idx, change_val = quiz[i]
        print(get_sum(0, N - 1, 1, left, right))
        diff = change_val - arr[change_idx]
        arr[change_idx] = change_val
        update_tree(0, N - 1, 1, change_idx, diff)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(Q):
        x, y, a, b = map(int, input().split())
        if x > y:
            x, y = y, x
        quiz.append((x - 1, y - 1, a - 1, b))

    solve()
