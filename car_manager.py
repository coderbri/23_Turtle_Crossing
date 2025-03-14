import random
from turtle import Turtle

COLORS = ["#FCC1C1", "#FCDFC1", "#FCFCC1", "#C1FCDF", "#C1E0FC", "#C1C2FC"]
COLORS_OUTLINE = ["red", "orange", "goldenrod", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # ? Initial speed of the cars
MOVE_INCREMENT = 5          # ? Speed increase per level

class CarManager:

    def __init__(self):
        """Initialize the CarManager with an empty list of cars."""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly generates a car and adds it to the game.
        A new car is created only 1 out of every 6 game loops to prevent overcrowding.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS_OUTLINE), random.choice(COLORS))

            random_y = random.randint(-225, 225)
            new_car.goto(300, random_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars leftward across the screen."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the speed of cars when the player reaches the finish line."""
        self.car_speed += MOVE_INCREMENT
