from sys import stdin

input = stdin.readline


# arpa's trick 을 이용한 풀이
def solve():
    N, M = map(int, input().split())

    arr = [int(input()) for _ in range(N)]

    disjoint_set = [-1] * N

    def union_find(node):
        if disjoint_set[node] == -1:
            return node
        else:
            disjoint_set[node] = union_find(disjoint_set[node])
            return disjoint_set[node]

    query = [[] for _ in range(N)]
    for i in range(M):
        l, r = map(int, input().split())
        query[r-1].append((l-1, i))

    s, ans = [], [0] * M
    for i in range(N):
        while s and arr[s[-1]] > arr[i]:
            disjoint_set[s[-1]] = i
            s.pop()
        s.append(i)
        for l, qi in query[i]:
            ans[qi] = arr[union_find(l)]

    return ans


if __name__ == '__main__':
    print(*solve(), sep='\n')
