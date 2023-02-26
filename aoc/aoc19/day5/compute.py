"""Day 2 of advent of code: gravity assist program
"""
import operator

import numpy as np


opcodes = {
    1: operator.add,
    2: operator.mul,
}


def opcode_1(args):
    pass


# def process_instruction(code, starting_pos=0):
#     opcode, mode_1, mode_2, mode_3 = parse_instruction(code[starting_pos])
#
#     # if operation is None:
#     #     return code
#
#     input1 = code[code[starting_pos + 1]]
#     input2 = code[code[starting_pos + 2]]
#     output_val = operation(input1, input2)
#
#     code[code[starting_pos + 3]] = output_val
#     return code


def process(code):
    opcode = code[0]
    starting_pos = 0

    while opcode != 99:
        code = process_instruction(code, starting_pos)
        starting_pos += 4
        opcode = code[starting_pos]

    return code


def load_input(path="input.dat"):
    return list(np.loadtxt(path, delimiter=",").astype(int))


def parse_instruction(instruction):
    opcode = int(str(instruction)[-2:])
    modes = {ii: int(mode) for (ii, mode) in enumerate(str(instruction)[-2::-1])}
    return opcode, modes


def process(code, starting_pos=0):

    instruction = code[starting_pos]

    opcode, modes = parse_instruction(instruction)

    if opcode == 1:
        input1 = code[code[starting_pos + 1]]
        input2 = code[code[starting_pos + 2]]

        output_val = operation(input1, input2)

        code[code[starting_pos + 3]] = output_val

    return code


def main():
    """
    """
    example_input = [1002, 4, 3, 4]

    instruction = example_input[0]

    mode = modes.get(0)
    if mode == 0:
        example
    example_input[1]

    from IPython import embed

    embed()


if __name__ == "__main__":
    main()
