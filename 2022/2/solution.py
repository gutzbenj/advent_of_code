from tools import load_input

MAP1 = {
    "A": 0,
    "B": 1,
    "C": 2
}
MAP2 = {
    "X": 0,
    "Y": 1,
    "Z": 2
}
_MAP2 = {value: key for key, value in MAP2.items()}
BONUS_SCORE = {
    0: 1,
    1: 2,
    2: 3
}
WINS = (
    (0, 1),
    (1, 2),
    (2, 0)
)


def is_win(x, y):
    if (y - x) == 1 or (y - x) == -2:
        return 1
    elif y == x:
        return 0
    else:
        return -1


def _evaluate(x, y):
    points = 0
    if is_win(x, y) == 1:
        points += 6
    elif x == y:
        points += 3
    return points + BONUS_SCORE[y]


def evaluate_ruleset1(choices):
    x, y = choices
    x = MAP1[x]
    y = MAP2[y]
    return _evaluate(x, y)


def evaluate_ruleset2(choices):
    x, y = choices
    if y == "X":
        _ = MAP1[x] - 1
        if _ < 0:
           _ = 2
        y = _MAP2[_]
    elif y == "Y":
        # create draw
        y = _MAP2[MAP1[x]]
    else:
        _ = MAP1[x] + 1
        if _ > 2:
           _ = 0
        y = _MAP2[_]
    x = MAP1[x]
    y = MAP2[y]
    return _evaluate(x, y)


def solve1():
    data = load_input("2022/2/1")
    data = data.split("\n")
    data = [
        evaluate_ruleset1(r.split(" "))
        for r in data
    ]
    return sum(data)


def solve2():
    data = load_input("2022/2/1")  # same input
    data = data.split("\n")
    data = [
        evaluate_ruleset2(r.split(" "))
        for r in data
    ]
    return sum(data)


def main():
    s1 = solve1()
    print(f"solution 1: {s1}")

    s2 = solve2()
    print(f"solution 2: {s2}")


if __name__ == "__main__":
    main()