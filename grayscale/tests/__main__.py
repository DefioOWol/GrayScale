"""Summary."""
from pathlib import Path
from os import system

if __name__ == '__main__':
    system(f'python {Path(__file__).parent}\\doctests.py')
    system(f'pytest -v {Path(__file__).parent}')
