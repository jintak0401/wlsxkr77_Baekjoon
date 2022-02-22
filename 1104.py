from sys import stdin
from math import ceil

input = stdin.readline


S1: str
S2: str


def is_in_s(s1, s2):
    S = s1 + s2
    count = 0
    idx = 0
    for i in range(len(S)):
        if S[i] == '0':
            if count == 0:
                idx = i
            count += 1
            if count == C:
                return idx

        else:
            count = 0

    return -1


def solve():

    ans = is_in_s(S1, S1)

    # s1만 이어붙여도 가능한 경우
    if ans != -1:
        return ans

    # s1만으로는 불가능한 경우
    else:

        # s1이 1_000_000개 이어붙여진 길이
        s1_group = len(S1) * 1_000_000

        # S1이 0으로만 이루어진 경우
        if '1' not in S1:
            if '1' not in S2:
                return 0

            else:
                s2_idx = S2.find('1')
                s2_ridx = S2.rfind('1')

                if s1_group + s2_idx >= C:
                    return 0
                elif (len(S2) - s2_ridx - 1) + s1_group + s2_idx >= C:
                    return s1_group + s2_ridx + 1
                else:
                    return -1

        # S1이 0과 1로 이루어진 경우
        else:
            s1_idx = S1.find('1')
            s1_ridx = S1.rfind('1')

            # S1 S2 S1 인 경우
            ans = is_in_s(S1+S2, S1)
            if ans != -1:
                return ans + (s1_group - len(S1))

            # S1 S2 S2 S1 인 경우
            ans = is_in_s(S1+S2, S2+S1)

            if ans != -1:
                return ans + (2 * s1_group - len(S1)) + len(S2)

            if '1' in S2:
                return -1

            # S2에 0밖에 없는 경우
            len_s1_side = s1_idx + (len(S1) - s1_ridx - 1)
            n = ceil((C - len_s1_side) / len(S2))
            idx = (1_000_000 * n - 1) * len(S1) + (n * (n - 1) // 2) * len(S2) + s1_ridx + 1
            # 문자열이 10^16개 이내로 들어오는지 검사
            if idx + C <= 10_000_000_000_000_000:
                return idx
            else:
                return -1


if __name__ == '__main__':
    S1 = input()[:-1]
    S2 = input()[:-1]
    C = int(input())
    print(solve())
