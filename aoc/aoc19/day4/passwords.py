"""Find all the passwords matching conditions
"""


def test_identical_adjacent_digits(number):
    previous_digit = None
    for digit in str(number):
        if digit == previous_digit:
            return True
        previous_digit = digit
    return False


def test_increasing_digits(number):
    previous_digit = 0
    for digit in str(number):
        digit = int(digit)
        if digit < previous_digit:
            return False
        previous_digit = digit
    return True


def test_identical_pair_only(number):
    previous_digit = None
    group = ""

    for digit in str(number) + "x":
        if digit == previous_digit:
            group += str(digit)
        else:
            if len(group) == 1:
                return True
            group = ""
        previous_digit = digit
    return False


def main():
    matching = 0
    for password in range(248345, 746315 + 1):
        if (
            test_identical_adjacent_digits(password)
            and test_increasing_digits(password)
            and test_identical_pair_only(password)
        ):
            matching += 1
    print(matching)


if __name__ == "__main__":
    main()
