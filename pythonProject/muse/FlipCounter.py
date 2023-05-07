import pygame

class FlipingCounter:
    def __init__(self, x, y, digit_width, digit_height, max_value, current_value):
        self.x = x
        self.y = y
        self.digit_width = digit_width
        self.digit_height = digit_height
        self.max_value = max_value
        self.current_value = current_value

        self.digits = []
        for i in range(10):
            digit_path = f"digit_{i}.png"  # ścieżka do pliku PNG cyfry i
            digit_image = pygame.image.load(digit_path).convert_alpha()
            digit_image = pygame.transform.scale(digit_image, (self.digit_width, self.digit_height))
            self.digits.append(digit_image)

        self.previous_value = current_value
        self.previous_digits = []
        for i in range(len(str(self.max_value))):
            self.previous_digits.append(0)

        self.flipping = False
        self.flipping_frame_count = 0
        self.flipping_frame_max = 10

    def set_value(self, value):
        self.previous_value = self.current_value
        self.previous_digits = self.get_digits(self.previous_value)
        self.current_value = value
        self.flipping = True
        self.flipping_frame_count = 0

    def get_digits(self, value):
        digits = []
        value_str = str(value).zfill(len(str(self.max_value)))
        for i in range(len(value_str)):
            digits.append(int(value_str[i]))
        return digits

    def draw(self, screen):
        current_digits = self.get_digits(self.current_value)
        previous_digits = self.previous_digits

        if self.flipping:
            flip_index = len(current_digits) - self.flipping_frame_count - 1
            previous_digit = previous_digits[flip_index]
            current_digit = current_digits[flip_index]

            # Wyświetl poprzednią cyfrę zamiast obecnej cyfry
            for i in range(flip_index):
                digit_image = self.digits[previous_digits[i]]
                screen.blit(digit_image, (self.x + i * self.digit_width, self.y))

            # Wyświetl częściowo przeflipowaną cyfrę
            progress = (self.flipping_frame_count + 1) / self.flipping_frame_max
            flip_image = pygame.transform.flip(self.digits[previous_digit], True, False)
            flip_height = int(self.digit_height * progress)
            flip_y = self.y + flip_index * self.digit_height + (self.digit_height - flip_height)
            screen.blit(flip_image, (self.x + flip_index * self.digit_width, flip_y), (0, 0, self.digit_width, flip_height))

            # Wyświetl obecnie wyświetlaną cyfrę
            for i in range(flip_index + 1, len(current_digits)):
                digit_image = self.digits[current_digits[i]]
                screen.blit(digit_image, (self.x + i * self.digit_width, self.y))

            self.flipping_frame_count += 1
            if self.flipping_frame_count == self.flipping_frame_max:
                self.flipping = False

        else:
            for i in range(len(current_digits)):
                digit_image = self.digits[current_digits[i]]
                screen.blit(digit_image, (self.x + i * self.digit_width, self.y))


pygame.init()

# Ustaw rozmiar okna
screen_width = 600
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

# Ustaw tło
background_color = (255, 255, 255)
screen.fill(background_color)

# Utwórz licznik
x = 100
y = 100
digit_width = 50
digit_height = 100
max_value = 999
current_value = 0
counter = FlipingCounter(x, y, digit_width, digit_height, max_value, current_value)

# Pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_value += 1
                if current_value > max_value:
                    current_value = 0
                counter.set_value(current_value)

    # Wyświetl tło i licznik
    screen.fill(background_color)
    counter.draw(screen)

    # Wyświetl wszystko na ekranie
    pygame.display.flip()

pygame.quit()
