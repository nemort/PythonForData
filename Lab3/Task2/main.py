import matplotlib.pyplot as plt
from PIL import Image
from skimage import io


# Функция для получения общей гистограммы с помощью Pillow
def plot_overall_histogram(image, axs):
    img = Image.open(image)
    histogram = img.histogram()

    axs[1].bar(range(256), histogram[:256], color='red', alpha=0.6, label='R')
    axs[1].bar(range(256), histogram[256:512], color='green', alpha=0.6, label='G')
    axs[1].bar(range(256), histogram[512:], color='blue', alpha=0.6, label='B')
    axs[1].set_title('Гистограмма изображения')
    axs[1].legend()


# Функция для построения гистограммы для R, G, B каналов
def plot_rgb_histograms(image, axs):
    # Разбиваем изображение на каналы
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    axs[0].imshow(image)
    axs[0].axis('off')
    axs[0].set_title('Исходное изображение')

    axs[2].hist(r.ravel(), bins=256, color='red', alpha=0.5)
    axs[2].set_title('Гистограмма R-канала')

    axs[3].hist(g.ravel(), bins=256, color='green', alpha=0.5)
    axs[3].set_title('Гистограмма G-канала')

    axs[4].hist(b.ravel(), bins=256, color='blue', alpha=0.5)
    axs[4].set_title('Гистограмма B-канала')


def main(image):
    fig, axs = plt.subplots(1, 5, figsize=(25, 5))

    plot_overall_histogram(image, axs)

    image = io.imread(image)
    plot_rgb_histograms(image, axs)

    plt.tight_layout()
    plt.savefig('histograms.jpg')
    plt.show()


if __name__ == '__main__':
    filename = 'puppy.jpg'
    main(filename)
