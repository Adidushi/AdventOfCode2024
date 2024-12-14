import math
import re
from dataclasses import dataclass

from PIL import Image

SIZE_X = 101
SIZE_Y = 103
ITERATIONS = 100


@dataclass
class Robot:
    position: complex
    velocity: complex

    def move(self):
        self.position += self.velocity
        x = self.position.real
        y = self.position.imag
        if not (0 <= x < SIZE_X):
            x %= SIZE_X
        if not (0 <= y < SIZE_Y):
            y %= SIZE_Y
        self.position = x + y * 1j

    def quadrant(self):
        x = self.position.real
        y = self.position.imag
        x_limit = SIZE_X - 1
        y_limit = SIZE_Y - 1
        if x < x_limit / 2 and y < y_limit / 2:
            return 1
        if x < x_limit / 2 and y > y_limit / 2:
            return 2
        if x > x_limit / 2 and y < y_limit / 2:
            return 3
        if x > x_limit / 2 and y > y_limit / 2:
            return 4
        return -1


def q1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    robots: list[Robot] = list()
    for line in data:
        pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r'-?\d+', line))

        position = pos_x + pos_y * 1j
        velocity = vel_x + vel_y * 1j
        robots.append(Robot(position, velocity))

    for _ in range(ITERATIONS):
        for robot in robots:
            robot.move()

    quadrants = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        -1: 0
    }
    for robot in robots:
        quadrants[robot.quadrant()] += 1
    quadrants.pop(-1)
    return math.prod(quadrants.values())


def check_bots(robots):
    positions = set()
    for robot in robots:
        positions.add(robot.position)
    return len(positions) == len(robots)


def q2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    robots: list[Robot] = list()
    for line in data:
        pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r'-?\d+', line))

        position = pos_x + pos_y * 1j
        velocity = vel_x + vel_y * 1j
        robots.append(Robot(position, velocity))
    iteration = 1
    while True:
        for robot in robots:
            robot.move()
        if check_bots(robots):
            return iteration
        iteration += 1


if __name__ == '__main__':
    from time import perf_counter as pc

    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1 - st) * 1000}ms\n\
            Part 2: {(pt2 - pt1) * 1000}ms\n\
            Total: {(pt2 - st) * 1000}ms')
