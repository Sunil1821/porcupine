from porcupine.demo.python.lights import Light
from porcupine.demo.python.lightscommand.lightbase import LightBase


class LightsOn(LightBase):
    def __init__(self):
        self._light = Light()

    def invoke(self):
        self._light.light_on()


if __name__ == "__main__":
    lights_off_obj = LightsOn()
    lights_off_obj.invoke()