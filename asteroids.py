
# Asteroids Clone
#Zakaria Abdi

import turtle
import math
import random

#Set up the game screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Asteroids! by @Zakaria")
wn.setup(800, 600)
wn.tracer(0) # Turns off the screen updates for performance


pen = turtle.Turtle()
pen.penup()
pen.speed(0)

class Sprite():
    # Base class for all the moving objects in the game
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        self.active = True
        
    def update(self):
        #Updating the Sprites position
        if self.active:
            self.x += self.dx
            self.y += self.dy
            
            #Wrapping around the screen
            if self.x > 400:
                self.x = -400
            elif self.x < -400:
                self.x = 400
                
            if self.y > 300:
                self.y = -300
            elif self.y < -300:
                self.y = 300
        
    def render(self, pen):
        #rendering the sprite on the screen
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size, self.size, 0)
            pen.color(self.color)
            pen.stamp()
            
    def is_collision(self, other):
        #Check for collision with another sprite
        x = self.x-other.x
        y = self.y-other.y
        distance = ((x**2) + (y**2)) ** 0.5
        if distance < ((10 * self.size) + (10 * other.size)):
            return True
        else:
            return False
            
    def goto(self, x, y):
        #Move the sprite to a new location
        self.x = x
        self.y = y
        
        
class Player(Sprite):
    #Class for the players spaceship
    def __init__(self):
        super().__init__()
        self.shape = "triangle"
        self.score = 0
        self.lives = 3
        
    def rotate_left(self):
        #Rotate the player left
        self.heading += 30
        
    def rotate_right(self):
        #Rotate the player right 
        self.heading -= 30
        
    def accelerate(self):
        #Accelerate the player in the direction its facing 
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx += ax * 0.1
        self.dy += ay * 0.1
        
    def render(self, pen):
        #render the player on the screen
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size/2.0, self.size, 0)
            pen.color(self.color)
            pen.stamp()

class Asteroid(Sprite):
    #Class for asteroids 
    def __init__(self):
        super().__init__()
        self.shape = "circle"

class Missile(Sprite):
    #Class for the missles firef by the player
    def __init__(self):
        super().__init__()
        self.shape = "circle"
        self.size = 0.2
        self.active = False

    def update(self):
        #Update the missle's position
        if self.active:
            self.x += self.dx
            self.y += self.dy
            
            if self.x > 400:
                self.active = False
            elif self.x < -400:
                self.active = False
                
            if self.y > 300:
                self.active = False
            elif self.y < -300:
                self.active = False
        
    def fire(self):
        #Fire the missle from the players current position
        if not self.active:
            self.active = True
            self.x = player.x
            self.y = player.y
            self.heading = player.heading
            self.dx = math.cos(math.radians(self.heading)) * 1
            self.dy = math.sin(math.radians(self.heading)) * 1

# Create sprites list to hold all the sprites 
sprites = []

# Create instances to add to the sprite list 
player = Player()
sprites.append(player)

missile = Missile()
sprites.append(missile)

# Create asteroids to add to the sprites list
for _ in range(5):
    asteroid = Asteroid()
    x = random.randint(-375, 375)
    y = random.randint(-275, 275)
    asteroid.goto(x, y)
    dx = random.randint(-5, 5) / 20.0
    dy = random.randint(-5, 5) / 20.0 
    asteroid.dx = dx
    asteroid.dy = dy
    size = random.randint(10, 30) / 10.0
    asteroid.size = size
    sprites.append(asteroid)

# Keyboard bindings
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeypress(missile.fire, "space")

# Main loop
def main():
    # Update the screen
    wn.update()
    
    # Clear everything the pen did
    pen.clear()

    # Draw Score
    pen.goto(-350, 250)
    pen.write(f"Score: {player.score}", False, font=("Courier New", 18, "normal"))
    
    # Draw Lives
    for i in range(player.lives):
        pen.goto(-350 + 30 * i, 225)
        pen.shape("triangle")
        pen.shapesize(0.7, 0.7, 0)
        pen.setheading(90)
        pen.color("white")
        pen.stamp()
        
    # Render and update sprites
    for sprite in sprites:
        sprite.update()
        sprite.render(pen)
    
    # Check for collisions
    for sprite in sprites:
        if isinstance(sprite, Asteroid):
            if player.is_collision(sprite):
                player.lives -= 1
                print(f"Lives: {player.lives}")
                player.goto(0, 0)
                sprite.goto(100, 100)
                
                if player.lives <= 0:
                    print("PLAYER DIES")
                    player.active = False
                
            if missile.active and missile.is_collision(sprite):
                print("ASTEROID DIES")
                missile.active = False
                player.score += 10
                print(f"Player Score: {player.score}")
                sprite.goto(100, 100)
    
    # Set timer to call main again
    wn.ontimer(main, 20)

# Start the game
main()
wn.mainloop()
