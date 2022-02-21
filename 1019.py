from sys import stdin

input = stdin.readline


def solve(original_n):
    ans = [0] * 10
    # 10^k
    digit_pos = 1

    # original_n = 876_543_210 인 경우
    # 10^k의 자리수를 k자리 수라고 하면
    # 0의 자리수부터 8의 자리수까지 진행
    n = original_n
    while n != 0:
        # _next = k 자리수 위쪽의 수
        # current = k 자리수의 숫자
        _next, current = divmod(n, 10)

        # 8의 자리수가 아닐 때
        # ex) 5의 자리수라고 하면 digit_pos = 10^5 = 100_000
        if _next:
            for i in range(10):
                # unit = 875
                unit = max(_next - 1, 0)

                # i = 5 일 때 unit = 875_043_211
                # 1_000_000 부터 875_999_999 까지 5의 자리에 5가 나오는 횟수 = (875 * 10^5)개
                # 876_500_000 부터 876_543_210 까지 총 (43_210 + 1)개
                if i == current:
                    unit = unit * digit_pos + (original_n % digit_pos) + 1

                # i < 5 인 경우
                # 1_000_000 부터 876_i99_999 까지 총 (876 * 10^5)개

                # i > 5 인 경우
                # 1_000_000 부터 875_999_999 까지 총 (875 * 10^5)개
                else:
                    unit = (unit + (i < current)) * digit_pos

                # 5의 자리수가 최고 자리 수 일 때 1부터 9까지 10^k 만큼 더 존재
                # i00_000 부터 i99_999 까지 총 10^5개
                if i != 0:
                    unit += digit_pos

                ans[i] += unit

        # 8의 자리수일 때
        # digit_pos = 10^8 = 100_000_000
        else:
            for i in range(1, current + 1):
                # 1 < = i = 7 인경우
                # i00_000_000 부터 i99_999_999 까지 총 10^8개
                if i < current:
                    ans[i] += digit_pos
                # i = 8 인 경우
                # 800_000_000 부터 876_543_210 까지 총 (76_543_210 + 1)개
                else:
                    ans[i] += (original_n % digit_pos) + 1

        digit_pos *= 10
        n = _next

    return ans


if __name__ == '__main__':
    num = int(input())

    if num <= 9:
        print(*[1 if 1 <= i <= num else 0 for i in range(10)])
    else:
        print(*solve(num))
