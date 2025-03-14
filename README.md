# 23 Turtle Crossing [CAPSTONE PROJECT]

**Turtle Crossing** is a simple arcade-style game built using Python's Turtle module. The objective is to navigate a turtle safely across a busy road while avoiding incoming cars. Each successful crossing increases the difficulty by speeding up the cars.

---

## Concepts Implemented

- **Object-Oriented Programming (OOP):** Encapsulation, inheritance, and modularization using separate classes for the player, cars, and game logic.

- **Game Loop & Event Handling:** Utilizing Python's `while` loop and `screen.onkeypress()` for real-time user interactions.

- **Collision Detection:** Checking if the player collides with a car to trigger the game-over sequence.

- **Randomization:** Randomly generating cars along the y-axis to create unpredictable obstacles.

- **Incremental Difficulty:** Increasing car speed as the player progresses to higher levels.

---

## Gameplay Mechanics

1. The turtle moves forward when pressing the "Up" key ("W"). It can only move forward, not back, left, or right.

2. Cars are randomly generated along the y-axis and move from the right edge of the screen to the left.

3. When the turtle reaches the top edge of the screen, it resets to the starting position, and the player levels up. Each new level increases the speed of the cars.

4. If the turtle collides with a car, the game ends.


## How to Run the Game

1. Ensure Python is installed on your system. If not, download Python from python.org.

2. Clone this repository.

3. Run the game script:

    - On Windows:
        ```py
        python main.py
        ```
    
    - On MacOS:
        ```py
        python3 main.py
        ```

<div align="center">
<img src="./imgs/23-TurtleCrossing-Demo.gif"
    alt="Turtle Crossing - Demo"
    width="400px" height="auto">
</div>

---
<section align="center">
  <code>coderBri © 2025</code>
</section>