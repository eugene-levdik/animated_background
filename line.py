class Line:

    def __init__(self, point1, point2):
        self.point1, self.point2 = point1, point2
        x1, y1 = point1
        x2, y2 = point2

        self.a = y2 - y1
        self.b = x1 - x2
        self.c = y1 * (x2 - x1) - x1 * (y2 - y1)

    def is_right(self, x, y):
        return (self.a * x + self.b * y + self.c) > 0
