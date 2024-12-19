import argparse
import sys
from pathlib import Path
from PIL import Image


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ftype')

    return parser


def image_viewer(file_extension):
    path = Path.cwd()
    for i in (list(path.glob('*'))):
        if i.name.endswith(file_extension):
            with Image.open(i) as img:
                img = img.resize((50, 50))
                img.show()


if __name__ == '__main__':
    print(sys.argv)
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    image_viewer(namespace.ftype)
