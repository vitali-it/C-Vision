import os


def init_data(path):
    categories = os.listdir(path)
    img_size = 32
    norm = 255.0
    return [categories, img_size, norm]
