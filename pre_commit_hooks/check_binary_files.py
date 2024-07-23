from __future__ import annotations

import argparse
import subprocess
from typing import Sequence


def is_binary(filename: str) -> bool:
    """Check if a file is binary by calling the `file` command."""
    result = subprocess.run(['file', filename], stdout=subprocess.PIPE, encoding='utf-8')
    return 'ELF' in result.stdout or 'PE32' in result.stdout or 'Mach-O' in result.stdout


def find_binary_files(filenames: set[str]) -> int:
    binary_files = [filename for filename in filenames if is_binary(filename)]

    if binary_files:
        for filename in binary_files:
            print(f'Binary file: {filename}')
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    args = parser.parse_args(argv)

    return find_binary_files(set(args.filenames))


if __name__ == '__main__':
    raise SystemExit(main())
