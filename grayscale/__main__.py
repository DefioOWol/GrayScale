"""Summary."""
from pathlib import Path
from os import system

from click import command, option
from grayscale.shades import is_gray, to_gray


@command()
@option('-t', '--test', is_flag=True, default=False,
        show_default=True, help='flag for running tests')
@option('-e', '--example', is_flag=True, default=False,
        show_default=True, help='flag for launching examples')
def main(test: bool, example: bool):
    """Summary."""
    if test:
        system(f'python {Path(__file__).parent}\\tests')
    if example:
        system(f'python {Path(__file__).parent.parent}\\grayscale_example.py')
    if test or example:
        return None

    def print_help():
        """Summary."""
        print('\nCommand menu:')
        print('    stop - complete the program')
        print('    help - output this help message')
        print('    isgray - check if the color is grayscale')
        print('    togray - defines the values needed to bring', end= ' ')
        print('the color to a shade of gray')

    def check_format(color: str) -> bool:
        """Summary."""
        if not color or color[0] != '#' or len(color) != 7:
            return False
        if any(i < '0' or (i > '9' and (i < 'A' or i > 'F'))
               for i in color[1:]):
            return False
        return True

    print_help()
    while (cmd := input('\n>>> ')) != 'stop':
        if cmd == 'help':
            print_help()
        elif cmd in ['isgray', 'togray']:
            print('\nEnter the color in the 16-digit number system', end=' ')
            color = input('(format #HHHHHH)> ')
            if check_format(color):
                if cmd == 'isgray':
                    print(is_gray(color))
                else:
                    print(to_gray(color))
            elif color:
                print('WARNING: incorrect format')
        elif cmd:
            print('WARNING: unknown command')
            print("INFO: use 'help' to output command menu")


if __name__ == '__main__':
    main()
