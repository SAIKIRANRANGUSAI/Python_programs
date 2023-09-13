class Lamp:
    def __init__(self, model: str, colour: str):
        self.model = model
        self.colour = colour

    def turn_on(self):
        print(self.model, 'is turned on')

    def turn_of(self):
        print(self.colour, 'turned of')

    def describe(self):
        print(f'lamp:{self.model} ({self.colour})')


red_lamp: Lamp = Lamp('rrd', 'Red')
red_lamp.turn_on()
