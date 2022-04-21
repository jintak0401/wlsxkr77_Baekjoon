from sys import stdin

input = stdin.readline


def solve():

    for _ in range(int(input())):
        # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
        # 홀수 idx는 왼쪽에서 버린 것
        # 짝수 idx는 오른쪽에서 버린 것
        p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

        n = int(input())
        arr = input()[1:-2].split(',')
        # [left, right) 가 출력된다
        left, right = sum(p[::2]), n - sum(p[1::2])

        if left <= right:
            # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
            arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
            print(f"[{','.join(arr)}]")
        else:
            print('error')


if __name__ == '__main__':
    solve()
