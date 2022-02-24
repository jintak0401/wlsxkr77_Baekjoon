from sys import stdin

input = stdin.readline


visited = []
connected_vertex = []


# 이분매칭
def bipartite_matching(vertex, here):
    global visited
    for there in vertex[here]:
        if not visited[there]:
            visited[there] = True
            if (not connected_vertex[there]) or bipartite_matching(vertex, connected_vertex[there]):
                connected_vertex[there] = here
                return True

    return False


def solve(n):
    global visited, connected_vertex
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        arr[i] = [*map(int, input().split())]

    # 밝은 칸과 어두운 칸을 나누어 생각
    white_diag = [0] + [[] for _ in range(n)]
    black_diag = [0] + [[] for _ in range(n - 1)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                # 왼쪽 아래를 향한 대각선과 오른쪽 아래를 향한 대각선
                # 두 그룹으로 나눈어 리스트에 넣는다
                if (i + j) & 1:
                    black_diag[((i + j) // 2) + 1].append(((i - j + n - 1) // 2) + 1)
                else:
                    white_diag[((i + j) // 2) + 1].append(((i - j + n - 1) // 2) + 1)

    ans = 0

    # 왼쪽 아래 대각선과 오른쪽 아래 대각선, 두 그룹에 대해 이분매칭 진행
    connected_vertex = [0] * len(white_diag)
    for i in range(1, len(white_diag)):
        visited = [False] * len(white_diag)
        if bipartite_matching(white_diag, i):
            ans += 1

    connected_vertex = [0] * len(black_diag)
    for i in range(1, len(black_diag)):
        visited = [False] * len(black_diag)
        if bipartite_matching(black_diag, i):
            ans += 1

    return ans


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
