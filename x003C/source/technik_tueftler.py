import os
import rich
import sys
from rich.console import Console, RenderGroup
from rich.table import Table
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich import box
from time import sleep
import math

console = Console()
greetingStyle = "bold white on red"
processStyle = "bold green"
fields = 0
max_value_field = 10
min_value_field = 5
battlefield = []
battlefield_new = dict()


def greeting():
    console.print("Welcome to cryptor!", style=greetingStyle, justify="center")


def set_dimensions():
    global fields
    global battlefield
    while True:
        console.print("Einstellungen", style="white on green", justify="center")
        try:
            fields = int(console.input("[green]Spielfelddimension eingeben[green]: "))
            if min_value_field <= fields <= max_value_field: break
            console.print(f"Bitte eine Zahl zwischen {min_value_field} und {max_value_field} eingeben", justify="left")
        except:
            console.print(f"Bitte eine Zahl zwischen {min_value_field} und {max_value_field} eingeben", justify="left")

    battlefield = [["O  "] * fields for i in range(fields)]


def set_dimensions_new():
    global fields
    global battlefield_new
    while True:
        console.print("Einstellungen", style="white on green", justify="center")
        try:
            fields = int(console.input("[green]Spielfelddimension eingeben[green]: "))
            if min_value_field <= fields <= max_value_field: break
            console.print(f"Bitte eine Zahl zwischen {min_value_field} und {max_value_field} eingeben", justify="left")
        except:
            console.print(f"Bitte eine Zahl zwischen {min_value_field} und {max_value_field} eingeben", justify="left")

    for zeilen in range(fields):
        for spalten in range(fields):
            battlefield_new[chr(ord('@') + zeilen + 1) + str(spalten)] = " O "

def header():
    grid = Table.grid(expand=True)
    grid.add_column(justify="center")
    grid.add_row("[b]TeTü Challenge 3 - Schiffe versenken [/b]")
    return Panel(grid, style="white on blue")


def field_new():
    table = Table()
    table.add_column("", justify="center")

    # Eigenes Feld
    test_string2 = "    [blue]"
    for i in range(fields):
        test_string2 = test_string2 + (chr(ord('@') + i + 1) + "   ")
    test_string2 = test_string2 + "[/blue]\n\n"

    for line in range(fields):
        test_string2 = test_string2 + "[blue]" + str(line) + "[/blue]  "
        for column in range(fields):
            test_string2 = test_string2 + battlefield_new[chr(ord('@') + column + 1) + str(line)] + " "
        test_string2 = test_string2 + "\n\n"

    # Gegnerisches Feld
    test_string4 = "    [red]"
    for i in range(fields):
        test_string4 = test_string4 + (chr(ord('@') + i + 1) + "   ")
    test_string4 = test_string4 + "[/red]\n\n"

    for line in range(fields):
        test_string4 = test_string4 + "[red]" + str(line) + "[/red]  "
        for column in range(fields):
            test_string4 = test_string4 + battlefield_new[chr(ord('@') + column + 1) + str(line)] + " "
        test_string4 = test_string4 + "\n\n"

    return Panel(Align.center(RenderGroup(Align.center(test_string4), Align.center(test_string2)), vertical="middle",), title="Spielfeld", border_style="white")


def field():
    table = Table()
    table.add_column("", justify="center")

    for i in range(len(battlefield)):
        table.add_column(str(i+1), justify="center")

    for i, element in enumerate(battlefield):
        table.add_row(chr(ord('@')+i+1), *element)

    return Panel(table, title="Spielfeld", border_style="white")


def box_equipment():
    test_string3 = "[green]  /\      /\      [red]/\\\n[/red]"   \
                   "[green] /  \    /  \    [red]/  \\\n[/red]"  \
                   "[green] |  |    |  |    [red]|  |\n[/red]"   \
                   "[green] |  |    |  |    [red]|  |\n[/red]"   \
                   "[green]/ == \  / == \  [red]/ == \\\n[/red]" \
                   "[green]|/**\|  |/**\|  [red]|/**\|\n[/red]"
    return Panel(test_string3, title="Ausrüstung", border_style="white")


def box_rules_and_commands():
    picture_battleships = "Test\n"

    return Panel(picture_battleships, title="Regeln und Befehle", border_style="white")


def show_layout():
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=1),
    )
    layout["side"].split(Layout(name="box1", ratio=1), Layout(name="box2", ratio=2))

    layout["header"].update(header())
    layout["body"].update(field_new())
    layout["box1"].update(box_equipment())
    layout["box2"].update(box_rules_and_commands())
    layout["footer"].update(header())

    console.print(layout)


def main():
    greeting()
    set_dimensions_new()
    while True:
        show_layout()
        break
        com = console.input("Enter [i bold red]option[/i bold red]?: ")

        if com == "1":
            name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
            console.print("File has been encrypted with RSA", style=processStyle, justify="left")
            console.clear()
        if com == "2":
            name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
            console.print("File has been decrypted with RSA", style=processStyle, justify="left")
        if com == "3":
            name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
            console.print("File has been encrypted with aes-256-cbc", style=processStyle, justify="left")
        if com == "4":
            name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
            console.print("File has been decrypted with aes-256-cbc", style=processStyle, justify="left")
        if com == "q":
            console.print("Bye ...", style=processStyle, justify="left")
            sys.exit()

def main2():
    set_dimensions()
    #print(battlefield)
    #for i in range(len(battlefield)):
        #print(battlefield[i])
        #print(i+1)
    test_string = ""
    for i, line in enumerate(battlefield):
        for j, column in enumerate(line):
            test_string = test_string + " O "
        test_string = test_string + "\n\n"

    print(test_string)

    """    print(test_string)
    numberss = [(str(i+1) + "  ")  for i in range(10)]
    print(*numberss)
    battlefield2 = [["O  "] * 10 for i in range(10)]
    for element in battlefield2:
        
    print(battlefield2)"""

    set_dimensions_new()

    test_string2 = "    "
    for i in range(fields):
        test_string2 = test_string2 + (chr(ord('@') + i + 1) + "   ")
    test_string2 = test_string2 + "\n\n"

    for line in range(fields):
        test_string2 = test_string2 + str(line) + "  "
        for column in range(fields):
            test_string2 = test_string2 + battlefield_new[chr(ord('@') + column + 1) + str(line)] + " "
        test_string2 = test_string2 + "\n\n"
    print(test_string2)

def set_dimensions():
    global fields
    global battlefield
    while True:
        console.print("Einstellungen", style="white on green", justify="center")
        try:
            fields = int(console.input("[green]Spielfelddimension eingeben[green]: "))
            if min_value_field < fields < max_value_field: break
            console.print(f"Bitte eine Zahl zwischen {min_value_field} und {max_value_field} eingeben", justify="left")
        except:
            console.print(f"Bitte eine Zahl zwischen {min_value_field} und {max_value_field} eingeben", justify="left")

    battlefield = [["O  "] * fields for i in range(fields)]

if __name__ == "__main__":
    main()
    #main2()