from textual.app import App
from textual.widgets import Placeholder, Footer
from textual.widget import Widget
from textual.reactive import Reactive
from textual import events

from rich.panel import Panel
from rich.table import Table
from rich.console import RenderableType

from datetime import datetime
import locale
import os

from menu.widgets import PcInfo, LeftMenu, Terminal, Credits, Breadcrumbs

#locale.setlocale(locale.LC_TIME, 'ca_ES.UTF-8')
locale.setlocale(locale.LC_TIME, '')

os.system("")

class MainApp(App):
    
    async def on_load(self) -> None:
        """
        Bind keys when app load
        """
        await self.bind("q","quit","Sortir")
        
    async def on_mount(self) -> None:
        self.footer = Footer()
        self.header = Header()
        self.breadcrumbs = Breadcrumbs()
        
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.header, edge="top", size=3)
        await self.view.dock(self.breadcrumbs, edge="top", size=3)
        
        # Create a grid
        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=1, name="left", size=30)
        grid.add_column(name="center", min_size=30)
        grid.add_column(fraction=1, name="right", size=20)

        grid.add_row(fraction=2, name="top")
        grid.add_row(fraction=2, name="middle")
        grid.add_row(fraction=3, name="bottom")

        grid.add_areas(
            area1="left,top-start|bottom-end",
            area2="center,top-start|bottom-end",
            area3="right,top-start|middle-end",
            area4="right,bottom",
        )

        grid.place(
            area1=LeftMenu(),
            area2=Terminal(),
            area3=PcInfo(),
            area4=Credits(),
        )        


        
        
        # await self.view.dock(Placeholder(name="stats2"), edge="top-left", size=40)

        #await self.view.dock(Placeholder(name="stats"), edge="left", size=40)
        #await self.view.dock(Placeholder(name="message"), edge="right", size=40)
        #await self.view.dock(Placeholder(name="grid"), edge="top")




class Header(Widget):
    """
    Personalized header
    """
    def __init__(
        self,
        *,
        clock: bool = True,
    ) -> None:
        super().__init__()
        self.clock = clock
    clock: Reactive[bool] = Reactive(True)
    
    
    def render(self) -> RenderableType:
        
        header_table = Table.grid(padding=(0, 1), expand=True)
        header_table.add_column(justify="left", ratio=0, width=40)
        header_table.add_column("title", justify="center", ratio=1)
        header_table.add_column("clock", justify="right", width=40)
        header_table.add_row(
            self.get_date(), ":laptop_computer: [b]EduToolkit[/b] :wrench:", self.get_clock() if self.clock else ""
        )
        header: RenderableType
        header = Panel(header_table, style="white on purple4")
        return header
    
    def get_clock(self) -> str:
        """
        Return time
        Returns:
            str: Formated time
        """
        return datetime.now().time().strftime("%X")
    
    def get_date(self) -> str:
        """
        Return complete today date
        Returns:
            str: Formated date
        """
        formated_date = datetime.today().strftime("%A, %d de %B de %Y")
        return formated_date

    async def on_mount(self, event: events.Mount) -> None:
        """
        Refresh header widget every 1 second
        """
        self.set_interval(1.0, callback=self.refresh)


# MainApp.run(title="test", log="test.log")