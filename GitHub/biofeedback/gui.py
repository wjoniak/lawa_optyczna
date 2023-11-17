import numpy as np
import time,pygame
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import matplotlib.backends.backend_agg as agg


import pylab

def gauge_linear( screen, x ,y ,name ,alt_value ,value):
    step = 1
    if alt_value < value:
        step = 1
    if alt_value >value:
        step = -1
    font = pygame.font.Font(None, 36)
    bg_image = pygame.image.load("images/gauge_bg_240.png")
    for angle in range(alt_value, value, step):
        pointer_image = pygame.image.load("images/pointer_120.png")
        pointer_image = pygame.transform.rotate(pointer_image, int(135 - angle * 2.7))
        rect = pygame.Rect(x, y, 240, 240)
        bg_rect = bg_image.get_rect(center=(x, y))
        pointer_rect = pointer_image.get_rect(center=bg_rect.center)
        text_surface_1 = font.render(name, True, (160, 160, 160))
        text_surface_2 = font.render(str(value), True, (255, 255, 255))
        text_rect_1 = text_surface_1.get_rect(center=(x, y - 40))
        text_rect_2 = text_surface_2.get_rect(center=(x, y + 80))
        screen.blit(bg_image, bg_rect)
        screen.blit(text_surface_1, text_rect_1)
        screen.blit(pointer_image, pointer_rect)
        screen.blit(text_surface_2, text_rect_2)
        pygame.display.update(rect)
        pygame.time.delay(10)


def pointer(screen,x,y,name, value):
    font = pygame.font.Font(None, 24)
    pointer_image = pygame.image.load("images/pointer_120.png")
    pointer_image = pygame.transform.rotate(pointer_image, int(135 - value * 2.7))
    rect = pygame.Rect(x, y, 240, 240)

    pointer_rect = pointer_image.get_rect(center=(x, y))
    text_surface_1 = font.render(name, True, (160, 160, 160))
    text_surface_2 = font.render(str(value), True, (255, 255, 255))
    text_rect_1 = text_surface_1.get_rect(center=(x, y - 30))
    text_rect_2 = text_surface_2.get_rect(center=(x, y + 50))
    screen.blit(text_surface_1, text_rect_1)
    screen.blit(pointer_image, pointer_rect)
    screen.blit(text_surface_2, text_rect_2)

def label(screen,x,y,value):
    font = pygame.font.Font(None, 32)
    text_surface = font.render(str(value), True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def timer():
    pass

def wynik(exercise_window,wyniki):
    screen = pygame.image.load('info/exercise1/exercise1.006.jpeg')
    screen = pygame.transform.scale(screen, (1200, 675))
    exercise_window.blit(screen, (0, 0))

    # Utworzenie obiektu Surface z tekstem
    font = pygame.font.Font('fonts/Raleway-Bold.ttf', 36)  # Wybierz czcionkę i rozmiar
    text = font.render("średni czas reakcji: "+str(round(sum(wyniki[0]) / len(wyniki[0] ),2))+' s', True, (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (exercise_window.get_width() // 2, 50)  # Ustaw pozycję napisu
    exercise_window.blit(text, text_rect)
    text = font.render("poprawne odpowiedzi: " + str(wyniki[4]), True, (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (exercise_window.get_width() // 2, 100)  # Ustaw pozycję napisu
    exercise_window.blit(text, text_rect)
    text = font.render("błędy: " + str(wyniki[5]), True, (0, 0, 255))
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
    ax.plot(wyniki[2], label='HRV')
    ax.plot(wyniki[3], label='GSR')
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

    time.sleep(10)
    return

def  start_game(exercise_window):
    pygame.mixer.Sound("sounds/start-beeps.mp3").play()
    for i in range(4):

        screen = pygame.image.load('info/start.00'+str(i+1)+'.jpeg')
        screen = pygame.transform.scale(screen, (1200, 675))
        exercise_window.blit(screen, (0, 0))
        pygame.display.update()
        time.sleep(1)

def check_gamepad(exercise_window):
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    while joystick_count == 0:
        screen = pygame.image.load('../../GitHub/biofeedback/info/error.001.jpeg')
        screen = pygame.transform.scale(screen, (1200, 675))
        exercise_window.blit(screen, (0, 0))
        pygame.display.update()


def update_bfb_data(screen):
    port = serial.Serial('/dev/cu.usbmodem12301', 115200, bytesize=8, parity='N', stopbits=1, timeout=1)
    dane = port.readline().decode('utf-8').strip()

    dane = dane.split(':')
    if dane[0] == "GSR":
        gsr = int(dane[1]) / 7
        gsr = round(gsr)
        gsr_data.append(gsr)
    if dane[0] == "CLK":
        tick = True

    if dane[0] == "BPM":
        bpm = int(dane[1])
        # print(':',BPM)
    if dane[0] == "IBI":
        ibi.append(int(dane[1]))
        if len(ibi) > 20:
            ibi.pop(0)
            ibi_s = np.array(ibi)
            hrv = np.std(np.diff(ibi_s))
            hrv = round(hrv)
            hrv_data.append(hrv)

    if tick:
        screen.blit(heart, (288, 548))
    pygame.time.delay(100)
    gui.pointer(screen, 100, 580, 'HRV', hrv)
    gui.pointer(screen, 1100, 580, 'GSR', gsr)
    gui.label(screen, 240, 580, "BPM:" + str(bpm))
    czas_str = f"{czas_minuty:02}:{czas_sekundy:02}"
    gui.label(screen, 880, 580, czas_str)
    pygame.display.flip()

def h_bar(screen,x,y,szer,wys, value,name):
    pass