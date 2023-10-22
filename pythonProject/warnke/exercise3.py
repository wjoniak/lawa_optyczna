import random,os
import numpy as np
import time,pygame

from pygame.locals import *
from gauge import Gauge



trend =[]
reflection =[]
sound_path ="sounds/select.mp3"
game = 1 # 1-trening słuchowo-wzrokowy, 2 - tylko słuch, 3 - tylko wzrok

exercise_window = pygame.display.set_mode((1200, 675))

def  DisplayInfo(path):
    answer = -1
    for i in range(4):
        if answer == 2:
            break
        answer =-1
        image_path = 'info/exercise1/'+'exercise1.00' + str(i + 1) + '.jpeg'
        print(image_path)
        screen = pygame.image.load(image_path)
        screen = pygame.transform.scale(screen,(1200,675))
        exercise_window.blit(screen, (0,0))
        pygame.display.update()
        while answer == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.JOYBUTTONDOWN:
                    answer = event.button


    pygame.mixer.Sound("sounds/start-beeps.mp3").play()
    for i in range(4):

        screen = pygame.image.load('info/start.00'+str(i+1)+'.jpeg')
        screen = pygame.transform.scale(screen, (1200, 675))
        exercise_window.blit(screen, (0, 0))
        pygame.display.update()
        time.sleep(1)

    screen = pygame.image.load('info/exercise1/exercise1.006.jpeg')
    screen = pygame.transform.scale(screen, (1200, 675))
    exercise_window.blit(screen, (0, 0))
    pygame.display.update()
def sound(channel,path=sound_path):
    sound = pygame.mixer.Sound(sound_path)
    if channel =="L" :
        sound_array = pygame.sndarray.array(sound)
        sound_array[:, 1] = 0  # Ustawienie głośności dla prawego kanału na 0
        sound = pygame.sndarray.make_sound(sound_array)
        print ("left")

    if channel == "P":
        sound_array = pygame.sndarray.array(sound)
        sound_array[:, 0] = 0  # Ustawienie głośności dla lewego kanału na 0
        sound = pygame.sndarray.make_sound(sound_array)
        print("right")

    sound.play()
    return channel
def exercise():
    pygame.init()
    pygame.mixer.init(channels=2)

    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    while joystick_count == 0:

        screen = pygame.image.load('info/error.001.jpeg')
        screen = pygame.transform.scale(screen, (1200, 675))
        exercise_window.blit(screen, (0, 0))
        pygame.display.update()
        pygame.joystick.init()
        time.sleep(5)
        exit()

    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()



    DisplayInfo('info/exercise1/')



    FONT = pygame.font.SysFont('Franklin Gothic Heavy', 60)


    my_gauge = Gauge(
            screen=exercise_window,
            FONT=FONT,
            x_cord=exercise_window.get_width() / 2,
            y_cord=exercise_window.get_height() / 2 + 100,
            thickness=20,
            radius=100,
            circle_colour=(240,20,20),
            glow=False)

    percentage = 0

    screen = pygame.image.load('info/exercise1/exercise1.006.jpeg')
    screen = pygame.transform.scale(screen,(1200,675))
    if game == 1 or game == 3:
        lamp1_L = pygame.image.load('images/bulb1.png')
        lamp2_L = pygame.image.load('images/bulb2.png')
        lamp1_R = pygame.image.load('images/bulb1.png')
        lamp2_R = pygame.image.load('images/bulb2.png')
    elif game == 2:
        lamp1_L = pygame.image.load('images/speaker_left.png')
        lamp2_L = pygame.image.load('images/speaker_left.png')
        lamp1_R = pygame.image.load('images/speaker_right.png')
        lamp2_R = pygame.image.load('images/speaker_right.png')

    no = pygame.image.load('images/no.png')
    ok = pygame.image.load('images/ok.png')
    pozycja_obrazka1 = (100, 50)
    pozycja_obrazka2 = (800, 50)
    result_position = (exercise_window.get_width()/2.0 - 100, 100)



    # Zmienne stopera
    start_time = 0
    #elapsed_time = 0

    counter_y = 0
    counter_n = 0
    setpoint = 0
    offset = 0.5

    exercise_window.blit(lamp1_L, pozycja_obrazka1)
    exercise_window.blit(lamp1_R, pozycja_obrazka2)
    my_gauge.draw(percent=offset*100)
    pygame.display.update()
    time.sleep(3)

    #time.sleep(5)

    #main loop:

    while True:



        task = random.randint(0,100)
        answer = -1


        if task % 2 == 0 :
            if game < 3:
                sound("L")
            exercise_window.blit(screen, (0,0))
            exercise_window.blit(lamp2_L, pozycja_obrazka1)
            exercise_window.blit(lamp1_R, pozycja_obrazka2)
            my_gauge.draw(percent=int(offset * 100))
            pygame.display.update()
            time.sleep(offset)
            exercise_window.blit(screen, (0, 0))
            exercise_window.blit(lamp1_L, pozycja_obrazka1)
            exercise_window.blit(lamp1_R, pozycja_obrazka2)
            my_gauge.draw(percent=int(offset * 100))
            if game < 3:
                sound("P")

            pygame.display.update()
        else:
            if game < 3:
                sound("P")
            exercise_window.blit(screen, (0, 0))
            exercise_window.blit(lamp1_L, pozycja_obrazka1)
            exercise_window.blit(lamp2_R, pozycja_obrazka2)
            my_gauge.draw(percent=int(offset * 100))
            pygame.display.update()
            time.sleep(offset)
            exercise_window.blit(screen, (0, 0))
            exercise_window.blit(lamp1_L, pozycja_obrazka1)
            exercise_window.blit(lamp1_R, pozycja_obrazka2)
            my_gauge.draw(percent=int(offset * 100))
            if game < 3:
                sound("L")
            pygame.display.update()

        start_time = pygame.time.get_ticks()
        while answer == -1:
            timer = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.JOYBUTTONDOWN:

                    elapsed_time = pygame.time.get_ticks() - start_time
                    reflection.append(elapsed_time)
                    start_time = elapsed_time
                    answer = event.button - 9
                    if answer == task % 2:
                        exercise_window.blit(ok, result_position)
                        pygame.display.update()
                        counter_y += 1
                        offset=offset -0.05
                    else:
                        exercise_window.blit(no, result_position)
                        pygame.display.update()
                        offset = offset + 0.01
                        counter_n += 1
                    break

        trend.append(offset)
        if offset<0.01:
            setpoint +=1
            offset = 0.01
        if setpoint > 2:
            exit()
        time.sleep(3)
return([reflection,trend,counter_y,counter_n])