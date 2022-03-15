from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 6)


input = stdin.readline


def solve():
    N = int(input())
    p_seq = (*map(int, input().split()), )
    visited = 0

    def dfs(num):
        nonlocal visited
        if not visited & (1 << num):
            visited |= (1 << num)
            dfs(p_seq[num])

    ans = 0
    for i in range(N):
        if not visited & (1 << i):
            dfs(i)
            ans += 1
    return ans if ans != 1 else 0


if __name__ == '__main__':
    print(solve())

