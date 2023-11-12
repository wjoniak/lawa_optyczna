import random,os
import numpy as np
import time,pygame
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import matplotlib.backends.backend_agg as agg


import pylab


def wynik(wyniki,exercise_window):
    screen = pygame.image.load('info/exercise1/exercise1.006.jpeg')
    screen = pygame.transform.scale(screen, (1200, 675))
    exercise_window.blit(screen, (0, 0))

    # Utworzenie obiektu Surface z tekstem
    font = pygame.font.Font('fonts/Raleway-Bold.ttf', 36)  # Wybierz czcionkę i rozmiar
    text = font.render("średni czas reakcji: "+str(round(sum(wyniki[0]) / len(wyniki[0] ),2))+' s', True, (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (exercise_window.get_width() // 2, 50)  # Ustaw pozycję napisu
    exercise_window.blit(text, text_rect)
    text = font.render("poprawne odpowiedzi: " + str(wyniki[3]), True, (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (exercise_window.get_width() // 2, 100)  # Ustaw pozycję napisu
    exercise_window.blit(text, text_rect)
    text = font.render("błędy: " + str(wyniki[2]), True, (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (exercise_window.get_width() // 2, 150)  # Ustaw pozycję napisu
    exercise_window.blit(text, text_rect)
    plt.style.use('ggplot')

    fig = pylab.figure(figsize=[10, 4],  # Inches
                       dpi=100,  # 100 dots per inch, so the resulting buffer is 400x400 pixels
                       )
    fig.figure.set_alpha(0)
    ax = fig.gca()


    ax.plot(wyniki[0],label='czas reakcji')
    ax.plot(wyniki[1], label='opóźnienie')
    ax.legend()


    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    wykres = pygame.display.get_surface()
    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    wykres.blit(surf, (100, 200))

    pygame.display.flip()

    time.sleep(30)
    return

def  intro(path):
    answer = -1
    for i in range(4):
        if answer == 2:
            break
        answer =-1
        image_path = 'info/exercise1/'+'exercise1.00' + str(i + 1) + '.jpeg'
        screen = pygame.image.load(image_path)
        screen = pygame.transform.scale(screen,(1200,675))
        exercise_window.blit(screen, (0,0))
        pygame.display.update()
        while answer == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.JOYBUTTONDOWN:
                    answer = event.button




def check_gamepad(exercise_window):
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


def  start_game(exercise_window):
    pygame.mixer.Sound("sounds/start-beeps.mp3").play()
    for i in range(4):

        screen = pygame.image.load('info/start.00'+str(i+1)+'.jpeg')
        screen = pygame.transform.scale(screen, (1200, 675))
        exercise_window.blit(screen, (0, 0))
        pygame.display.update()
        time.sleep(1)



def progressbar(window,x,y,width,marker):
    height=50
    width = (width * 500.0) /500.0
    rect_surface_out = pygame.Surface((500, 50))
    rect_surface = pygame.Surface((int(width*5.0), height))

    for i in range(height):
        red = int(255 - (i / height) * 255)
        yellow = int((i / height) * 255)
        pygame.draw.line(rect_surface_out, (red, yellow, 0), (4, i-4), (width+4, i-4))
        triangle_points = [
            (marker, 50),
            (marker + 20, 50),
            (marker + 20 / 2, 30)
        ]
        pygame.draw.polygon(rect_surface_out, (255, 0, 0), triangle_points)
    pygame.draw.rect(rect_surface_out, (20,20,20), pygame.Rect(0, 0, 600, 50),  2)
    window.blit(rect_surface_out, (x, y))
    pygame.display.update(x,y-20,600,90)
