import pygame
import sys
import numpy as np

pygame.init()

# Ustawienia dźwięku
sample_rate = 44100
duration = 1.0
frequency1 = 440.0

# Generowanie dźwięku
num_samples = int(sample_rate * duration)
time = np.linspace(0, duration, num_samples, endpoint=False)
sound_data = np.sin(2 * np.pi * frequency1 * time)
sound_data = np.array(np.clip(sound_data * 32767, -32767, 32767), dtype=np.int16)

channel = pygame.mixer.Channel(0)
sound = pygame.mixer.Sound(sound_data)

def lewy():
    channel.play(sound)
    channel.set_volume(1.0, 0.0)
    pygame.time.wait(int(duration * 1000))

def prawy():
    channel.play(sound)
    channel.set_volume(0.0, 1.0)
    pygame.time.wait(int(duration * 1000))

def main():
    for i in range (10):

        if np.random.randint(10) > 4:
            lewy()
            prawy()
            pygame.time.wait(int(duration * 1000))
        else:
            prawy()
            lewy()
            pygame.time.wait(int(duration * 1000))

main()