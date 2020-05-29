import random as r
from line import Line
from moving_point import MovingPoint


class MovingLine:

    def __init__(self, screensize, speed, duration, line_seed):
        r.seed(line_seed)
        point1 = MovingPoint(screensize, speed, duration, r.random())
        point2 = MovingPoint(screensize, speed, duration, r.random())
        self.line_path = []
        for i in range(duration):
            self.line_path.append(Line(point1[i], point2[i]))

    def __getitem__(self, item):
        return self.line_path[item]

    def __len__(self):
        return len(self.line_path)
