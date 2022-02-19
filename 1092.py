from sys import stdin
from heapq import heappush, heappop
from bisect import bisect_left

input = stdin.readline


def solve(boxes: list[int], cranes: list[int]) -> int:

    cranes[:bisect_left(cranes, boxes[-1])] = []

    crane_heap = []

    for box in boxes:
        # 큰 박스부터 heap에 들어가므로 이후의 박스들도 크레인이 들 수 있다
        while cranes and cranes[-1] >= box:
            # (박스 옮긴 횟수, 해당 크레인 무게) 를 crane_heap 에 넣는다
            heappush(crane_heap, (0, cranes.pop()))
        # 가능한 크레인들 중 박스 옮긴 횟수(=cnt)가 가장 적은 크레인이 짐을 옮긴다
        cnt, crane = heappop(crane_heap)
        # 옮긴 크레인의 cnt를 1증가하여 다시 heap에 삽입
        heappush(crane_heap, (cnt + 1, crane))

    # 튜플의 첫 요소(박스 옮긴 횟수)가 큰 튜플이 반환
    return max(crane_heap)[0]


if __name__ == '__main__':
    _ = int(input())
    cranes = list(map(int, input().split()))
    _ = int(input())
    boxes = list(map(int, input().split()))

    cranes.sort()
    boxes.sort(reverse=True)

    print(solve(boxes, cranes) if cranes[-1] >= boxes[0] else -1)
