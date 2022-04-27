from sys import stdin

input = stdin.readline


def solve():

    arr = input()[:-1]
    brr = input()[:-1]

    if len(brr) < len(arr):
        arr, brr = brr, arr

    # brr 안에 arr
    for i in range(len(brr) - len(arr) + 1):
        flag = True
        for j in range(len(arr)):
            if arr[j] == '2' and brr[i+j] == '2':
                flag = False
                break

        if flag:
            return len(brr)

    for i in range(len(arr) - 1, 0, -1):
        flag1, flag2, idx = True, True, -i
        for j in range(i):
            if flag1 and arr[idx] == '2' and brr[j] == '2':
                flag1 = False
            if flag2 and arr[j] == '2' and brr[idx] == '2':
                flag2 = False
            if not flag1 and not flag2:
                break

            idx += 1

        if flag1 or flag2:
            return len(arr) + len(brr) - i

    return len(arr) + len(brr)


if __name__ == '__main__':
    print(solve())
