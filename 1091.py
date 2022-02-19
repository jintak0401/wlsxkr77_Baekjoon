from sys import stdin

input = stdin.readline

N: int
P: str
S: tuple[int, ...]
target: str


def shuffle(card: str):
    tmp = [''] * N
    for before, after in enumerate(S):
        tmp[after] = card[before]
    return ''.join(tmp)


def solve() -> int:
    global N, P, S, target
    card = P
    ans = 0
    while card != target:
        if card == P and ans != 0:
            ans = -1
            break

        ans += 1
        card = shuffle(card)

    return ans


if __name__ == '__main__':
    N = int(input())
    P = input()[:-1].replace(' ', '')
    S = tuple(map(int, input().split()))
    target = '012' * (N // 3)
    print(solve())
