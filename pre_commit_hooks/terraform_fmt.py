import argparse
import subprocess
from typing import Sequence


def run_terraform_fmt(filenames: list[str]) -> int:
    """Run terraform fmt on the given files."""
    for filename in filenames:
        result = subprocess.run(['terraform', 'fmt', filename])
        if result.returncode != 0:
            return result.returncode
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    args = parser.parse_args(argv)

    return run_terraform_fmt(args.filenames)


if __name__ == '__main__':
    raise SystemExit(main())
