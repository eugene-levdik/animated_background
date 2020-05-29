import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
from moving_line import MovingLine
import random as r
import cv2


def gen_color_dict(seed, number_of_lines):
    r.seed(seed)
    colors = {}
    for code in range(2, (1 << (number_of_lines + 1))):
        colors.update({code: [r.randint(1, 255), r.randint(1, 255), r.randint(1, 255)]})
    return colors


def area_seed(x, y, time, lines):
    seed = 1
    for moving_line in lines:
        seed = seed << 1
        if moving_line[time].is_right(x, y):
            seed += 1
    return seed


if __name__ == '__main__':
    w, h = 426, 240
    fps = 30
    seconds = 5
    duration = fps * seconds

    number_of_lines = 5
    lines = []
    r.seed(566)
    for i in range(number_of_lines):
        lines.append(MovingLine((h, w), 1, duration, r.random()))

    fourcc = VideoWriter_fourcc(*'MP42')
    video = VideoWriter('C:/Users/eugen_000/Desktop/turbo_background.avi', fourcc, float(fps), (w, h))

    colors = gen_color_dict(r.random, number_of_lines)

    for i in range(duration):
        print(i * 100 / duration, '%')
        frame = np.zeros((h, w, 3), dtype=np.uint8)
        for x in range(h):
            for y in range(w):
                frame[x][y] = colors[area_seed(x, y, i, lines)]
        video.write(frame)

    video.release()
