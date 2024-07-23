from __future__ import annotations

import argparse
import os
from typing import Sequence


def _fix_file(filename: str) -> bool:
    with open(filename, mode='rb') as file_processed:
        content = file_processed.read()

    if b'\r\n' in content:
        content = content.replace(b'\r\n', b'\n')
        with open(filename, mode='wb') as file_processed:
            file_processed.write(content)
        return True
    return False


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        if _fix_file(filename):
            print(f'Converted DOS newlines to Unix newlines in {filename}')
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
