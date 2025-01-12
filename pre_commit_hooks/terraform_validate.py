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
    # Use `parse_known_args` to handle unexpected arguments like `.tf` files
    args, unknown = parser.parse_known_args(argv)

    # Filter out .tf files if needed (not strictly required now)
    unknown = [arg for arg in unknown if not arg.endswith('.tf')]

    # Run validation in the specified directory
    return run_terraform_validate(args.directory)


if __name__ == '__main__':
    raise SystemExit(main())
