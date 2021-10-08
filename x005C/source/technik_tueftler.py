#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

battlefield = [[0] * 10 for i in range(10)]


def print_battlefield(list):
    for row in list:
        print('  '.join([str(col) for col in row]))


def combine_numbers(num_1: int, num_2: int) -> int:
    return (num_1 * 10) + num_2


def break_numbers(num: int) -> (int, int):
    return num // 10, num % 10


def set_battleship_in_direction(row: int, col: int, size: int, func_started: bool, direction: str, battle_field: list) \
        -> bool:
    size -= 1
    if size <= 0: return True
    if not func_started:
        battle_field[row][col] = "X"
    if direction == "n":
        if row - 1 < 0:  # ToDo: Fehlercheck kann gelöscht werden
            print(f'Fehler in Setzrichtung {direction}')
            return False
        if battle_field[row - 1][col] == 0:
            battle_field[row - 1][col] = "X"
            set_battleship_in_direction(row - 1, col, size, True, "n", battle_field)
        else:
            print(f'Fehler Feld ist besetzt {direction}')
            return False
    elif direction == "e":  # ToDo: Fehlercheck kann gelöscht werden
        if col + 1 > 9:
            print(f'Fehler in Setzrichtung {direction}')
            return False
        if battle_field[row][col + 1] == 0:
            battle_field[row][col + 1] = "X"
            set_battleship_in_direction(row, col + 1, size, True, "e", battle_field)
        else:
            print(f'Fehler Feld ist besetzt {direction}')
            return False
    elif direction == "s":  # ToDo: Fehlercheck kann gelöscht werden
        if row + 1 > 9:
            print(f'Fehler in Setzrichtung {direction}')
            return False
        if battle_field[row + 1][col] == 0:
            battle_field[row + 1][col] = "X"
            set_battleship_in_direction(row + 1, col, size, True, "s", battle_field)
        else:
            print(f'Fehler Feld ist besetzt {direction}')
            return False
    elif direction == "w":
        if col - 1 < 0:  # ToDo: Fehlercheck kann gelöscht werden
            print(f'Fehler in Setzrichtung {direction}')
            return False
        if battle_field[row][col - 1] == 0:
            battle_field[row][col - 1] = "X"
            set_battleship_in_direction(row, col - 1, size, True, "w", battle_field)
        else:
            print(f'Fehler Feld ist besetzt {direction}')
            return False


def next_field_valid(row: int, col: int, size: int, directions: str, battle_field: list) -> bool:
    print(f'Aktueller Index: [{row}][{col}]')
    size -= 1
    if size <= 0:
        print(f'Richtung {directions}')
        return True
    if directions == "n":
        print(f'Call: [{row}][{col}] und Size: {size}]')
        if row - 1 < 0:
            print(f'Fehler in Richtung {directions}')
            return False
        if battle_field[row - 1][col] != 0:
            print(f'Fehler Feld ist besetzt [{row - 1}][{col}]')
            return False
        return next_field_valid(row - 1, col, size, directions, battle_field)
    elif directions == "e":
        print(f'Call: [{row}][{col}] und Size: {size}]')
        if col + 1 > 9:
            print(f'Fehler in Richtung {directions}')
            return False
        if battle_field[row][col + 1] != 0:
            print(f'Fehler Feld ist besetzt [{row}][{col + 1}]')
            return False
        return next_field_valid(row, col + 1, size, directions, battle_field)
    elif directions == "s":
        print(f'Call: [{row}][{col}] und Size: {size}]')
        if row + 1 > 9:
            print(f'Fehler in Richtung {directions}')
            return False
        if battle_field[row + 1][col] != 0:
            print(f'Fehler Feld ist besetzt [{row + 1}][{col}]')
            return False
        return next_field_valid(row + 1, col, size, directions, battle_field)
    elif directions == "w":
        print(f'Call: [{row}][{col}] und Size: {size}]')
        if col - 1 < 0:
            print(f'Fehler in Richtung {directions}')
            return False
        if battle_field[row][col - 1] != 0:
            print(f'Fehler Feld ist besetzt [{row}][{col - 1}]')
            return False
        return next_field_valid(row, col - 1, size, directions, battle_field)


def set_new_battleship(battle_field: list, ship_size: int) -> None:
    directions = ["n", "e", "s", "w"]
    random.shuffle(directions)
    # Generate a list of values (row-index + col-index) for easy access in a loop which field has to be checked
    fields_for_new_ship = [combine_numbers(row, col)
                           for row in range(len(battle_field))
                           for col in range(len(battle_field[row]))
                           if battle_field[row][col] == 0]
    random.shuffle(fields_for_new_ship)  # shuffle list for a random check if field is valid for ship

    find_place = False
    for field in fields_for_new_ship:
        row, col = break_numbers(field)
        for direction in directions:
            if next_field_valid(row, col, ship_size, direction, battle_field) is True:
                set_battleship_in_direction(row, col, ship_size, False, direction, battle_field)
                print(f'Neues Schiff bei [{row}][{col}] in Richtung {direction} '
                      f'mit einer Schiffsgröße von {ship_size} möglich.')
                find_place = True
                break
        if find_place:
            break


def main():
    print("--------Start--------")
    print_battlefield(battlefield)
    print("--------Ship 1--------")
    set_new_battleship(battlefield, 4)
    print_battlefield(battlefield)


if __name__ == "__main__":
    main()
