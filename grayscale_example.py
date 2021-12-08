"""grayscale_example.

The module of the GrayScale package containing examples of the
functions of the main module.

Each example displays the main executable code and its result.

When running this module from the command line, you can specify
the numbers of tests that will be executed. By default, all
examples are executed.

Imports:
    - from click import command, argument, IntRange - to provide a CLI
        to this module
    - from grayscale.shades import is_gray, to_gray - functions whose
        examples of work are given

Functions:
    - is_gray_first_example() - the first example of the is_gray function
    - is_gray_second_example() - the second example of the is_gray function
    - to_gray_example() - example of the to_gray function
    - main(numbers) - calls the selected examples to execute

"""
from click import command, argument, IntRange
from grayscale.shades import is_gray, to_gray


def is_gray_first_example():
    """Show the first example of the is_gray function."""
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
    """Show the second example of the is_gray function."""
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
    """Show an example of the to_gray function."""
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
    """Allow you to select examples from the list below to execute.

    Examples:
        0. all examples
        1. is_gray_first_example
        2. is_gray_second_example
        3. to_gray_example

    Arguments:
        - numbers: tuple[int] - example numbers for execution

    """
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
