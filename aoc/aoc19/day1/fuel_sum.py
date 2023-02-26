"""Day 1 of the Advent of Code 2019 challenge"""
import numpy as np


def load_masses(path="input.dat"):
    """TODO: fixed paths are not a good idea
    """
    return np.loadtxt(path)


def calculate_fuel(mass):
    """Divide mass by three, round down and subtract 2
    """
    return int(mass / 3) - 2


def part_one(masses):
    """Caclculate the masses for part one of the challenge
    """
    return np.sum([calculate_fuel(mass) for mass in masses])


def part_two(masses):
    """Caclculate the masses for part two of the challenge
    """
    total_fuel = 0

    for mass in masses:
        fuel = calculate_fuel(mass)

        while fuel > 0:
            total_fuel += fuel
            fuel = calculate_fuel(fuel)
    return total_fuel


def main():
    """Load in the masses and Caclculate part one and part two
    """
    masses = load_masses()
    print(f"Answer to part one = {part_one(masses)}")
    print(f"Answer to part two = {part_two(masses)}")


if __name__ == "__main__":
    main()
