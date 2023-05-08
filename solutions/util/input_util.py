# Utility for reading inputs quickly


def read_input_file(day:int) -> list:
    filename = f'input/day{str(day).zfill(2)}_input.txt'
    print("Input file: ", filename)
    with open(filename) as f:
        lines = f.readlines()
        
    # Remove new line char
    return [l.replace('\n', '') for l in lines]


def read_input_file_part(day:int, part:int) -> list:
    filename = f'input/day{str(day).zfill(2)}_{part}_input.txt'
    print("Input file: ", filename)
    with open(filename) as f:
        lines = f.readlines()
        
    # Remove new line char
    return [l.replace('\n', '') for l in lines]