import pyttsx3

def textToSpeech(text):
    engine = pyttsx3.init()

    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate + 1) # Скорость
    volume = engine.getProperty("volume")
    engine.setProperty("volume", volume + 0.1) # Громкость

    engine.say(text)
    engine.runAndWait()

textToSpeech(input("Введите текст для озвучки: "))  # Запуск