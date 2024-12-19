from pathlib import Path
from argparse import ArgumentParser
from skimage import io, transform, util, exposure


def rotate_image(image, angle=45):
    return transform.rotate(image, angle)


def flip_horizontal(image):
    return image[:, ::-1]


def add_noise(image, mode='gaussian'):
    return util.random_noise(image, mode=mode)


def adjust_brightness(image, gamma=1.2):
    return exposure.adjust_gamma(image, gamma)


def resize_image(image, scale=0.8):
    return transform.rescale(image, scale, anti_aliasing=True, channel_axis=-1)


def complex_transformation(image):
    image = rotate_image(image, angle=30)
    image = add_noise(image, mode='s&p')
    return image


def main():
    parser = ArgumentParser()
    parser.add_argument('data_path', type=str)
    parser.add_argument('--rotate', action='store_true')
    parser.add_argument('--flip', action='store_true')
    parser.add_argument('--noise', action='store_true')
    parser.add_argument('--brightness', action='store_true')
    parser.add_argument('--resize', action='store_true')
    parser.add_argument('--complex', action='store_true')
    args = parser.parse_args()

    folder = Path(args.data_path)
    image_files = sorted(folder.glob('*.jpg'))

    # Удаление всех файлов, кроме первых 20 исходных
    for img in image_files[20:]:
        img.unlink()
        print(f"Удалено: {img.name}")

    image_files = image_files[:20]
    next_num = 20

    for img in image_files:
        image = io.imread(img)

        if args.rotate:
            image = rotate_image(image)
        if args.flip:
            image = flip_horizontal(image)
        if args.noise:
            image = add_noise(image)
        if args.brightness:
            image = adjust_brightness(image)
        if args.resize:
            image = resize_image(image)
        if args.complex:
            image = complex_transformation(image)

        # Приведение к диапазону [0, 255]
        if image.dtype == 'float64':
            image = (image * 255).astype('uint8')

        # Сохранение изображения
        new_filename = f"{next_num}.jpg"
        new_path = folder / new_filename
        io.imsave(new_path, image)
        print(f"Сохранено: {new_filename}")
        next_num += 1


if __name__ == "__main__":
    main()
