from rich.console import Console, RenderGroup
from rich.table import Table
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel

console = Console()
greetingStyle = "bold white on red"
processStyle = "bold green"
fields = 0
max_value_field = 10
min_value_field = 5
battlefield = []
battlefield_new = dict()


def greeting():
    console.print("Welcome to cryptor 😀!", style=greetingStyle, justify="center")


def set_dimensions():
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


def field():
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
    layout["body"].update(field())
    layout["box1"].update(box_equipment())
    layout["box2"].update(box_rules_and_commands())
    layout["footer"].update(header())

    console.print(layout)


def main():
    greeting()
    set_dimensions()
    while True:
        show_layout()
        break
        com = console.input("Enter [i bold red]option[/i bold red]?: ")


if __name__ == "__main__":
    main()
