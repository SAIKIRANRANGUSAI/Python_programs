class Lamp:

    def __init__(self, model:str, color:str):
        self.model = model
        self.color = color

    def turn_on(self):
        print(self.model,'is turned on:')

    def turn_of(self):
        print(self.model,'turned off:')

    def describe(self):
        print(f'{self.model}({self.color})')

red_lamp:Lamp = Lamp('rehgd','red')
red_lamp.turn_on()

