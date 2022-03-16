from sys import stdin


input = stdin.readline


def solve():
    N = int(input())
    M = int(input())
    enemy = {}
    disjoint_set = [-1] * (N + 1)

    def find(a):
        if disjoint_set[a] <= 0:
            return a
        else:
            disjoint_set[a] = find(disjoint_set[a])
            return disjoint_set[a]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return
        elif root_a < root_b:
            disjoint_set[root_b] = root_a
        else:
            disjoint_set[root_a] = root_b

    for _ in range(M):
        relationship, *people = input().split()
        p, q = map(int, people)
        if relationship == 'F':
            union(p, q)
        else:
            if p not in enemy:
                enemy[p] = set()
            if q not in enemy:
                enemy[q] = set()
            enemy[p].add(q)
            enemy[q].add(p)

    for same_team in enemy.values():
        a = same_team.pop()
        for b in same_team:
            union(a, b)

    return sum(1 for i in range(1, N+1) if disjoint_set[i] == -1)


if __name__ == '__main__':
    print(solve())
