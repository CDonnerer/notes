"""Day 8 of AoC. Image data parsing.
"""
import numpy as np
import pandas as pd


def parse_image(image: str, width: int, height: int):
    """Parse image str, based on width and height
    """
    split_img = [pixel for pixel in image]
    n_layers = int(len(split_img) / (width * height))

    layers = list()
    start = 0
    stop = width

    for _ in range(n_layers):
        layer = np.zeros(shape=(height, width))

        for j in range(height):
            layer[j, :] = split_img[start:stop]
            start += width
            stop += width

        layers.append(layer)

    return layers


def load_input(path="input.dat"):
    return str(np.loadtxt(path, dtype=str))


def print_image(image):
    """Given input image as 2d np.ndarray, we print nicely to console
    """
    df = pd.DataFrame(image, dtype=int)
    df = df.replace({0: " ", 1: "o"})  # for ease of reading the chars
    print(df)  # print to console


def part_1(layers):
    l_zeros = list()

    for layer in layers:
        n_zeros = sum(sum(layer == 0))
        l_zeros.append(n_zeros)

    fewest_zeros = np.array(l_zeros).argmin()

    n_ones = sum(sum(layers[fewest_zeros] == 1))
    n_twos = sum(sum(layers[fewest_zeros] == 2))

    return n_ones * n_twos


def part_2(layers):
    final_image = np.zeros_like(layers[0])
    previous_filled = np.zeros_like(final_image)
    previous_filled = False

    for layer in layers:
        is_transparent = layer == 2
        # fill pixels if not previously filled and not transparent now
        to_fill = ~previous_filled & ~is_transparent
        final_image[to_fill] = layer[to_fill]
        previous_filled = np.logical_or(previous_filled, to_fill)

    return final_image


def main():
    """
    """
    # example_input = "123456789012"
    # layers = parse_image(image=example_input, width=25, height=6)

    image = load_input()
    layers = parse_image(image=image, width=25, height=6)

    solution = part_1(layers)
    print(solution)

    # Part 2.

    # example_image = "0222112222120000"
    # layers = parse_image(image=example_image, width=2, height=2)

    final_image = part_2(layers)
    print_image(final_image)


if __name__ == "__main__":
    main()
