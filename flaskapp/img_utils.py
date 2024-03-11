import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def alt_horizontal(image: np.ndarray, size: int):
    image1 = image.copy()
    height = image.shape[0]
    n_bars = height // (2 * size)
    for i in range(n_bars):
        beg = 2 * i * size
        mid = beg + size
        end = mid + size
        image1[beg:mid, :, :] = image[mid:end, :, :]
        image1[mid:end, :, :] = image[beg:mid, :, :]

    rem = height - n_bars * size * 2
    if rem > size:
        beg = n_bars * size * 2
        mid1 = beg + size
        mid2 = beg + (rem - size)
        end = height
        image1[beg:mid1, :, :] = image[mid2:end, :, :]
        image1[mid1:end, :, :] = image[beg:mid2, :, :]

    return image1


def alt_vertical(image: np.ndarray, size: int):
    image1 = image.copy()
    width = image.shape[1]
    n_bars = width // (2 * size)
    for i in range(n_bars):
        beg = 2 * i * size
        mid = beg + size
        end = mid + size
        image1[:, beg:mid, :] = image[:, mid:end, :]
        image1[:, mid:end, :] = image[:, beg:mid, :]

    rem = width - n_bars * size * 2
    if rem > size:
        beg = n_bars * size * 2
        mid1 = beg + size
        mid2 = beg + (rem - size)
        end = width
        image1[:, beg:mid1, :] = image[:, mid2:end, :]
        image1[:, mid1:end, :] = image[:, beg:mid2, :]

    return image1


def alt_both(image: np.ndarray, size: int):
    image1 = alt_horizontal(image, size)
    image2 = alt_vertical(image1, size)
    return image2


def img_alt(in_fname: str, out_fname: str, size: int, horizontal: bool, vertical: bool):
    image_in = Image.open(in_fname)
    image0 = np.array(image_in)
    if horizontal and vertical:
        image1 = alt_both(image0, size)
    elif horizontal:
        image1 = alt_horizontal(image0, size)
    elif vertical:
        image1 = alt_vertical(image0, size)
    else:
        image1 = image0.copy()

    image_out = Image.fromarray(image1)
    image_out.save(out_fname)


def img_size(fname: str):
    image = Image.open(fname)
    return image.width, image.height


def img_resize(fname: str, new_width: int):
    image = Image.open(fname)
    w, h = image.width, image.height
    ratio = w / h
    new_height = int(new_width / ratio)
    image0 = np.array(image.resize((new_width, new_height)))
    image = Image.fromarray(image0)
    image.save(fname)


def make_hist(in_fn: str, out_fn: str):
    image = Image.open(in_fn)

    (w, h) = image.size
    wh = w * h

    r = np.array(image.getchannel(0)).reshape((wh,))
    g = np.array(image.getchannel(1)).reshape((wh,))
    b = np.array(image.getchannel(2)).reshape((wh,))

    r_hist = [0 for _ in range(256)]
    g_hist = [0 for _ in range(256)]
    b_hist = [0 for _ in range(256)]

    for p in r:
        r_hist[p] += 1

    for p in g:
        g_hist[p] += 1

    for p in b:
        b_hist[p] += 1

    for i in range(256):
        r_hist[i] /= (wh) * 100
        g_hist[i] /= (wh) * 100
        b_hist[i] /= (wh) * 100

    plt.plot(r_hist, color="red")
    plt.plot(g_hist, color="green")
    plt.plot(b_hist, color="darkblue")
    plt.savefig(out_fn)
    plt.close()
