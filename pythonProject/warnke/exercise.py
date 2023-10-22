import pygame

pygame.init()

# Inicjalizacja gamepada
pygame.joystick.init()

# Sprawdzenie dostępnych gamepadów
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Brak podłączonych gamepadów.")
    pygame.quit()
    exit()

# Wybór pierwszego gamepada
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

# Główna pętla programu
while True:
    # Odczytanie zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            # Odczytanie wartości osi analogowych
            axis_x = gamepad.get_axis(0)
            axis_y = gamepad.get_axis(1)
            axis_z = gamepad.get_axis(2)
            print("Oś X:", axis_x)
            print("Oś Y:", axis_y)
            print("Oś Z:", axis_z)

        elif event.type == pygame.JOYBUTTONDOWN:
            # Odczytanie wciśniętych przycisków
            button = event.button
            print("Przycisk", button, "wciśnięty.")

        elif event.type == pygame.JOYBUTTONUP:
            # Odczytanie zwolnionych przycisków
            button = event.button
            print("Przycisk", button, "zwolniony.")