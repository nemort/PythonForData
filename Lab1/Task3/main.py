import sys
from pathlib import Path


def create_files(list_of_files, directory):
    Path(directory).mkdir(parents=True, exist_ok=True)

    for i in list_of_files:
        try:
            file = open(directory + '\\' + i, 'w')
        finally:
            file.close()


if __name__ == '__main__':
    directory = sys.argv[1]

    with open(r'..\Task2\missing_files.txt', 'r') as file:
        files = file.read().splitlines()

    create_files(files, directory)
