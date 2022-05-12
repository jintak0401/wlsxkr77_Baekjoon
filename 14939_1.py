from sys import stdin

input = stdin.readline


def solve():
    # 'O'를 1, '#'을 0 으로 하는 이진수로 저장
    origin = [int(''.join([str(int(c == 'O'))for c in input()[:-1]]), 2)for _ in range(10)]

    def hit(first_row):
        # need_hit 에서 1인 스위치를 눌러주어야 한다
        need_hit = first_row
        cnt = 0
        middle, up = 0, 0
        # 0행에서 9행까지 실행
        for i in range(10):
            cnt += bin(need_hit).count('1')
            middle, up = up, need_hit
            # (up // 2) 와 (up * 2) 는 윗 칸이 켜져있을 때
            # 가운데 줄은 해당 열의 좌우 까지 불이 toggle 되므로 존재
            need_hit = middle ^ (up // 2) ^ up ^ (up * 2) & 1023 ^ origin[i]

        # 마지막 행이 모두 꺼져있지 않다면 불가능
        return cnt if need_hit == 0 else 101

    # 1023: 맨 윗줄 스위치 누르는 경우의 수
    ans = min(hit(i) for i in range(1023))

    return ans if ans != 101 else -1


if __name__ == '__main__':
    print(solve())
