"""Summary."""


def is_gray(hex: str) -> bool:
    """Summary."""
    if hex[0] != '#':
        raise ValueError('the color code should start with #')
    if len(hex) != 7:
        raise ValueError('the color code must consist of seven characters')
    red, green, blue = int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)
    return red == green == blue and red not in [0, 255]


def to_gray(hex: str) -> tuple[int, int, int]:
    """Summary."""
    if hex[0] != '#':
        raise ValueError('the color code should start with #')
    if len(hex) != 7:
        raise ValueError('the color code must consist of seven characters')
    red, green, blue = int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)
    mid = red + green + blue - max(red, green, blue) - min(red, green, blue)
    mid = 1 if not mid else 254 if mid == 255 else mid
    return (mid - red, mid - green, mid - blue)
