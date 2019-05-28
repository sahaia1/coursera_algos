'''
Problem # 14

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

import random


def get_y(x, r):
    return (r**2 - x**2)**0.5


def get_dist(p1, p2):
    return sum([(a - b)**2 for a, b in zip(p1, p2)])**0.5


def estimate_pi():
    pi = 0
    radius = 1000
    for i in range(1, 11):
        circumfarance_4 = 0
        prev = 0, radius
        for j in range(radius):
            dx = 0
            x = j
            for _ in range(100):
                dx = random.uniform(dx, 1)
                if dx == 1.0:
                    break
                y = get_y(x, radius)
                circumfarance_4 += get_dist(prev, (x, y))
                prev = x, y
        pi = (pi * (i - 1) + (circumfarance_4 / (2 * radius))) / i
        print('Pi So Far - ', 4 * pi)
    return 4 * pi
