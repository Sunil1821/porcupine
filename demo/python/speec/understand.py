from porcupine.demo.python.speec.understandbase import UnderstandBase
from porcupine.demo.python.lightscommand import LightsOn, LightsOff
import re
import string
import random
import faker
import time
import speech_recognition as sr


def get_random_string():
   wordlist = ["lights", "light", "Light", "LiGht", "on", "off", "lll;llightsflmef",
               "llonnnn", "ok", "hello", "olllll", "hwy", "why"]

   faker_ = faker.Faker()
   return faker_.sentence(ext_word_list=wordlist)


class Understand(UnderstandBase):
    def __init__(self, lights_on_cmd, lights_off_cmd):
        self._lights_on_cmd = lights_on_cmd
        self._lights_off_cmd = lights_off_cmd
        self._parsed_output = None

    def listen(self):
        r = sr.Recognizer()

        with sr.Microphone(device_index=0) as source:
            r.adjust_for_ambient_noise(source=source)
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
            self._parsed_output = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

    def check(self):
        if re.search("light", self._parsed_output.lower()):
            if re.search("on", self._parsed_output.lower()):
                self._lights_on_cmd.invoke()
            elif re.search("off", self._parsed_output.lower()):
                self._lights_off_cmd.invoke()
            else:
                print("Unable to understand the command")
        else:
            print("Unable to understand the command")


if __name__ == "__main__":
    lo = LightsOff()
    ln = LightsOn()
    ud = Understand(ln, lo)
    for i in range(100):
        ud.listen()
        ud.check()
