import cv2
from json import load, dump
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(img, rgb=True, save_name='', height=256):
    if rgb:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    width = int(height / img.shape[0] * img.shape[1])
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    if save_name:
        cv2.imwrite(save_name, resized)
    return resized


def reshape(img, to_wool=True, save=True):
    if to_wool:
        with open('wool_colors.json', 'r') as file:
            wool_colors = load(file)

    final_wools = []

    for i, row in enumerate(img):
        final_wools.append([])
        for color in row:
            diff = []
            for value in wool_colors.values():
                diff.append(30 * (color[0] - value[0]) ** 2 +
                            59 * (color[1] - value[1]) ** 2 +
                            11 * (color[2] - value[2]) ** 2)
            sum_wool_color = min(diff)

            index = diff.index(sum_wool_color)
            final_color = list(wool_colors.values())[index]
            final_wools[i].append(index)

    final_wools.reverse()

    if save:
        with open('image.json', 'w') as file:
            dump(final_wools, file)

    return final_wools
