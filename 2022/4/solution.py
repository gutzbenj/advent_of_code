from tools import load_input
import string


def get_sections(pairs):
    p1, p2 = pairs.split(",")
    p1_range = p1.split("-")
    p2_range = p2.split("-")
    p1_set = set(range(int(p1_range[0]), int(p1_range[1])+1, 1))
    p2_set = set(range(int(p2_range[0]), int(p2_range[1])+1, 1))
    return p1_set, p2_set


def is_contained(s1, s2):
    return s1.issubset(s2) or s2.issubset(s1)


def is_overlapped(s1, s2):
    return bool(s1.intersection(s2))


def solve1():
    data = load_input("2022/4/1")
    data = data.split("\n")
    data = [
        is_contained(*get_sections(d))
        for d in data
    ]
    return sum(data)


def solve2():
    data = load_input("2022/4/1")  # same input
    data = data.split("\n")
    data = [
        is_overlapped(*get_sections(d))
        for d in data
    ]
    return sum(data)


def main():
    s1 = solve1()
    print(f"solution 1: {s1}")

    s2 = solve2()
    print(f"solution 2: {s2}")


if __name__ == "__main__":
    main()
