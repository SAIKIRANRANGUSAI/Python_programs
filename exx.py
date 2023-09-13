class lamp:

    def __init__(self, model: str, colour :str):
        self.model = model
        self.colour = colour

    def turn_on(self):
        print(f'{self.model} is turned on')

    def turn_of(self):
        print(f'{self.model} is turned off')


    def dec(self):
        print(f'{self.model} ({self.colour})')

red : lamp = lamp('hmmm', 'blue')
red.turn_on()

