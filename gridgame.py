#!/usr/bin/python

import copy
import readline

def print_grid(grid):
    for line in grid:
        print ''.join(line)

def create_grid(xdim, ydim):
    grid = []
    for x in range(ydim):
        grid.append( ['.'] * 20 )
    return grid

def copy_grid(grid):
    return copy.deepcopy(grid)

def main():
    empty_grid = create_grid(60,15)

    player_x = 2
    player_y = 4

    treasure_x = 8
    treasure_y = 12

    while True:
        screen = copy_grid(empty_grid)
        screen[treasure_y][treasure_x] = 'T'
        screen[player_y][player_x] = 'P'

        print_grid(screen)
        line = raw_input()
        if line == "n":
            player_y -= 1
        elif line == "s":
            player_y += 1


if __name__ == "__main__":
    main()