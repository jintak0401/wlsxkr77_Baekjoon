from sys import stdin


input = stdin.readline

ans_val = 0
count = [0] * 1000001
ans = []


def add_dic(n: int):
    global ans_val, count
    ans_val += not count[n]
    count[n] += 1


def erase_dic(n: int):
    global ans_val, count
    count[n] -= 1
    ans_val -= not count[n]


def solve():
    global ans, ans_val, arr

    lidx = 1
    ridx = 0

    for l, r, qid in query:
        # R 오른쪽으로 이동 --> 다음 숫자를 넣어준다
        for i in range(ridx + 1, r + 1):
            add_dic(arr[i])

        # R 왼쪽으로 이동 --> 이번 숫자를 빼준다
        for i in range(ridx, r, -1):
            erase_dic(arr[i])

        # L 오른쪽으로 이동 --> 이번 숫자를 빼준다
        for i in range(lidx, l):
            erase_dic(arr[i])

        # L 왼쪽으로 이동 --> 이전 숫자를 넣어준다
        for i in range(lidx-1, l-1, -1):
            add_dic(arr[i])

        lidx = l
        ridx = r

        ans[qid] = ans_val


if __name__ == '__main__':
    N = int(input())
    sqrt_N = int(N ** 0.5)
    arr = [0] + list(map(int, input().split()))
    M = int(input())
    ans = [0] * M
    query = [(*map(int, input().split()), i) for i in range(M)]
    query.sort(key=lambda t: (t[1] // sqrt_N, t[0]))
    solve()
    print(*ans, sep='\n')
