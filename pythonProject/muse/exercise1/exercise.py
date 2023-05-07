import pygame,random,time

# Inicjuj Pygame
pygame.init()

# Ustaw rozmiar ekranu
screen_width = 2000
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load("forest.jpg")
licznik = 0
timer = 0
import pygame
class Counter:
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

    def set_value(self, value):
        self.current_value = value

    def draw(self, screen):
        # wyświetlenie cyfr jako obrazów PNG
        value_str = str(self.current_value)
        value_len = len(value_str)
        x_offset = self.x
        for i in range(value_len):
            digit = int(value_str[i])
            digit_image = self.digits[digit]
            screen.blit(digit_image, (x_offset, self.y))
            x_offset += self.digit_width

class VerticalProgressBar:
    def __init__(self, x, y, width, height, bg_color, bar_color, min_value, max_value, current_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.bar_color = bar_color
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value

    def set_value(self, value):
        self.current_value = value

    def draw(self, screen):
        progress = (self.current_value - self.min_value) / (self.max_value - self.min_value)
        bar_height = int(progress * self.height)
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.bar_color, (self.x, self.y + self.height - bar_height, self.width, bar_height))

# Klasa sprite'a
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        nr = random.randint(1, 5)
        x = random.randint(0, 2000)
        y = random.randint(0, 900)
        scale  = random.random()/10 + 0.1
        flip = random.randint(1, 10)
        self.image = pygame.image.load("bird"+str(nr)+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        if flip > 5:
            self.image = pygame.transform.flip(self.image, True, False)
        sound = pygame.mixer.Sound("bird"+str(nr)+".wav")
        sound.play()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Aktualizuj stan sprite'a
        pass


progress_bar = VerticalProgressBar(50, 50, 20, 300, (200, 200, 200), (0, 255, 0), 0, 300, 300)
all_sprites = pygame.sprite.Group()


bird = MySprite()
all_sprites.add(bird)
# Pętla gry
running = True
while running:
    progress_bar.set_value(300-timer)
    timer = timer+1

    time.sleep(0.01)
    if timer > 300:
        bird = MySprite()
        all_sprites.add(bird)
        timer = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bird.rect.collidepoint(event.pos):
                all_sprites.remove(bird)
                licznik=licznik+1
                print ("trafienia:",licznik)

        # Odśwież ekran

    screen.blit(background_image, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    progress_bar.draw(screen)
    pygame.display.flip()

# Wyjdź z Pygame
pygame.quit()
