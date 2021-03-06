input = []

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        input.append(int(line))


def day_one_part_one(input):
    print("The answer to part one is ", sum(input))


def day_one_part_two(input):
    part_one = 0
    part_two = 0
    frequency = set()

    while part_two == 0:

        for number in input:
            part_one = part_one + number

            if part_one in frequency:
                part_two = part_one
                break
            else:
                frequency.add(part_one)

    print("The answer to part two is ", part_two)


if __name__ == "__main__":
    day_one_part_one(input)
    day_one_part_two(input)
