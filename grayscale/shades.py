"""shades.

The main module of the GrayScale package, containing
functions for working with grayscale.

Functions:
    - is_gray(hex) - grayscale check
    - to_gray(hex) - casting to a shade of gray

"""


def is_gray(hex: str) -> bool:
    """Check if hex is a grayscale.

    Arguments:
        - hex: str - color code in the 16-digit number system, format:
            #HHHHHH, where H is the digit of the 16-digit number system

    Returns True or False depending on the result.

    """
    if hex[0] != '#':
        raise ValueError('the color code should start with #')
    if len(hex) != 7:
        raise ValueError('the color code must consist of seven characters')
    red, green, blue = int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)
    return red == green == blue and red not in [0, 255]


def to_gray(hex: str) -> tuple[int, int, int]:
    """Define the values to be added to hex.

    Determines which values need to be added to
    the hex components so that it becomes a shade of gray.

    Arguments:
        - hex: str - color code in the 16-digit number system, format:
            #HHHHHH, where H is the digit of the 16-digit number system

    Returns a tuple of received values in the 10-digit number system.

    """
    if hex[0] != '#':
        raise ValueError('the color code should start with #')
    if len(hex) != 7:
        raise ValueError('the color code must consist of seven characters')
    red, green, blue = int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)
    mid = red + green + blue - max(red, green, blue) - min(red, green, blue)
    mid = 1 if not mid else 254 if mid == 255 else mid
    return (mid - red, mid - green, mid - blue)
