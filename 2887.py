from sys import stdin

input = stdin.readline


def find(disjoint_set, a):
    if disjoint_set[a] <= 0:
        return a
    else:
        disjoint_set[a] = find(disjoint_set, disjoint_set[a])
        return disjoint_set[a]


def solve():
    N = int(input())
    planet = [0] * N
    for i in range(N):
        planet[i] = (*map(int, input().split()), i+1)

    mst = [0] * (3 * (N - 1))
    for i in range(3):
        planet.sort(key=lambda t: t[i])
        mst[(N-1) * i: (N-1) * (i+1)] = [(planet[j][i] - planet[j-1][i], planet[j][-1], planet[j-1][-1]) for j in range(1, N)]

    disjoint_set = [0] * (N + 1)
    mst.sort()
    ans = 0
    unit = 0
    for diff, a, b in mst:
        a_root, b_root = find(disjoint_set, a), find(disjoint_set, b)
        if a_root != b_root:
            if a_root < b_root:
                disjoint_set[b_root] = a_root
            else:
                disjoint_set[a_root] = b_root

            ans += diff
            unit += 1

            if unit == N - 1:
                break

    return ans


if __name__ == '__main__':
    print(solve())
