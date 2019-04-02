# 🐍 Python Tutorial

## 🧐 Setup!

Python is a really popular language, and it's named after Monty Python, so you know it's gotta be good. First, let's make sure you have it on your dang computer. 

In your terminal, type `python --version` and hit enter. 

If you get an error, you don't have python at all. If not, it will list your Python version. If your version is under 3.6, try entering `python3 --version`. If you have at least version 3.6, you're all set! If not, you'll need to install Python.

### Installing Python3 - Windows 

Go to [this link](https://www.python.org/downloads/) and download 3.7.3. 😎

### Installing Python3 - Mac

Macs come with Python on them, but you might not have the newest version. You can install it with Homebrew. If you don't already have Homebrew, you can install it with this ruby command:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

And then install the newest Python like so:

```
brew install python3
```

### Testing Our File

Let's start with a basic Python script. Create a new directory, cd into it, create and open new file, and name it `main.py`. In that file, write this:

```
print("Hello world!")
```

To run that file, run `python3 main.py` in your command line. 

## 🕹 The game!

Our starting, base file:

```
from pygame.locals import *
import pygame

grid_size = 44

class Player:
  
  #
  # Attributes will go here!
  #


  #
  # Override Print function
  #

  
  #
  # Movement function
  #


# Setting up the class for our game:
class App:
  
  #
  # Attributes here
  #


  # 
  # Init function
  #


  #
  # on_execute()
  #
 
  # Just leave this here:
  def on_loop(self):
    pass
 

  # 
  # on_loop()
  #
 
  #
  # on_cleanup
  #

# This is what starts the whole game:
if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()
```

Note that this file won't work yet! We need to add a bunch.

Look through the rest of this repo to see various stages of the project. The various `iterationX.py` files have finished projects at each of our checkpoints, while `iterationX_base.py` files have a starting file for each of those iterations, including comments indicating what you'll need to add. 
