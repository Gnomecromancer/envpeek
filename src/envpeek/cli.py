import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="envpeek",
        description="Windows environment inspector: PATH analysis, missing dirs, duplicates, system vs user vars",
    )
    parser.add_argument("--version", action="version", version="0.1.0")
    args = parser.parse_args()
    print("envpeek: not yet implemented")


if __name__ == "__main__":
    main()
