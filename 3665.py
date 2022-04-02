from sys import stdin

input = stdin.readline


def solve():
    TC = int(input())
    for _ in range(TC):
        N = int(input())
        arr = [*map(int, input().split())]
        # indegree[i] = i번째 팀의 등수 - 1
        indegree = [0] * (N + 1)
        for i in range(N):
            indegree[arr[i]] = i
        cp_indegree = [*indegree]
        for _ in range(int(input())):
            a, b = map(int, input().split())
            if cp_indegree[a] > cp_indegree[b]:
                indegree[a] -= 1
                indegree[b] += 1
            else:
                indegree[a] += 1
                indegree[b] -= 1

        ranking = sorted(enumerate(indegree[1:], start=1), key=lambda x: x[1])
        ans, flag = [ranking[0][0]] + [0] * (N-1), False
        for i in range(1, N):
            if ranking[i][1] == ranking[i-1][1]:
                flag = True
                break
            ans[i] = ranking[i][0]

        if flag:
            print('IMPOSSIBLE')
        else:
            print(*ans)


if __name__ == '__main__':
    solve()
