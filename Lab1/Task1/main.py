from pathlib import Path
from glob import glob
import shutil
import sys


def find_and_copy_small_files(directory):
    # Удаление папки small, если уже была создана.
    if 'small' in list(glob('*')):
        for i in list(Path('small').glob('*')):
            Path.unlink(i)
        Path.rmdir(Path('small'))

    flag = False
    for i in (list(Path(directory).glob('*'))):
        if i.stat().st_size < 2048 and i.is_file():
            flag = True
            print(i.name)
            Path("small").mkdir(parents=True, exist_ok=True)
            shutil.copy(i, "small")
    if not flag:
        print('Файлы менее 2КБ отсутствуют')


if __name__ == "__main__":
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = Path.cwd()

    find_and_copy_small_files(directory)


