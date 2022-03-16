from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = [*map(int, input().split())]

    def init_tree():
        # len(arr) -> size: 1 ~ 2 -> 2 / 3 ~ 4 -> 4 / 5 ~ 8 -> 8 / ... / 2^n + 1 ~ 2^(n+1) -> 2^(n+1)
        size = 1 << (len(arr) - 1).bit_length()
        # internal_node 의 개수는 (size - 1)개, 루트 노드의 인덱스는 1
        internal_node = [[] for _ in range(size)]
        # leaf_node 의 개수는 size개
        leaf_node = [[i] for i, value in sorted(enumerate(arr), key=lambda t: t[1])] + [[]] * (size - len(arr))
        tree = internal_node + leaf_node
        # internal_node 를 초기화
        for i in range(size - 1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]
            tree[i].sort()
        # ex) 수열 입력: 10, 50, 20, 60, 30, 70, 40, 90, 80
        # 루트노드: [0(10), 1(50), 2(20), 3(60), 4(30), 5(70), 6(40), 7(90), 8(80)]
        # 루트노드는 인덱스 순서로 정렬되며, 입력된 수열과 같은 순서를 가진다

        # 리프노드: [0(10)], [2(20)], [4(30)], [6(40)], [1(50)], [3(60)], [5(70)], [8(80)], [7(90)]
        # 리프노드는 입력된 수열이 정렬된 순서로 저장된다
        return size, tree

    def query(start, end, k):
        idx = 1
        # 리프노드에 도달할 때까지 수행
        while idx < size:
            # 부모노드의 수열 중 작은 수들이 모여있는 왼쪽 자식노드의 수열에 대해
            # start ~ end 의 인덱스에 해당하는 수가 몇 개 있는지 계산
            # 왼쪽 자식은 정렬되어 있는 것은 아니지만 모든 원소가 오른쪽 자식노드보다 작다
            idx += idx
            node = tree[idx]
            count = bisect_left(node, end) - bisect_left(node, start)
            # 왼쪽 자식노드에 start ~ end 인덱스에 해당하는 수가 k보다 적다면 원하는 수는 오른쪽 자식 노드에 있다
            # 왜냐하면 왼쪽 자식노드는 정렬되어 있지는 않지만 모든 원소가 오른쪽 자식노드보다 작기 때문
            if count < k:
                idx += 1
                k -= count

        return arr[tree[idx][0]]

    size, tree = init_tree()
    for _ in range(M):
        start, end, k = map(int, input().split())
        # 개수를 세주기 위해서 start - 1 을 해줌
        print(query(start - 1, end, k))


if __name__ == '__main__':
    solve()
