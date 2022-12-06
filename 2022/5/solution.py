from operator import itemgetter
from tools import load_input


def split_crates_and_moves(data):
    for i in range(len(data)):
        if data[i] == "":
            break
    return data[:i], data[(i+1):]


def get_crates_stacks(data):
    data = data[:-1]
    rows = []
    for line in data:
        row = []
        for i in range(0, len(line), 4):
            letter = line[i:(i+3)]
            if letter:
                letter = letter[1:-1]
            row.append(letter)
        rows.append(row)
    stacks = list(zip(*rows))
    stacks = [[s for s in stack if s != " "] for stack in stacks]
    return stacks


def run_moves(stacks, moves, keep_order):
    for move in moves:
        quant, from_, to_ = list(itemgetter(*[1, 3, 5])(move.split(" ")))
        quant, from_, to_ = int(quant), int(from_), int(to_)
        items = []
        for i in range(quant):
            items.append(stacks[(from_-1)].pop(0))
        if keep_order:
            items.reverse()
        for item in items:
            stacks[(to_ - 1)].insert(0, item)


def solve1():
    data = load_input("2022/5/1")
    data = data.split("\n")
    crates_rows, moves = split_crates_and_moves(data)
    crates_stacks = get_crates_stacks(crates_rows)
    run_moves(crates_stacks, moves, keep_order=False)
    stack_string = ""
    for s in crates_stacks:
        stack_string += s[0]
    return stack_string


def solve2():
    data = load_input("2022/5/1")  # same input
    data = data.split("\n")
    crates_rows, moves = split_crates_and_moves(data)
    crates_stacks = get_crates_stacks(crates_rows)
    run_moves(crates_stacks, moves, keep_order=True)
    stack_string = ""
    for s in crates_stacks:
        stack_string += s[0]
    return stack_string


def main():
    s1 = solve1()
    print(f"solution 1: {s1}")

    s2 = solve2()
    print(f"solution 2: {s2}")


if __name__ == "__main__":
    main()
