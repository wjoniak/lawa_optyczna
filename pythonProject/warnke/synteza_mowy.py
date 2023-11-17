from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    # Utwórz obiekt gTTS
    tts = gTTS(text=text, lang=language, slow=False)

    # Zapisz plik dźwiękowy
    tts.save("output.mp3")

    # Odtwórz plik dźwiękowy
    os.system("start output.mp3")

if __name__ == "__main__":
    # Pobierz tekst od użytkownika
    input_text = input("Podaj tekst do przekształcenia na mowę: ")

    # Przekształć tekst na mowę i odtwórz
    text_to_speech(input_text)
