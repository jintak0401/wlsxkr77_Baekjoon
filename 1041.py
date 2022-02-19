from sys import stdin


input = stdin.readline

N: int
arr: list[int]


def solve() -> int:
    global N, arr
    if N == 1:
        return sum(arr) - max(arr)
    # 마주 보고 있는 면들 중 더 적은 숫자들 3개 --> 모두 이웃하다
    parallel = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
    parallel.sort()
    three = sum(parallel)
    two = parallel[0] + parallel[1]
    one = parallel[0]
    return 4*three + (8*N-12)*two + (N-2)*(5*N-6)*one


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve())
