"""__main__.

Tests package module designed to start execution
all tests that are in this package.

Imports:
    - from pathlib import Path - to extract the path to the file
    - from os import system - to run tests

"""
from pathlib import Path
from os import system

if __name__ == '__main__':
    system(f'python {Path(__file__).parent}\\doctests.py')
    system(f'pytest -v {Path(__file__).parent}')
