from sys import stdin

input = stdin.readline


def solve():

    def get_rotate_side(side, direction):
        if direction == '+':
            return [side[-1]] + side[:-1]
        else:
            return side[1:] + [side[0]]

    def get_rotate_plane(plane, direction):
        ret = [[0] * 3 for _ in range(3)]
        if direction == '+':
            ret[0] = [plane[2][0], plane[1][0], plane[0][0]]
            ret[1] = [plane[2][1], plane[1][1], plane[0][1]]
            ret[2] = [plane[2][2], plane[1][2], plane[0][2]]

        else:
            ret[0] = [plane[0][2], plane[1][2], plane[2][2]]
            ret[1] = [plane[0][1], plane[1][1], plane[2][1]]
            ret[2] = [plane[0][0], plane[1][0], plane[2][0]]

        return ret

    # 위(0), 아래(1), 앞(2), 뒤(3), 왼(4), 오(5)
    def rotate(where, direction):
        if where == 'U':
            plane_num = 0
            side_pos = [
                [(3, 0, 2), (3, 0, 1), (3, 0, 0)],
                [(5, 0, 2), (5, 0, 1), (5, 0, 0)],
                [(2, 0, 2), (2, 0, 1), (2, 0, 0)],
                [(4, 0, 2), (4, 0, 1), (4, 0, 0)],
            ]
        elif where == 'D':
            plane_num = 1
            side_pos = [
                [(2, 2, 0), (2, 2, 1), (2, 2, 2)],
                [(5, 2, 0), (5, 2, 1), (5, 2, 2)],
                [(3, 2, 0), (3, 2, 1), (3, 2, 2)],
                [(4, 2, 0), (4, 2, 1), (4, 2, 2)],
            ]
        elif where == 'F':
            plane_num = 2
            side_pos = [
                [(0, 2, 0), (0, 2, 1), (0, 2, 2)],
                [(5, 0, 0), (5, 1, 0), (5, 2, 0)],
                [(1, 0, 2), (1, 0, 1), (1, 0, 0)],
                [(4, 2, 2), (4, 1, 2), (4, 0, 2)],
            ]
        elif where == 'B':
            plane_num = 3
            side_pos = [
                [(0, 0, 2), (0, 0, 1), (0, 0, 0)],
                [(4, 0, 0), (4, 1, 0), (4, 2, 0)],
                [(1, 2, 0), (1, 2, 1), (1, 2, 2)],
                [(5, 2, 2), (5, 1, 2), (5, 0, 2)],
            ]
        elif where == 'L':
            plane_num = 4
            side_pos = [
                [(0, 0, 0), (0, 1, 0), (0, 2, 0)],
                [(2, 0, 0), (2, 1, 0), (2, 2, 0)],
                [(1, 0, 0), (1, 1, 0), (1, 2, 0)],
                [(3, 2, 2), (3, 1, 2), (3, 0, 2)],
            ]
        else:
            plane_num = 5
            side_pos = [
                [(0, 2, 2), (0, 1, 2), (0, 0, 2)],
                [(3, 0, 0), (3, 1, 0), (3, 2, 0)],
                [(1, 2, 2), (1, 1, 2), (1, 0, 2)],
                [(2, 2, 2), (2, 1, 2), (2, 0, 2)]
            ]

        plane = cube[plane_num]
        side = [[] for _ in range(4)]
        for idx, pos in enumerate(side_pos):
            for x, y, z in pos:
                side[idx].append(cube[x][y][z])

        after_plane = get_rotate_plane(plane, direction)
        after_side = get_rotate_side(side, direction)

        cube[plane_num] = after_plane
        for i in range(4):
            pos = side_pos[i]
            for j in range(3):
                x, y, z = pos[j]
                cube[x][y][z] = after_side[i][j]

    def print_result():
        for line in cube[0]:
            print(*line, sep='')

    def generate_cube():
        ret = [0] * 6
        for i in range(6):
            ret[i] = [[colors[i]] * 3 for _ in range(3)]
        return ret

    # 위(0), 아래(1), 앞(2), 뒤(3), 왼(4), 오(5)
    colors = ['w', 'y', 'r', 'o', 'g', 'b']

    for _ in range(int(input())):
        N = int(input())
        cube = generate_cube()
        queries = input().split()
        for query in queries:
            rotate(*query)
        print_result()


if __name__ == '__main__':
    solve()
