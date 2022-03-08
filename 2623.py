from sys import stdin


input = stdin.readline


def solve():

    N, M = map(int, input().split())

    # edge[이전 사람] = [다음 사람들]
    edge = [[] for _ in range(N + 1)]
    # indegree[i]: i번째 가수 이전에 나와야 하는 가수들 중 나오지 않은 사람들의 수
    indegree = [0] * (N + 1)

    for _ in range(M):
        _, *line = map(int, input().split())
        for i in range(len(line) - 1):
            edge[line[i]].append(line[i+1])
            indegree[line[i+1]] += 1

    que = [i for i in range(1, N + 1) if indegree[i] == 0]
    ans = [0] * N
    idx = 0
    while True:
        if not que:
            break
        new_que = []
        while que:
            cur_singer = que.pop()
            ans[idx] = cur_singer
            idx += 1
            for next_singer in edge[cur_singer]:
                indegree[next_singer] -= 1
                if indegree[next_singer] == 0:
                    new_que.append(next_singer)
        que = new_que

    return ans if idx == N else [0]


if __name__ == '__main__':
    print(*solve(), sep='\n')
