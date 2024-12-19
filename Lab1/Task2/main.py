import sys
import argparse
from pathlib import Path


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath')
    parser.add_argument('--files', nargs='*')

    return parser


def check_for_transferred_files(dirpath, list_of_files):
    names_of_files = [i.name for i in Path(dirpath).glob("*") if i.is_file()]

    # Если имена файлов на входе отсутствуют.
    if not list_of_files:
        print(f'Количество файлов: {len(names_of_files)}')
        summ = 0
        for i in Path(dirpath).glob("*"):
            if i.is_file():
                summ += i.stat().st_size
        print(f'Общий размер: {summ}')
        return

    existing_files = []
    missing_files = []

    for i in list_of_files:
        if i not in names_of_files:
            missing_files.append(i)
        else:
            existing_files.append(i)

    print('Присутствующие файлы:', *existing_files)
    print('Отсутствующие файлы:', *missing_files)
    with open('existing_files.txt', 'w') as existing:
        existing.write('\n'.join(existing_files))
    with open('missing_files.txt', 'w') as missing:
        missing.write('\n'.join(missing_files))


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    check_for_transferred_files(namespace.dirpath, namespace.files)
