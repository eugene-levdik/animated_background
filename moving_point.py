import random as r
import math as m


class MovingPoint:

    def __init__(self, screensize, speed, duration, point_seed, init_pos=None):
        w, h = screensize
        r.seed(point_seed)
        if init_pos is None:
            x = r.random() * w
            y = r.random() * h
        else:
            x, y = init_pos
        angle = r.random() * 2 * m.pi
        self.path = []
        self.path.append(tuple(map(int, (x, y))))

        for _ in range(1, duration):
            vx = speed * m.cos(angle)
            vy = speed * m.sin(angle)
            x += vx
            y += vy
            self.path.append(tuple(map(int, (x, y))))
            angle += ((r.random()) + 1) * m.pi * speed / 100

    def __getitem__(self, item):
        return self.path[item]

    def __len__(self):
        return len(self.path)


if __name__ == '__main__':
    point = MovingPoint((1280, 720), 3, 100, 566)
    for i in range(len(point)):
        print(i, point[i][0], point[i][1], sep='\t')
