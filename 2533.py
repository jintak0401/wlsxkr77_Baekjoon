from sys import stdin, setrecursionlimit as SRL
SRL(1_000_000)

input = stdin.readline


def solve():
    N = int(input())

    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (N + 1)

    def dfs(idx):
        cur1, cur2 = 1, 0
        visited[idx] = True

        for nxt in tree[idx]:
            if not visited[nxt]:
                tmp1, tmp2 = dfs(nxt)
                cur1 += tmp1 if tmp1 < tmp2 else tmp2
                cur2 += tmp1

        return cur1, cur2

    ans1, ans2 = dfs(1)

    return ans1 if ans1 < ans2 else ans2


if __name__ == '__main__':
    print(solve())
