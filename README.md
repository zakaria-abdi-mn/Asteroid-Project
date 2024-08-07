Asteroids Clone
===============

Created by Zakaria Abdi

Description:
------------
This is a simple Asteroids clone game written in Python using the turtle graphics library. The objective of the game is to control a spaceship, avoid collisions with asteroids, and destroy them using missiles.

Requirements:
-------------
- Python 3.x
- turtle graphics library (comes pre-installed with Python)

How to Run:
-----------
1. Make sure you have Python 3 installed on your computer.
2. Save the provided game code in a file named `asteroids.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory where `asteroids.py` is saved using the `cd` command.
   Example: `cd /path/to/directory`
5. Run the game by typing `python3 asteroids.py` in the terminal or command prompt.

Game Controls:
--------------
- Left Arrow Key: Rotate the spaceship left
- Right Arrow Key: Rotate the spaceship right
- Up Arrow Key: Accelerate the spaceship
- Spacebar: Fire a missile

Game Objective:
---------------
- Control the spaceship to avoid collisions with asteroids.
- Destroy asteroids by firing missiles.
- The player starts with 3 lives. A life is lost each time the spaceship collides with an asteroid.
- The game ends when the player loses all lives.

Files:
------
- `asteroids.py`: Main game code file

Code Overview:
--------------
- `Sprite`: Base class for all moving objects in the game. Includes methods for updating position, rendering, collision detection, and moving to new locations.
- `Player`: Inherits from `Sprite` and represents the player's spaceship. Includes methods for rotating, accelerating, and rendering the player.
- `Asteroid`: Inherits from `Sprite` and represents the asteroids in the game.
- `Missile`: Inherits from `Sprite` and represents the missiles fired by the player. Includes methods for updating position and firing the missile.
- `main()`: Main game loop that updates the screen, clears the pen's drawings, draws the score and lives, updates and renders all sprites, checks for collisions, and schedules the next call to itself.

Enjoy the game!
