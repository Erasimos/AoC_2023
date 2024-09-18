import os




class Position:


    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))


    def __lt__(self, other): 
        if isinstance(other, Position):
            return (self.x + self.y) < (other.x + other.y)
        return NotImplemented
    

    def __neg__(self):
        """Negates the x and y values"""
        if isinstance(self, Position):
            return Position(-self.x, -self.y)
        return NotImplemented

def manhattan(pos_1: Position, pos_2: Position):
    return abs(pos_1.x - pos_2.x) + abs(pos_1.y - pos_2.y)


UDLR = [Position(1, 0), Position(-1, 0), Position(0, 1), Position(0, -1)]
NEIGHBORS_2D = [Position(1, 0), Position(-1, 0), Position(0, 1), Position(0, -1), Position(1, 1), Position(1, -1), Position(-1, 1), Position(-1, -1)]

ZERO_POS = Position(0, 0)
RIGHT = Position(1, 0)
LEFT = Position(-1, 0)
UP = Position(0, -1)
DOWN = Position(0, 1)

def read_file(file='input.txt'):
    filepath = os.getcwd() + '/' + file
    f = open(filepath, 'r')
    content = f.read().splitlines()
    f.close()
    return content


def print_answer(day, part, answer):
    print('The answer to day: ', day, ' part ', part, ' is: ', answer)
    





