import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
from moving_line import MovingLine
import random as r
import cv2
from color_factory import gen_color_dict


def area_seed(x, y, time, lines):
    seed = 1
    for moving_line in lines:
        seed = seed << 1
        if moving_line[time].is_right(x, y):
            seed += 1
    return seed


if __name__ == '__main__':
    w, h = 1280, 720
    fps = 30
    seconds = 3
    duration = fps * seconds
    speed = 0.5

    number_of_lines = 15
    lines = []
    r.seed(3)
    for i in range(number_of_lines):
        lines.append(MovingLine((w, h), speed, duration, r.random()))

    fourcc = VideoWriter_fourcc(*'mp4v')
    video = VideoWriter('C:/Users/eugen_000/Desktop/turbo_background.avi', fourcc, float(fps), (w, h))

    colors = gen_color_dict(r.random(), number_of_lines)

    for i in range(duration):
        print('Animation:', round(i * 100 / duration, 1), '%')
        frame = np.zeros((h, w, 3), dtype=np.uint8)
        for y in range(h):
            cross_points = [0, w]
            for moving_line in lines:
                line = moving_line[i]
                cross_point = line.cross_ordinate(y)
                if cross_point is None:
                    continue
                cross_points.append(cross_point)
            cross_points.sort()
            for j in range(len(cross_points) - 1):
                x_1 = cross_points[j]
                x_2 = cross_points[j + 1]
                segment_color = colors[area_seed((x_1 + x_2) / 2, y, i, lines)]
                cv2.line(frame, (x_1, y), (x_2, y), segment_color)
            # for x in range(w):
            #     frame[y][x] = colors[area_seed(x, y, i, lines)]
        # cv2.blur(frame, (100, 100))
        back = cv2.imread('images/720.jpg')
        final_frame = cv2.addWeighted(frame, 0.5, back, 0.5, 1)
        # cv2.imshow('a', final_frame)
        # cv2.waitKey(0)
        # exit()
        video.write(final_frame)

    video.release()
    print('100% Complete!')
