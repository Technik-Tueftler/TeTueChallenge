from textual.app import App
from textual import events
from textual.view import View
from textual.widgets import Placeholder, Button
from textual.layouts.grid import GridLayout


class Streamdeck(App):
    async def on_load(self, event: events.Load) -> None:
        await self.bind("q,ctrl+c", "quit", "Quit")

    async def on_startup(self, event: events.Startup) -> None:

        layout = GridLayout()
        await self.push_view(View(layout=layout))

        layout.add_column(fraction=1, name="tab_1")
        layout.add_column(fraction=1, name="tab_2")
        layout.add_column(fraction=1, name="tab_3")
        layout.add_column(fraction=1, name="tab_4")

        layout.add_row(fraction=1, name="tab")
        layout.add_row(fraction=1, name="top")
        layout.add_row(fraction=1, name="middle")
        layout.add_row(fraction=1, name="bottom")

        layout.add_areas(
            button_t1="tab_1,tab",
            button_t2="tab_2,tab",
            button_t3="tab_3,tab",
            button_t4="tab_4,tab",
            button_00="tab_1,top",
            button_01="tab_2,top",
            button_02="tab_3,top",
            button_03="tab_4,top",
            button_10="tab_1,middle",
            button_11="tab_2,middle",
            button_12="tab_3,middle",
            button_13="tab_4,middle",
            button_20="tab_1,bottom",
            button_21="tab_2,bottom",
            button_22="tab_3,bottom",
            button_23="tab_4,bottom",
        )

        layout.place(
            button_t1=Button(style="white on rgb(51,51,51)", name="tab_button_1"),
            button_t2=Button(style="white on rgb(51,51,51)", name="tab_button_2"),
            button_t3=Button(style="white on rgb(51,51,51)", name="tab_button_3"),
            button_t4=Button(style="white on rgb(51,51,51)", name="tab_button_4"),
            button_00=Button(style="white on rgb(51,51,51)", name="button_00"),
            button_01=Button(style="white on rgb(51,51,51)", name="button_01"),
            button_02=Button(style="white on rgb(51,51,51)", name="button_02"),
            button_03=Button(style="white on rgb(51,51,51)", name="button_03"),
            button_10=Button(style="white on rgb(51,51,51)", name="button_10"),
            button_11=Button(style="white on rgb(51,51,51)", name="button_11"),
            button_12=Button(style="white on rgb(51,51,51)", name="button_12"),
            button_13=Button(style="white on rgb(51,51,51)", name="button_13"),
            button_20=Button(style="white on rgb(51,51,51)", name="button_20"),
            button_21=Button(style="white on rgb(51,51,51)", name="button_21"),
            button_22=Button(style="white on rgb(51,51,51)", name="button_22"),
            button_23=Button(style="white on rgb(51,51,51)", name="button_23"),
        )


Streamdeck.run(title="Streamdeck")
