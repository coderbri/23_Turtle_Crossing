from turtle import Turtle

def draw_ocean(screen_width=800, ocean_height=120):
    """Draws the ocean area at the top of the screen with space for sand below."""
    ocean = Turtle()
    ocean.hideturtle()
    ocean.penup()
    ocean.goto(-screen_width // 2, 250)  # Raised to make space for sand
    ocean.pendown()
    ocean.color("paleturquoise")
    ocean.begin_fill()
    for _ in range(2):
        ocean.forward(screen_width)
        ocean.left(90)
        ocean.forward(ocean_height)
        ocean.left(90)
    ocean.end_fill()

def draw_waves(screen_width=800):
    """Draws wavy lines to simulate water ripples with fewer waves."""
    waves = Turtle()
    waves.hideturtle()
    waves.penup()
    waves.color("LightCyan")
    waves.pensize(2)

    for y in range(220, 300, 30):  # Increased gap between waves
        waves.goto(-screen_width // 2, y)
        waves.pendown()
        for x in range(-screen_width // 2, screen_width // 2, 40):  # Fewer horizontal segments
            waves.goto(x, y + (5 if (x // 40) % 2 == 0 else -5))  # Reduced wave height
        waves.penup()

def draw_road(screen_width=800, road_height=470):
    """Draws the road where the cars move (-225 to 225)."""
    road = Turtle()
    road.hideturtle()
    road.penup()
    road.goto(-screen_width // 2, -235)  # Adjusted to match car movement area
    road.pendown()
    road.color("LightSlateGray")
    road.begin_fill()
    for _ in range(2):
        road.forward(screen_width)
        road.left(90)
        road.forward(road_height)
        road.left(90)
    road.end_fill()
