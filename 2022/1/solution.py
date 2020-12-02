from pathlib import Path

HERE = Path(__file__).parent


def calculate_calories_per_elf(data):
    data = data.split("\n\n")
    return [
        sum([int(c) for c in x.split("\n")])
        for x in data
    ]


def solve1():
    data = Path(HERE / "1" / "input.txt").read_text()
    return max(calculate_calories_per_elf(data))


def solve2():
    data = Path(HERE / "2" / "input.txt").read_text()
    data = calculate_calories_per_elf(data)
    data = list(sorted(data, reverse=True))[:3]
    return sum(data)


def main():
    s1 = solve1()
    print(f"solution 1: {s1}")

    s2 = solve2()
    print(f"solution 2: {s2}")


if __name__ == "__main__":
    main()
