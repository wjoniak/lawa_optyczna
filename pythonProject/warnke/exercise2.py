import time

import pygame,random
import numpy as np
from gauge import Gauge
from trening import wynik,intro,check_gamepad,start_game,progressbar
trend =[]
reflection =[]

game = 4 # 1-trening słuchowo-wzrokowy, 2 - tylko słuch, 3 - tylko wzrok

exercise_window = pygame.display.set_mode((1200, 675))

# Ustawienia
def task(chann,czas_trwania = 200, pauza = 20):
    if chann == 0:
        task = [880, 440, 440]  # Częstotliwości w Hz
        pygame.mixer.Channel(0).set_volume(1.0)
        pygame.mixer.Channel(1).set_volume(0.0)
    elif chann == 1:
        task = [440, 440, 880]
        pygame.mixer.Channel(0).set_volume(0.0)
        pygame.mixer.Channel(1).set_volume(1.0)
    else:
        task =[440,880,440]
        pygame.mixer.Channel(0).set_volume(0.1)
        pygame.mixer.Channel(1).set_volume(0.1)

    # Generowanie dźwięków
    for czestotliwosc in task:
        # Tworzenie tablicy z próbkami dźwięku
        sample_array = np.int16(32767.0 * np.sin(2 * np.pi * czestotliwosc * np.arange(0, czas_trwania/1000, 1/44100.0)))

        # Odtwarzanie dźwięku

        pygame.mixer.Sound(sample_array).play()

        # Pauza

        pygame.time.delay(czas_trwania + pauza)

def exercise():
    pygame.init()
    pygame.mixer.init(channels=2)

    check_gamepad(exercise_window)
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()



    #DisplayInfo('info/exercise1/')

    pygame.mixer.Sound("sounds/start-beeps.mp3").play()
    for i in range(4):
        screen = pygame.image.load('info/start.00' + str(i + 1) + '.jpeg')
        screen = pygame.transform.scale(screen, (1200, 675))
        exercise_window.blit(screen, (0, 0))
        pygame.display.update()
        time.sleep(1)



    screen = pygame.image.load('images/gamepad_screen.jpg')

    no = pygame.image.load('images/no.png')
    ok = pygame.image.load('images/ok.png')
    arrow_l = pygame.image.load("images/line-clipart-L.png")
    arrow_r = pygame.image.load("images/line-clipart-R.png")
    result_position = (exercise_window.get_width()/2.0 - 100, 30)


    counter_y = 0
    counter_n = 0
    setpoint = 0
    offset = 0.5
    cel = 0.2
    limit = 5
    korekta = 0.05

    exercise_window.blit(screen, (0, 0))
    pygame.display.update()
    time.sleep(3)

    #time.sleep(5)

    #main loop:

    while True:

        t = random.randint(0,1)

        task(t,int(offset*1000),int(offset*100))
        answer = -1

        start_time = pygame.time.get_ticks()
        while answer == -1:
            timer = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.JOYBUTTONDOWN:

                    elapsed_time = pygame.time.get_ticks() - start_time
                    reflection.append(round(elapsed_time/1000.0 ,2))
                    start_time = elapsed_time
                    answer = event.button - 9
                    print(t,answer,counter_y,counter_n)

                    exercise_window.blit(screen, (0, 0))


                    if answer == t:
                        if t == 0:
                            exercise_window.blit(arrow_l, (50, 200))

                        elif t == 1:
                            exercise_window.blit(arrow_r, (850, 200))
                        exercise_window.blit(ok, result_position)
                        progressbar(exercise_window, 350, 550, int(600*offset), int(600*cel))
                        pygame.display.update()
                        counter_y += 1
                        offset=offset - korekta
                    else:
                        if t == 0:
                            exercise_window.blit(arrow_l, (50, 200))

                        elif t == 1:
                            exercise_window.blit(arrow_r, (850, 200))
                        exercise_window.blit(no, result_position)
                        progressbar(exercise_window,350,550,int(600*offset),int(600*cel))
                        pygame.display.update()
                        offset = offset + korekta
                        counter_n += 1
                    pygame.display.update()
                    break




        trend.append(offset)
        if offset<cel:
            setpoint +=1
            offset = cel
        if setpoint > limit:
            break
        time.sleep(2)
        exercise_window.blit(screen, (0, 0))

        progressbar(exercise_window,350,550,int(600*offset),int(600*cel))
        pygame.display.update()

    return([reflection,trend,counter_n,counter_y])

wynik (exercise(),exercise_window)
pygame.quit()
