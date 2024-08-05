import os


Neighbours_2D = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
UDLR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def read_file(file='input.txt'):
    filepath = os.getcwd() + '/2023/' + file
    f = open(filepath, 'r')
    content = f.read().splitlines()
    f.close()
    return content


def print_answer(day, part, answer):
    print('The answer to day: ', day, ' part ', part, ' is: ', answer)
    



