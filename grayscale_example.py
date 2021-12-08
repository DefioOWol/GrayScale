"""Summary."""
from click import command, argument, IntRange
from grayscale.shades import is_gray, to_gray


def is_gray_first_example():
    """Summary."""
    print('\n' + '=' * 42)
    print("""print(is_gray('#F0F0F0'))
print(is_gray('#808080'))
print(is_gray('#424242'))
print(is_gray('#010101'))
print(is_gray('#A9A9A9'))""")
    print('-' * 42)

    print(is_gray('#F0F0F0'))
    print(is_gray('#808080'))
    print(is_gray('#424242'))
    print(is_gray('#010101'))
    print(is_gray('#A9A9A9'))

    print('=' * 42)


def is_gray_second_example():
    """Summary."""
    print('\n' + '=' * 42)
    print("""print(is_gray('#FFFFFF'))
print(is_gray('#000000'))
print(is_gray('#435612'))
print(is_gray('#130303'))
print(is_gray('#777787'))""")
    print('-' * 42)

    print(is_gray('#FFFFFF'))
    print(is_gray('#000000'))
    print(is_gray('#435612'))
    print(is_gray('#130303'))
    print(is_gray('#777787'))

    print('=' * 42)


def to_gray_example():
    """Summary."""
    print('\n' + '=' * 42)
    print("""print(to_gray('#FFFFFF'))
print(to_gray('#000000'))
print(to_gray('#435612'))
print(to_gray('#130303'))
print(to_gray('#777787'))
print(to_gray('#808080'))
print(to_gray('#A9A9A9'))""")
    print('-' * 42)

    print(to_gray('#FFFFFF'))
    print(to_gray('#000000'))
    print(to_gray('#435612'))
    print(to_gray('#130303'))
    print(to_gray('#777787'))
    print(to_gray('#808080'))
    print(to_gray('#A9A9A9'))

    print('=' * 42)


@command()
@argument('numbers', type=IntRange(0, 3), nargs=-1)
def main(numbers: tuple[int]):
    """Summary."""
    example_functions = {
        1: is_gray_first_example, 2: is_gray_second_example,
        3: to_gray_example
    }
    if not numbers:
        numbers = (0,)
    if 0 in numbers:
        for func in example_functions.values():
            func()
    else:
        for number in numbers:
            example_functions[number]()


if __name__ == '__main__':
    main()
