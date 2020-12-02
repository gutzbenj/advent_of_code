
def solution():
    with open("input.txt") as f:
        numbers = f.read().split("\n")

    numbers = list(map(int, numbers))

    for i in numbers:
        for j in numbers:
            for k in numbers:
                if (i + j + k) == 2020:
                    return i * j * k


def main():
    s = solution()

    print(s)


if __name__ == "__main__":
    main()
