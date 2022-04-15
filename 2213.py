"""
Probliem Link: https://www.acmicpc.net/problem/2213
Solution Link: https://jintak0401.github.io/posts/boj-2213
"""
from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    arr = [0, *map(int, input().split())]

    tree = [[] for _ in range(N + 1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (N + 1)

    def get_ans(idx):
        visited[idx] = True
        sel_w, nsel_w = arr[idx], 0
        sel_n, nsel_n = [idx], []

        for nxt in tree[idx]:
            if not visited[nxt]:
                w_sel, w_nsel, n_sel, n_nsel = get_ans(nxt)
                sel_w += w_nsel
                sel_n += n_nsel
                if w_sel > w_nsel:
                    nsel_w += w_sel
                    nsel_n += n_sel
                else:
                    nsel_w += w_nsel
                    nsel_n += n_nsel

        return sel_w, nsel_w, sel_n, nsel_n

    wa, wb, na, nb = get_ans(1)

    if wa > wb:
        print(wa)
        print(*sorted(na))
    else:
        print(wb)
        print(*sorted(nb))


if __name__ == '__main__':
    solve()
