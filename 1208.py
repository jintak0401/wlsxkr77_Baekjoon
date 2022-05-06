from sys import stdin

input = stdin.readline


def solve():
    N, S = map(int, input().split())
    arr = [*map(int, input().split())]

    def extend(brr):
        ret = [0]
        for b in brr:
            tmp = [b + c for c in ret]
            ret += tmp
        return ret

    def count_sub(brr):
        dic = {0: 1}
        for b in brr:
            tmp = {}
            for v in dic:
                tmp[b + v] = dic[v]
            for v in tmp:
                if v in dic:
                    dic[v] += tmp[v]
                else:
                    dic[v] = tmp[v]

        return dic

    idx = N//2
    left_arr = extend(arr[:idx])
    right_dic = count_sub(arr[idx:])

    ans = 0
    for v in left_arr:
        remain = S - v
        if remain in right_dic:
            ans += right_dic[remain]

    return ans if S != 0 else ans - 1


if __name__ == '__main__':
    print(solve())
