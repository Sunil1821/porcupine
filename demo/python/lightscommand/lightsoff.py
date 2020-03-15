from porcupine.demo.python.lights import Light
from porcupine.demo.python.lightscommand.lightbase import LightBase


class LightsOff(LightBase):
    def __init__(self):
        self._light = Light()

    def invoke(self):
        self._light.light_off()


if __name__ == "__main__":
    lights_off_obj = LightsOff()
    lights_off_obj.invoke()
