import copy
import random


def dict_to_arr(dict):
    contents = []

    for ball, amount in dict.items():
        contents += [ball] * amount

    return contents


def color_counter(colors):
    color_counts = {}

    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    return color_counts


class Hat:
    def __init__(self, **kwargs):
        self.contents = dict_to_arr(kwargs)

    def draw(self, balls: int):
        self.balls_drawn = []

        if balls >= len(self.contents):
            self.balls_drawn = copy.copy(self.contents)
            self.contents = []
        else:
            for _ in range(balls):
                ball_index = random.randrange(len(self.contents))
                self.balls_drawn.append(self.contents.pop(ball_index))

        return self.balls_drawn


def experiment(hat: Hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_successes = 0

    for _ in range(num_experiments):
        balls_drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        balls_counted = color_counter(balls_drawn)

        experiment_succeeded = True

        for color in expected_balls:
            if balls_counted.get(color, 0) < expected_balls[color]:
                experiment_succeeded = False

        if experiment_succeeded:
            experiment_successes += 1

    return experiment_successes / num_experiments
