import random as r


def gen_color(seed):
    primary_r = 120
    disp_r = 50
    primary_g = 50
    disp_g = 10
    primary_b = 150
    disp_b = 50

    r.seed(seed)

    red = r.randint(primary_r - disp_r, primary_r + disp_r)
    red = max(0, red)
    red = min(red, 255)

    green = r.randint(primary_g - disp_g, primary_g + disp_g)
    green = max(0, green)
    green = min(green, 255)

    blue = r.randint(primary_b - disp_b, primary_b + disp_b)
    blue = max(0, blue)
    blue = min(blue, 255)

    return [red, green, blue]


def gen_color_dict(seed, number_of_lines):
    r.seed(seed)
    colors = {}
    n = 1 << (number_of_lines + 1)
    next_print = 0
    for code in range(2, n):
        percentage = round(code * 100 / n, 1)
        if percentage > next_print:
            print('Color dictionary:', percentage, '%')
            next_print += 5
        colors.update({code: gen_color(r.random())})
    return colors
