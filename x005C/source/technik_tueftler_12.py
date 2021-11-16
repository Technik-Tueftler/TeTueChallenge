#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
BATTLEFIELD_LENGTH = 10

battlefield = [0 for i in range(BATTLEFIELD_LENGTH*BATTLEFIELD_LENGTH)]


def print_battlefield(battle_field):
    for row in range(BATTLEFIELD_LENGTH):
        print('  '.join([str(battle_field[row*BATTLEFIELD_LENGTH+col]) for col in range(BATTLEFIELD_LENGTH)]))


def combine_numbers(num_1: int, num_2: int) -> str:
    return f"{num_1}{num_2}"


def break_numbers(num: str) -> (int, int):
    return int(num[0]), int(num[1])


def set_battleship_in_direction(row: int, col: int, size: int, func_started: bool, ship_sign: str, direction: str,
                                battle_field: list) -> bool:
    size -= 1
    if size <= 0: return True
    if not func_started:
        battle_field[row * BATTLEFIELD_LENGTH + col] = ship_sign
    if direction == "n": # Enums
        battle_field[(row - 1) * BATTLEFIELD_LENGTH + col] = ship_sign
        set_battleship_in_direction(row - 1, col, size, True, ship_sign, "n", battle_field)
    elif direction == "e":
        battle_field[row * BATTLEFIELD_LENGTH + (col + 1)] = ship_sign
        set_battleship_in_direction(row, col + 1, size, True, ship_sign, "e", battle_field)
    elif direction == "s":
        battle_field[(row + 1) * BATTLEFIELD_LENGTH + col] = ship_sign
        set_battleship_in_direction(row + 1, col, size, True, ship_sign, "s", battle_field)
    elif direction == "w":
        battle_field[row * BATTLEFIELD_LENGTH + (col - 1)] = ship_sign
        set_battleship_in_direction(row, col - 1, size, True, ship_sign, "w", battle_field)


def next_field_valid(row: int, col: int, size: int, directions: str, battle_field: list) -> bool:
    size -= 1
    if size <= 0: return True
    if directions == "n":
        if row - 1 < 0: return False  # end of playing field reached
        if battle_field[(row - 1) * BATTLEFIELD_LENGTH + col] != 0: return False  # playing field is occupied
        return next_field_valid(row - 1, col, size, directions, battle_field)
    elif directions == "e":
        if col + 1 > 9: return False
        if battle_field[row * BATTLEFIELD_LENGTH + (col + 1)] != 0: return False
        return next_field_valid(row, col + 1, size, directions, battle_field)
    elif directions == "s":
        if row + 1 > 9: return False
        if battle_field[(row + 1) * BATTLEFIELD_LENGTH + col] != 0: return False
        return next_field_valid(row + 1, col, size, directions, battle_field)
    elif directions == "w":
        if col - 1 < 0: return False
        if battle_field[row * BATTLEFIELD_LENGTH + (col - 1)] != 0: return False
        return next_field_valid(row, col - 1, size, directions, battle_field)


def set_new_battleship(battle_field: list, ship_size: int, ship_sign: str) -> None:
    directions = ["n", "e", "s", "w"]
    random.shuffle(directions)
    # Generate a list of values (row-index + col-index) for easy access in a loop which field has to be checked
    fields_for_new_ship = [combine_numbers(row, col)
                           for row in range(BATTLEFIELD_LENGTH)
                           for col in range(BATTLEFIELD_LENGTH)
                           if battle_field[row * BATTLEFIELD_LENGTH + col] == 0]
    random.shuffle(fields_for_new_ship)  # shuffle list for a random check if field is valid for ship

    find_place = False
    for field in fields_for_new_ship:
        row, col = break_numbers(field)
        for direction in directions:
            if next_field_valid(row, col, ship_size, direction, battle_field) is True:
                set_battleship_in_direction(row, col, ship_size, False, ship_sign, direction, battle_field)
                find_place = True
                break
        if find_place:
            break


def measure_performance():
    set_new_battleship(battlefield, 5, "5")


def main():
    print("--------Start--------")
    set_new_battleship(battlefield, 3, "1")
    set_new_battleship(battlefield, 3, "2")
    set_new_battleship(battlefield, 3, "3")
    set_new_battleship(battlefield, 4, "4")
    set_new_battleship(battlefield, 5, "5")
    print_battlefield(battlefield)


if __name__ == "__main__":
    main()
