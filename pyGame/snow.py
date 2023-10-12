 #Import a library of functions called 'pygame'
import pygame
import random
# Initialize the game engine
pygame.init()
#House

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Let It Snow")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Classes
class Snow(pygame.sprite.Sprite):

    # Constructor function
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(WHITE)
        self.speed = random.randrange(1,3)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(0,400)
    # end of constructor function
    def update(self):
        if self.rect.y> 500:
            self.rect.y = -50
            self.speed = random.randrange(1,3)
        else:
            self.rect.y = self.rect.y + self.speed
        # end if
  # end Class Snow  

# Global variables
snow_group = pygame.sprite.Group()
number_of_flakes = 200
for i in range (0,number_of_flakes):
    flake = Snow(5,5)
    snow_group.add(flake)
#Next i
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    snow_group.update()

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLUE)
    # Draw stuff here
    snow_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# end while

pygame.quit()