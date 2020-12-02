
def solution():
    with open("input.txt") as f:
        numbers = f.read().split("\n")

    numbers = list(map(int, numbers))

    for i in numbers:
        for j in numbers:
            if (i + j) == 2020:
                return i * j


def main():
    s = solution()

    print(s)


if __name__ == "__main__":
    main()
