from sys import stdin

input = stdin.readline

N: int
arr: list[list[str]] = []

# should_not_no[2] 중 하나라도 on인 경우 --> 2는 불가
# should_not_no[8] 이 모두 off인 경우 --> 8은 가능
should_not_on = {
    0: [(1, 1), (2, 1), (3, 1)],
    1: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)],
    2: [(1, 0), (1, 1), (3, 1), (3, 2)],
    3: [(1, 0), (1, 1), (3, 0), (3, 1)],
    4: [(0, 1), (1, 1), (3, 0), (3, 1), (4, 0), (4, 1)],
    5: [(1, 1), (1, 2), (3, 0), (3, 1)],
    6: [(1, 1), (1, 2), (3, 1)],
    7: [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)],
    8: [(1, 1), (3, 1)],
    9: [(1, 1), (3, 0), (3, 1)]
}


def which_num_possible(bulbs) -> list[int]:
    ret = []
    for num, pos in should_not_on.items():
        flag = True
        for x, y in pos:
            if bulbs[x][y] == '#':
                flag = False
                break
        if flag:
            ret.append(num)

    return ret


def solve() -> float:
    global N, arr
    nums = []
    total_len = 1
    for i in range(N):
        n = 4 * i
        val = [arr[j][n: n + 3] for j in range(5)]
        num = which_num_possible(val)
        if len(num) == 0:
            return -1
        nums.append(num)
        total_len *= len(num)
    ans = 0
    for i in range(len(nums)):
        ans = 10 * ans + sum(nums[i]) * total_len / len(nums[i])

    return ans / total_len


if __name__ == '__main__':
    N = int(input())
    for _ in range(5):
        arr.append(input()[:-1])
    print(solve())
