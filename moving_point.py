import random as r
import math as m


class MovingPoint:

    def __init__(self, screensize, speed, duration, point_seed):
        w, h = screensize
        r.seed(point_seed)
        x, y = r.random() * w, r.random() * h
        angle = r.random() * 2 * m.pi
        self.path = []
        self.path.append(tuple(map(int, (x, y))))

        for _ in range(1, duration):
            vx = speed * m.cos(angle)
            vy = speed * m.sin(angle)
            x += vx
            y += vy
            self.path.append(tuple(map(int, (x, y))))
            angle += (r.random()) * m.pi * speed / 30

    def __getitem__(self, item):
        return self.path[item]

    def __len__(self):
        return len(self.path)


if __name__ == '__main__':
    point = MovingPoint((1280, 720), 3, 100, 566)
    for i in range(len(point)):
        print(i, point[i][0], point[i][1], sep='\t')
