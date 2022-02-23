from sys import stdin, setrecursionlimit as SRL
from collections import deque
from math import ceil, log2

SRL(10**5)
input = stdin.readline


arr = []
tree = []


def init_tree(start, end, node):

    if start == end:
        tree[node] = start

    else:
        mid = (start + end) // 2

        init_tree(start, mid, 2 * node)
        init_tree(mid+1, end, 2 * node + 1)

        if arr[tree[2*node]] <= arr[tree[2*node + 1]]:
            tree[node] = tree[2*node]
        else:
            tree[node] = tree[2*node + 1]


def query(start, end, node, left, right):
    # 겹치는게 없는 경우
    if end < left or right < start:
        return -1
    # 완전히 겹치는 경우
    elif left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    l_query = query(start, mid, 2*node, left, right)
    r_query = query(mid+1, end, 2*node + 1, left, right)

    if l_query == -1:
        return r_query
    elif r_query == -1:
        return l_query
    else:
        return l_query if arr[l_query] < arr[r_query] else r_query


def largest(left, right):
    height_idx = query(0, len(arr) - 1, 1, left, right)
    ans = (right - left + 1) * arr[height_idx]
    if left < height_idx:
        ans = max(largest(left, height_idx - 1), ans)

    if height_idx < right:
        ans = max(largest(height_idx + 1, right), ans)

    return ans


if __name__ == '__main__':
    while True:
        arr = deque(map(int, input().split()))
        n = arr.popleft()
        if not n:
            break
        tree = [0] * (1 << (ceil(log2(n)) + 1))
        init_tree(0, n - 1, 1)
        print(largest(0, n - 1))
