from sys import stdin

input = stdin.readline

min_val: int
max_val: int


def get_prime_list(n: int) -> list[int]:
    if n < 2:
        return []

    n += 1
    # [ 쓰레기값, 3, 5, 7, 9, 11, 13, ... ] 에 대응됨
    sieve = [True] * (n // 2)
    # 3부터 홀수만 검사 (2를 제외한 모든 소수는 홀수이므로)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            k = i * i
            # k=9 -> sieve[4]=9 / i=3는 소수고 sieve[4::3]=[9, 15, 21,...]은 소수가 아님
            # k=25 -> sieve[14]=25 / i=5는 소수고 sieve[14::5]=[25, 35, 45, ...]은 소수가 아님
            sieve[k // 2::i] = [False] * ((n - k - 1) // (2 * i) + 1)

    # 인덱스 1부터 시작하는 이유는 sieve[0]은 쓰레기값이므로
    return [2] + [2 * i + 1 for i in range(1, len(sieve)) if sieve[i]]


def solve():
    sieve = [1] * (max_val - min_val + 1)

    for p in get_prime_list(int(max_val ** 0.5)):
        square = p ** 2
        u = (min_val - 1) // square + 1
        v = max_val // square + 1
        sieve[u * square - min_val::square] = [0] * (v - u)

    return sum(sieve)


if __name__ == '__main__':
    min_val, max_val = map(int, input().split())
    print(solve())
