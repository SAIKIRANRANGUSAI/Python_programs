#In Python, a data class is a class that is designed to only hold data values.

from dataclasses import dataclass
@dataclasses    # we are adding one more data class by only 4 lines insted of 10-16 line
class fruit2:
    name: str
    calaries: float


class fruit:
    def __init__(self, name:str, calaries: float):
        self.name = name
        self.calaries = calaries

    def __eq__(self, other):
        return  self.__dict__ == other.__dict__


if __name__ == '__main__':
    apple:fruit2 = fruit2('applee', 55)
    apple2:fruit2 = fruit2('applee', 55)
    print(apple ==apple2)
