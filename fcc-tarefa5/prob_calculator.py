import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents += [color] * count
    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        balls_drawn = random.sample(self.contents, num_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        drawn_dict = {color: balls_drawn.count(color) for color in set(balls_drawn)}
        success = True
        for color, count in expected_balls.items():
            if drawn_dict.get(color, 0) < count:
                success = False
                break
        if success:
            m += 1
    probability = m / num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)