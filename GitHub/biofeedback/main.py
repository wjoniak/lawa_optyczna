import serial,pygame,numpy as np

import gui,time,random
from gui import pointer,label,wynik,start_game

sound_path = "sounds/select.mp3"
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


port = serial.Serial('/dev/cu.usbmodem12301', 115200, bytesize=8, parity='N', stopbits=1,timeout=1)

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
while joystick_count == 0:
    screen = pygame.image.load('../../GitHub/biofeedback/info/error.001.jpeg')
    screen = pygame.transform.scale(screen, (1200, 675))
    screen.blit(screen, (0, 0))
    pygame.display.update()
    pygame.joystick.init()
    time.sleep(5)
    exit()

gamepad = pygame.joystick.Joystick(0)
gamepad.init()


zegar = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
czas_start = pygame.time.get_ticks()
czas_minuty = 1
czas_sekundy = 0
status = "running"

width, height = 1200, 675
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PTTP - gabinet biofeedback")

heart = pygame.image.load("images/heart.png")

tick_time = 0
bpm,gsr,hrv = 0,0,0
ibi = []
hrv_data = []
gsr_data = []
rtime_data = []
trend = []
reflection = []
counter_y = 0
counter_n = 0
setpoint = 0
offset = 0.5
task = 50
answer = 0
game = 2 # 1-trening słuchowo-wzrokowy, 2 - tylko słuch, 3 - tylko wzrok



if game == 1 or game == 3:
    lamp1_L = pygame.image.load('images/bulb1.png')
    lamp2_L = pygame.image.load('images/bulb2.png')
    lamp1_R = pygame.image.load('images/bulb1.png')
    lamp2_R = pygame.image.load('images/bulb2.png')
    pozycja_obrazka1 = (100, 40)
    pozycja_obrazka2 = (800, 40)
elif game == 2:
    lamp1_L = pygame.image.load('images/speaker_left.png')
    lamp2_L = pygame.image.load('images/speaker_left.png')
    lamp1_R = pygame.image.load('images/speaker_right.png')
    lamp2_R = pygame.image.load('images/speaker_right.png')
    pozycja_obrazka1 = (100, 40)
    pozycja_obrazka2 = (700, 40)

no = pygame.image.load('images/no.png')
ok = pygame.image.load('images/ok.png')

result_position = (screen.get_width()/2.0 - 100, 100)

bg = pygame.image.load("images/background.png")




while status == "running":
    screen.blit(bg, (0, 0))
    screen.blit(lamp1_L, pozycja_obrazka1)
    screen.blit(lamp1_R, pozycja_obrazka2)

    if answer >= 0 :
        task = random.randint(0, 100)
        if task % 2 == 0  :
            if game < 3:
                sound("L")
            screen.blit(screen, (0, 0))
            screen.blit(lamp2_L, pozycja_obrazka1)
            screen.blit(lamp1_R, pozycja_obrazka2)
            #my_gauge.draw(percent=int(offset * 100))
            pygame.display.update()
            time.sleep(offset)
            screen.blit(screen, (0, 0))
            screen.blit(lamp1_L, pozycja_obrazka1)
            screen.blit(lamp1_R, pozycja_obrazka2)
            #my_gauge.draw(percent=int(offset * 100))
            if game < 3:
                sound("P")

            pygame.display.update()
        else:
            if game < 3:
                sound("P")
            screen.blit(screen, (0, 0))
            screen.blit(lamp1_L, pozycja_obrazka1)
            screen.blit(lamp2_R, pozycja_obrazka2)
            #my_gauge.draw(percent=int(offset * 100))
            pygame.display.update()
            time.sleep(offset)
            screen.blit(screen, (0, 0))
            screen.blit(lamp1_L, pozycja_obrazka1)
            screen.blit(lamp1_R, pozycja_obrazka2)
            #gauge
            if game < 3:
                sound("L")
            pygame.display.update()



    answer = -1
    tick = False
    start_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.JOYBUTTONDOWN:

            elapsed_time = pygame.time.get_ticks() - start_time
            reflection.append(round(elapsed_time / 1000.0, 2))
            start_time = elapsed_time
            answer = event.button - 9
            if answer == task % 2:
                screen.blit(ok, result_position)
                pygame.display.update()
                counter_y += 1
                offset = offset - 0.02
            else:
                screen.blit(no, result_position)
                pygame.display.update()
                offset = offset + 0.02
                counter_n += 1
        elif event.type == pygame.USEREVENT:
            czas_sekundy -= 1
            if czas_sekundy == -1:
                czas_sekundy = 59
                czas_minuty -= 1
            if czas_minuty == 0 and czas_sekundy == 0:
                status = "completed"
                print(status)
                break

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


    trend.append(round(offset, 2))
    if offset < 0.01:
        setpoint += 1
        offset = 0.01
    if setpoint > 10:
        break






if port.is_open:
    port.close()
if status == "completed":
    gui.wynik(screen,[reflection,offset,hrv_data,gsr_data,counter_y,counter_n])
