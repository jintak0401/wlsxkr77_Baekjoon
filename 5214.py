from sys import stdin

input = stdin.readline


def solve():
    N, K, M = map(int, input().split())
    if N == 1:
        return 1
    arr = [[*map(int, input().split())] for _ in range(M)]

    # hyper[i] = [j] --> j번째 하이퍼튜브에 i번 역이 있다
    hyper = [[] for _ in range(N + 1)]
    for i in range(M):
        for j in arr[i]:
            hyper[j].append(i)

    visited = [False] * (N + 1)
    visited[1] = True

    que, ans = [1], 1
    # bfs
    while que:
        new_que = []
        for _ in range(len(que)):
            cur = que.pop()
            if cur == N:
                return ans
            # cur역이 존재하는 하이퍼 튜브를 돌면서 다음에 갈 수 있는 역을 que에 넣어준다
            for h in hyper[cur]:
                for nxt in arr[h]:
                    if not visited[nxt]:
                        new_que.append(nxt)
                        visited[nxt] = True

                # 하이퍼 튜브는 한 번만 이용되어야 하므로 비워준다
                arr[h] = []

        que = new_que
        ans += 1

    return -1


if __name__ == '__main__':
    print(solve())
