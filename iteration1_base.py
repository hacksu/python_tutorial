from pygame.locals import *
import pygame

grid_size = 44

class Player:
  # Initialize attributes x, y, and speed

  # def __str__(self):

  # def move(self, x, y):   
  pass              


class App:
  # Initializing variables windowWidth, windowHeight, and  player

  # def __init__(self):

  # def on_execute(self):
    # Initialize the game

    # Setting up our display. We'll use this to render our game:
    self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

    # This "titles" our game
    pygame.display.set_caption('Hacksu Snake! 🐍')

    # Setting up our 
    self._player_image = pygame.image.load("mario.png").convert()
    # Setting  our image to  the correct dimensions!
    self._player_image = pygame.transform.scale(self._player_image, (grid_size, grid_size))

    self._running =  True       # Keeps track of whether the app is running

    while( self._running ):
      pygame.event.pump()             # This lets Pygame know a frame has passed
      keys = pygame.key.get_pressed() # Returns a dictionary of booleans for which  keys are pressed

      # Gives us -1 or 1 calculated by which key we're pressing
      x_movement = keys[K_RIGHT] - keys[K_LEFT]
      y_movement = keys[K_DOWN] - keys[K_UP]
      self.player.move(x_movement, y_movement)
      
      # Lets us log where the player is at a given time
      if (keys[K_SPACE]):
        print(self.player)

      # Lets us exit our game
      if (keys[K_ESCAPE]):
        self._running = False

      # on_loop will be used later, on_render will render our graphics
      self.on_loop()
      self.on_render()

    # This will ONLY be called once  that while loop is exited. 
    self.on_cleanup()
 
  def on_loop(self):
    pass
 
  # Rendering out specific images
  def on_render(self):
    self._display.fill((0,0,0))
    self._display.blit(self._player_image,(self.player.x,self.player.y))
    pygame.display.flip() # "Flips" the graphics to our new specifications
 
  def on_cleanup(self):
    pygame.quit()

# This is what starts the whole game:
if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()