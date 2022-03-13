from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    # 직원에 해당하는 변수로 1인당 2개까지 일할 수 있으므로 1명을 2명으로 만들어준다
    # left_vertex[i] = [i번째 직원이 할 수 있는 일들]
    left_vertex = [0] * (N + 1)
    for i in range(1, N + 1):
        _, *works = map(int, input().split())
        left_vertex[i] = works

    # 일에 해당하는 변수
    # right_vertex[i] = j --> i번째 일은 j번째 직원이 한다
    right_vertex = [0] * (M + 1)

    def bipartite_matching(visited, here):
        visited[here] = True
        for there in left_vertex[here]:
            if not right_vertex[there]:
                right_vertex[there] = here
                return True
        for there in left_vertex[here]:
            if not visited[right_vertex[there]] and bipartite_matching(visited, right_vertex[there]):
                right_vertex[there] = here
                return True
        return False

    ans = 0
    for i in range(1, N+1):
        if bipartite_matching([False]*(N+1), i):
            ans += 1
            if ans == M:
                break

    return ans


if __name__ == '__main__':
    print(solve())
