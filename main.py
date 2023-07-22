from typing import List


def print_error_message() -> None:
    print()
    print("Number must NOT contain spaces.")
    print("Number must NOT contain letters.")
    print("Number must NOT contain symbols.")
    print("Number must NOT be a decimal number.")
    print("Number must NOT be a negative integer.")
    print("Number must NOT be an even integer.")
    print("Number must NOT be blank.")
    print()


def validate_input(text_input: str) -> bool:
    trimmed_input = text_input.strip()

    if trimmed_input.startswith('-'):
        print_error_message()
        return False
    else:
        for i in range(len(trimmed_input)):
            if trimmed_input[i].isnumeric():
                continue
            else:
                print_error_message()
                return False
            # Defining main function

    first_char = trimmed_input[0]
    if first_char == '1' or first_char == '3' or first_char == '5' or first_char == '7' or first_char == '9':
        return True
    else:
        print_error_message()
        return False


def get_user_input() -> int:
    while True:
        text_input = input("Enter an odd integer: ")

        if len(text_input) == 0:
            print_error_message()
            continue

        if validate_input(text_input):
            user_input = int(text_input.strip())
            if user_input % 2 == 0:
                print_error_message()
                continue
            else:
                return user_input


def initial_square_array(square_array: List[List[str]], odd_int: int, input: str) -> None:
    for i in range(odd_int):
        for j in range(odd_int):
            square_array[i][j] = input


def fill_square_array(square_array: List[List[str]], odd_int: int, index: int, input: str) -> None:
    for i in range(index, int(odd_int / 2), 2):
        for j in range(i, odd_int - i):
            square_array[i][j] = input
            square_array[odd_int - 1 - i][j] = input
            square_array[j][i] = input
            square_array[j][odd_int - 1 - i] = input


def print_square_array(square_array: List[List[str]], odd_int: int) -> None:
    for i in range(odd_int):
        for j in range(odd_int):
            print(square_array[i][j], end="")
            print("", end="")
        print()


def print_pattern(square_array: List[List[str]], odd_int: int) -> None:
    X = 'X'
    space = " "
    if odd_int % 4 == 1:
        initial_square_array(square_array, odd_int, space)
        fill_square_array(square_array, odd_int, 0, X)
    else:
        initial_square_array(square_array, odd_int, X)
        fill_square_array(square_array, odd_int, 1, space)
    print_square_array(square_array, odd_int)


def main():
    odd_int = get_user_input()
    square_array = [["" for j in range(odd_int)] for i in range(odd_int)]
    print_pattern(square_array, odd_int)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
