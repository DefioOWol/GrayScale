# GrayScale

GrayScale is a package written in Python and designed to work with
[shades of gray](https://en.wikipedia.org/wiki/Grey), namely, it checks
whether a color is a shade of gray and how many values need to be added
to its components to make it so. The shades are taken from the
[RGB](https://en.wikipedia.org/wiki/RGB_color_model) palette,
and the color codes are written in a 16-digit number system.

## Requirements
![](https://img.shields.io/badge/python-%20%3E%3D%203.7-yellow)  
This package was written in Python versions at least 3.7, so in order to
avoid errors and incorrect work requires Python >= 3.7.  

![](https://img.shields.io/badge/click-%3E%3D%208.0.0-blue)
![](https://img.shields.io/badge/pytest-%20%3E%3D%206.2.0-success)
![](https://img.shields.io/badge/coverage-%20%3E%3D%206.2-red)  
Together with the package will be installed and its dependencies:
modules click >= 8.0.0, pytest >= 6.2.0 and coverage >= 6.2.

## Installation

The package can be installed with the following command in the console:
```
pip install grayscale
```

To remove the package, replace install with uninstall in the above command.

## Usage

The package contains one main module - shades, which contains the necessary
functions for the implementation of the above functionality:
- is_gray - checks whether the specified color is a shade of gray  
    _For example_:
    ```Python
    >>> from grayscale.shades import is_gray
    >>> is_gray('#F0F0F0')
    True
    >>> is_gray('#808080')
    True
    >>> is_gray('#171717')
    True
    >>> is_gray('#231223')
    False
    >>> is_gray('#FFFFFF')
    False
    >>> is_gray('#000000')
    False
    ```

- to_gray - determines how much to add to the components of the specified
    color so that it becomes a shade of gray  
    _For example_:
    ```Python
    >>> from grayscale.shades import to_gray
    >>> to_gray('#F0F0F0')
    (0, 0, 0)
    >>> to_gray('#231223')
    (0, 17, 0)
    >>> to_gray('#424536')
    (0, -3, 12)
    >>> to_gray('#FFFFFF')
    (-1, -1, -1)
    >>> to_gray('#000000')
    (1, 1, 1)
    ```
    > Remark: the color codes are written in the 16-digit number system,
    > while the to_gray function returns values in the 10-digit number system.

In addition, the package can be launched from the console as an independent
program using the command:
```
grayscale
```

It is also possible to install flags -t (--test) and (or) -e (--example),
which will launch tests and (or) examples respectively:
```
grayscale -t -e
```
 
For more information, see the documentation of the modules and
functions themselves.

## License
![](https://img.shields.io/badge/license-MIT-success)
This package is licensed in accordance with the MIT license - see details
in the LICENSE.txt file.

## Contact information

Author: Vyacheslav Velger  
Email: vyvelger@yandex.ru
