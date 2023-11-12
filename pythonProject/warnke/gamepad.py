import pygame,time

pygame.init()
pygame.joystick.init()

clock = pygame.time.Clock()
FPS = 60

#create empty list to store joysticks
joysticks = []


def gamepadEvent(joysticks):
    for joystick in joysticks:

        if abs(joystick.get_axis(4)) > 0.8:
            time.sleep(0.1)
            return ('L')


        if abs(joystick.get_axis(5)) > 0.8:
            time.sleep(0.1)
            return ('R')


run = True
while run:

  clock.tick(FPS)




  #event handler
  for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
      joy = pygame.joystick.Joystick(event.device_index)
      joysticks.append(joy)
    #quit program
    if event.type == pygame.QUIT:
      run = False
    print (gamepadEvent(joysticks))

pygame.quit()


