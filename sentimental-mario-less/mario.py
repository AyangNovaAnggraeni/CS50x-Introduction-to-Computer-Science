from cs50 import get_int


def main():
    height = get_height()
    for i in range(height):
        print_row(i + 1, height - i - 1)


def get_height():
    while True:
        height = get_int("height: ")
        if height > 0 and height < 9:
            break
    return height


def print_row(height, space):
    for i in range(space):
        print(" ", end="")

    for i in range(height):
        print("#", end="")
    print()


main()
