from sys import stdin


input = stdin.readline

N: int
tree: dict[int, set] = {}
delete: int = 0


def solve(node: int) -> int:
    global N, tree, delete
    if node not in tree or tree[node] == {delete}:
        return 1
    ret = 0
    for i in tree[node]:
        if i != delete:
            ret += solve(i)
    return ret


if __name__ == '__main__':
    N = int(input())
    # tree --> { 부모1: { 자식1, 자식2, ... }, 부모2: { 자식1, 자식2, ...} }
    parents = list(map(int, input().split()))
    root = 0
    for child in range(N):
        if parents[child] == -1:
            root = child
        else:
            tree[parents[child]] = tree.get(parents[child], set()) | {child}
    delete = int(input())

    print(solve(root) if delete != root else 0)
