from sys import stdin

_input = stdin.readline


def solve():
    N = int(_input())
    # (idx, 높이)
    arr = [int(_input()) for _ in range(N)]

    # (높이, 연속된 개수)
    stack = []
    ans = 0

    for height in arr:
        while stack and stack[-1][0] < height:
            ans += stack.pop()[1]

        # 스택이 비었을 경우 그냥 넣어준다
        if not stack:
            stack.append((height, 1))

        else:
            # 같은 높이로 연속된 경우
            if stack[-1][0] == height:
                count = stack.pop()[1]
                # 같은 높이 내에서 서로 바라보는 경우의 수
                ans += count

                # stack이 비어있지 않다면 --> 더 높은 높이만 존재
                # 이전의 더 높은 높이에서 바라보는 경우의 수
                if stack:
                    ans += 1

                stack.append((height, count + 1))

            else:
                ans += 1
                stack.append((height, 1))

    return ans


if __name__ == '__main__':
    print(solve())
