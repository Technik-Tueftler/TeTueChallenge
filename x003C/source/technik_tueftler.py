#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console


def main():
    console = Console()
    console.print("Hello", "World!", style="bold red")


if __name__ == "__main__":
    main()
