from random import randint

_queens = []


def chess_solve():
    for i in range(8):
        _queens.append(tuple(map(int, f'{randint(1, 8)} {randint(1, 8)}'.split())))
        print(_queens)

    # Проверяем, бьют ли ферзи друг друга
    for i in range(8):
        for j in range(i + 1, 8):
            if is_attacking(_queens[i], _queens[j]):
                return False
    return True


def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return True
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    else:
        return False


def random_chess():
    count = 0
    while count < 4:
        if chess_solve():
            print(_queens)
            print()
            count += 1
        _queens.clear()


if __name__ == "__main__":
    random_chess()
