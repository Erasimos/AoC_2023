import ut


def get_input():
    puzzle_input = ut.read_file()
    return puzzle_input


def get_schematic_element(schematics, row, col):

    if row < 0 or row >= len(schematics): 
        return '.'
    if col < 0 or col >= len(schematics[0]):
        return '.'
    
    else:
        return schematics[row][col]


def has_neighbours(schematics, row, col, is_first = False, is_last = False):
    for neigbhour in [(0, 1), (1, 1), (0, -1), (1, -1), (-1, 1), (-1, -1)]:
        new_row = row + neigbhour[1]
        new_col = col + neigbhour[0]

        char = get_schematic_element(schematics, new_row, new_col)

        if not char == '.':
            return True
        
    if is_first:
        new_col = col - 1

        char = get_schematic_element(schematics, row, new_col)

        if not char == '.':
            return True

    if is_last:
        new_col = col + 1

        char = get_schematic_element(schematics, row, new_col)

        if not char == '.':
            return True
    

    return False
                

def get_gear_ratio_sum(schematics):
    pass


def get_engine_part_sum(schematics):
    sum = 0
    
    is_num = False
    is_part_number = False
    current_number = ''
    is_first = True
    is_last = False

    for row in range(len(schematics)):

        if is_num and is_part_number:
            print('part number', current_number)
            sum += int(current_number)

        is_num = False
        is_part_number = False
        current_number = ''
        is_first = True
        is_last = False
        for col in range(len(schematics[0])):
            char = schematics[row][col]
            if str.isnumeric(char):
                if not str.isnumeric(get_schematic_element(schematics, row, col + 1)):
                    is_last = True
                is_num = True
                current_number += char
                if has_neighbours(schematics, row, col, is_first, is_last):
                    is_part_number = True

                is_first = False

            else:

                if is_num and is_part_number:
                    print('part number', current_number)
                    sum += int(current_number)

                is_num = False
                is_part_number = False
                current_number = ''
                is_first = True
                is_last = False
    return sum



def part_one():

    schematics = get_input()

    print('schematics', schematics)

    answer = get_engine_part_sum(schematics)

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()