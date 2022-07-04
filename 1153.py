from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solve():
    def get_prime_list(n):
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

    def dfs(idx):
        if len(ans) == 3:
            remain = N - sum(ans)
            tmp_idx = bisect_left(prime_list, remain)
            if remain == prime_list[tmp_idx if tmp_idx < len(prime_list) else -1]:
                ans.append(remain)
                return True
            return False

        for nxt_idx, num in enumerate(prime_list[idx:]):
            ans.append(num)
            result = dfs(nxt_idx)
            if result:
                return True
            ans.pop()

        return False

    N = int(input())
    if N < 8:
        print(-1)
        return
    prime_list = get_prime_list(N)
    ans = []
    if dfs(0):
        print(*ans, sep=' ')
    else:
        print(-1)


if __name__ == '__main__':
    solve()
