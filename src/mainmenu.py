from textual.app import App
from textual.widgets import Placeholder, Footer
from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.table import Table
from rich.console import RenderableType
from datetime import datetime
from textual import events
import locale

locale.setlocale(locale.LC_TIME, 'ca_ES.UTF-8')

class MainApp(App):
    
    async def on_load(self) -> None:
        """
        Bind keys when app load
        """
        await self.bind("q","quit","Sortir")
        
    async def on_mount(self) -> None:
        self.footer = Footer()
        self.header = Header()
        
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.header, edge="top", size=3)
        
        await self.view.dock(Placeholder(name="header2"), edge="top", size=3)
        await self.view.dock(Placeholder(name="stats"), edge="left", size=40)
        await self.view.dock(Placeholder(name="message"), edge="right", size=40)
        await self.view.dock(Placeholder(name="grid"), edge="top")

class Header(Widget):
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
        return datetime.now().time().strftime("%X")
    
    def get_date(self) -> str:
        formated_date = datetime.today().strftime("%A, %d de %B de %Y")
        return formated_date

    async def on_mount(self, event: events.Mount) -> None:
        self.set_interval(1.0, callback=self.refresh)
    
MainApp.run(title="test", log="test.log")