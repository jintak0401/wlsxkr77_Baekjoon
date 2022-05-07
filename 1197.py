from sys import stdin

input = stdin.readline


def solve():
    V, E = map(int, input().split())
    weight = sorted([[*map(int, input().split())] for _ in range(E)], key=lambda x: x[2])
    disjoint_set = [-1] * (V + 1)

    def find(x):
        ret = x
        while disjoint_set[ret] > 0: ret = disjoint_set[ret]
        while x != ret:
            tmp = disjoint_set[x]
            disjoint_set[x] = ret
            x = tmp
        return ret

    cnt, ans = V - 1, 0
    for a, b, c in weight:
        x, y = find(a), find(b)
        if x != y:
            disjoint_set[y] = x
            cnt -= 1
            ans += c
            if cnt == 0: return ans


if __name__ == '__main__':
    print(solve())
