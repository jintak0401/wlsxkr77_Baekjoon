from sys import stdin
from heapq import heappush, heappop

_input = stdin.readline


def solve():
    N, K = map(int, _input().split())
    arr = [*map(int, _input().split())]

    tmp = [500_001] * (K + 1)
    # arr[i] 와 같은 숫자가 다음으로 나오는 index
    pos = [0] * (K + 1)

    for i in range(K - 1, -1, -1):
        pos[i] = tmp[arr[i]]
        tmp[arr[i]] = i

    used, heap, ans = set(), [], 0

    for i in range(K):
        if i != K-1 and arr[i] == arr[i+1]:
            continue
        elif arr[i] not in used:
            if len(used) == N:
                ans += 1
                _, target = heappop(heap)
                used.remove(target)

            used.add(arr[i])

        heappush(heap, (-pos[i], arr[i]))

    return ans


if __name__ == '__main__':
    print(solve())
