from tools import load_input


def get_chunk(data, size):
    for i in range(len(data)):
        yield data[i:(i+size)]


def is_len_marker(data, size):
    return len(set(data)) == size


def solve1():
    size = 4
    data = load_input("2022/6/1")
    for packet in get_chunk(data, size):
        if is_len_marker(packet, size):
            return data.index(packet) + size


def solve2():
    size = 14
    data = load_input("2022/6/1")  # same input
    for packet in get_chunk(data, size):
        if is_len_marker(packet, size):
            return data.index(packet) + size


def main():
    s1 = solve1()
    print(f"solution 1: {s1}")

    s2 = solve2()
    print(f"solution 2: {s2}")


if __name__ == "__main__":
    main()
