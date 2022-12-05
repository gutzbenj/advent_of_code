from tools import load_input
import string


LOWERCASE_UPPERCASE = string.ascii_lowercase + string.ascii_uppercase


def split_supply(supply):
    half = int(len(supply) / 2)
    return supply[:half], supply[half:]


def find_item_from_supplies(s1, s2):
    return set(s1).intersection(set(s2)).pop()


def find_item_from_rucksacks(r1, r2, r3):
    return set(r1).intersection(set(r2)).intersection(set(r3)).pop()


def get_priority(item):
    return LOWERCASE_UPPERCASE.index(item) + 1


def solve1():
    data = load_input("2022/3/1")
    data = data.split("\n")
    data = [
        get_priority(find_item_from_supplies(*split_supply(s)))
        for s in data
    ]
    return sum(data)


def solve2():
    data = load_input("2022/3/1")  # same input
    data = data.split("\n")
    rucksack_groups = []
    for i in range(0, len(data), 3):
        rucksack_groups.append(data[i:(i+3)])
    data = [
        get_priority(find_item_from_rucksacks(*r))
        for r in rucksack_groups
    ]
    return sum(data)


def main():
    s1 = solve1()
    print(f"solution 1: {s1}")

    s2 = solve2()
    print(f"solution 2: {s2}")


if __name__ == "__main__":
    main()
