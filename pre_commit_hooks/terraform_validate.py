import argparse
import subprocess


def run_terraform_validate(directory: str) -> int:
    """Run terraform validate in the given directory."""
    result = subprocess.run(['terraform', 'validate'], cwd=directory)
    return result.returncode


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--directory', '-d', default='.',
        help='The working directory to run terraform validate in.',
    )
    args = parser.parse_args(argv)

    return run_terraform_validate(args.directory)


if __name__ == '__main__':
    raise SystemExit(main())
