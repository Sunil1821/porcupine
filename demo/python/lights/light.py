from porcupine.demo.python.lights.lightbaseclass import LightBase


class Light(LightBase):
    def __init__(self):
        pass

    def light_on(self):
        print("Lights ON")

    def light_off(self):
        print("Lights OFF")


if __name__ == "__main__":
    light1 = Light()
    light1.light_on()
    light1.light_off()