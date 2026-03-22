import argparse
from build import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--drafts", action="store_true")
    args = parser.parse_args()
    main(args)
