"""GrayScale package initialization module.

The GrayScale package is designed to work with shades of gray, namely,
it checks whether a color is a shade of gray and how many values need
to be added to its components to make it so. The shades are taken from
the RGB palette, and the color codes are written in a 16-digit number
system.

The package can be launched from the console as an independent program
using the 'grayscale' command. It is also possible to set the
-t (--test) and -e (--example) flags, which will start the execution
of tests and examples of functions of the main module.

For the correct operation of this package, the modules click, pytest and
coverage are required. The first is necessary to provide a CLI for some
modules of the package, the second is needed to run tests, the third is
needed to check the code coverage with tests. In addition, the modules
of this package import unittest module and functions from os, pathlib
and doctest modules.

Content:

    Main modules:
        - __init__ - package initialization
        - __main__ - ensuring the independent operation of the package
        - shades - contains functions for working with shades of gray

    Additional modules:
        - grayscale_example - contains examples of the functions of the main
            module (lies on the same level with the package)

    Subpackages:
        - tests - a package of tests of the functions of the main module

"""

__all__ = ['shades']
