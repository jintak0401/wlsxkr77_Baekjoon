from sys import stdin

input = stdin.readline


def solve():
    Str = input()[:-1]
    N = len(Str)
    ans = [2500] * (N + 1)
    ans[0], ans[N] = 1, 0

    # 2*N-1 인 이유: 홀수길이, 짝수길이 번갈아가며 팰린드롬 여부 확인하기 위해
    for i in range(1, 2 * N - 1):
        # i가 홀수: 짝수길이, i가 짝수: 홀수길이
        start, end = i // 2, (i + 1) // 2
        while 0 <= start and end < N:
            if Str[start] == Str[end]:
                if ans[start-1] + 1 < ans[end]:
                    ans[end] = ans[start-1] + 1
                start -= 1
                end += 1
            else: break

    return ans[N-1]


if __name__ == '__main__':
    print(solve())
