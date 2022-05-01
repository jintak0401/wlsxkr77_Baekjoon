from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    L = int(input())
    C = int(input())

    num_song_in_one = (C + 1) // (L + 1)

    if num_song_in_one % 13 == 0:
        num_song_in_one -= 1

    ans = N // num_song_in_one

    remain = N % num_song_in_one

    if remain > 0:
        if remain % 13 == 0 and remain + 1 == num_song_in_one:
            ans += 2
        else:
            ans += 1

    return ans


if __name__ == '__main__':
    print(solve())
