from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    TC = int(input())

    for _ in range(TC):
        N, M = map(int, input().split())
        # 더 작은 권수부터 필요한 사람이 뒤로 가도록 정렬
        people = sorted([[*map(int, input().split())] for _ in range(M)], reverse=True)
        heap, ans = [], 0

        for i in range(1, N + 1):
            # i권부터 필요한 사람들이 몇권까지 허용되는지 heap에 넣어준다
            while people and people[-1][0] == i:
                heappush(heap, people.pop()[1])

            # i권을 가져도 되는 사람이 있을 경우
            while heap:
                if heappop(heap) >= i:
                    ans += 1
                    break

        print(ans)


if __name__ == '__main__':
    solve()
