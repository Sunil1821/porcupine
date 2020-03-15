
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()


with sr.Microphone(device_index=0) as source:
    r.adjust_for_ambient_noise(source=source)
    print("Say something!")
    audio = r.listen(source, timeout=3, phrase_time_limit=3)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))