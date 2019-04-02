from pygame.locals import *
import pygame
import time
from random import randint

grid_size = 44

class Apple:
    x = 0
    y = 0
 
    def __init__(self,x,y):
        self.x = x * grid_size
        self.y = y * grid_size

class Player:
  x = []
  y = []
  speed = 1
  step = grid_size
  
  # The direction the snake is currently moving. Note that we'll never move diagonally. 
  x_direction = 1  
  y_direction = 0   
  length = 3

  def __init__(self, length):
    self.length = length
    for i in range(0,length):
      self.x.append(0)
      self.y.append(0)
    self.update()

  def update(self):
 
 
    # update previous positions. This for loop iterates from the last node to the first,
    # updating each node to be the value of the subsequent node
    for i in range(self.length-1,0,-1):
      self.x[i] = self.x[i-1]
      self.y[i] = self.y[i-1]

    # update position of head of snake
    self.x[0] = self.x[0] + (self.step * self.x_direction)
    self.y[0] = self.y[0] + (self.step * self.y_direction)


  def __str__(self):
    return "self.x[" + str(self.x[0]) + "] = self.x[" + str(self.y[0]) + "]"

  # We can call this with positive or negative numbers for x or y
  # to move the player  right, left, up, or down.
  def move(self, x, y):    
    self.x_direction = x
    self.y_direction = y

# Setting up the class for our games
class App:
  windowWidth = 800
  windowHeight = 600
  player = 0

  # Our app's constructor
  def __init__(self):
    self._running = False
    self._player_image = None   # We'll store the image we'll use for the player here
    self._apple_image = None
    self._display = None        # This will be the window we display everything on
    self.player = Player(3)      # Creating a new player object. This calls that __init__ thing!
    self.apple = Apple(5,5)

  # This will be the function we call to start our game! It should only be called once!
  def on_execute(self):
    pygame.init() # Initializing our pygame object

    # Setting up our display. We'll use this to render our game:
    self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

    # This "titles" our game
    pygame.display.set_caption('Hacksu Snake! 🐍')

    # Setting up our player image
    self._player_image = pygame.image.load("mario.png").convert()
    # Setting  our image to  the correct dimensions!
    self._player_image = pygame.transform.scale(self._player_image, (grid_size, grid_size))

    self._apple_image = pygame.image.load("spaghetti.jpeg").convert()
    self._apple_image = pygame.transform.scale(self._apple_image, (grid_size, grid_size))

    self._running =  True       # Keeps track of whether the app is running

    while( self._running ):
      pygame.event.pump()             # This lets Pygame know a frame has passed
      keys = pygame.key.get_pressed() # Returns a dictionary of booleans for which  keys are pressed

      if (keys[K_RIGHT]):
        self.player.move(1, 0)
      elif (keys[K_LEFT]):
        self.player.move(-1, 0)
      if (keys[K_DOWN]):
        self.player.move(0, 1)
      elif (keys[K_UP]):
        self.player.move(0, -1)
      
      # Lets us log where the player is at a given time
      if (keys[K_SPACE]):
        print(self.player)

      # Lets us exit our game
      if (keys[K_ESCAPE]):
        self._running = False

      # on_loop will be used later, on_render will render our graphics
      self.on_loop()
      self.on_render()

      time.sleep (0.5)

    # This will ONLY be called once  that while loop is exited. 
    self.on_cleanup()
 
  def on_loop(self):
    self.player.update()

    # does snake eat apple?
    # for i in range(0,self.player.length):
    if self.collision_check(self.apple.x, self.apple.y, self.player.x[0], self.player.y[0]):
      self.apple.x = randint(2,9) * grid_size
      self.apple.y = randint(2,9) * grid_size
      self.player.x.append(self.player.x[self.player.length - 1])
      self.player.y.append(self.player.y[self.player.length - 1])
      self.player.length = self.player.length + 1


    # does snake collide with itself?
    for i in range(2,self.player.length):
      if self.collision_check(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i]):
        print("You lose! Collision: ")
        print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
        print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
        exit(0)

    pass

  def collision_check(self,x1,y1,x2,y2):
    if x1 == x2 and y1 == y2:
      return True
    return False
 
  # Rendering out specific images
  def on_render(self):
    self._display.fill((0,0,0))
    
    # Drawing the player:
    for i in range(0,self.player.length):
      self._display.blit(self._player_image, (self.player.x[i], self.player.y[i])) 

    # Drawing the apple:
    self._display.blit(self._apple_image,(self.apple.x, self.apple.y)) 

    pygame.display.flip() # "Flips" the graphics to our new specifications
 
  def on_cleanup(self):
    pygame.quit()

# This is what starts the whole game:
if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()