from ctypes.wintypes import DOUBLE
from textual.widget import Widget
from textual.reactive import Reactive

from rich.panel import Panel
from rich import print, box

import os, platform


class LeftMenu(Widget):
    """
    Basic information from computer
    """
    #def hola(self):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        panel = Panel(
            "Hello [b]World[/b]",
            title="Menú",
            style=("purple" if self.mouse_over else ""),
            box=box.DOUBLE
        )
        return panel

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

class Terminal(Widget):
    """
    Basic information from computer
    """
    #def hola(self):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        panel = Panel(
            "Hello [b]World[/b]",
            title="Terminal",
            style=("purple" if self.mouse_over else ""),
            box=box.DOUBLE
        )
        return panel
  
    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
        
class PcInfo(Widget):
    """
    Basic information from computer
    """
    #def hola(self):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        os_name = platform.system()
        os_release = platform.release()
        os_edition = platform.win32_edition()
        
        panel = Panel(
            "SO = [b]"+ os_name + " " + os_edition + " " + os_release + "[/b]",
            title="Pc Info",
            style=("purple" if self.mouse_over else ""),
            box=box.DOUBLE
        )
        return panel
     
    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

class Breadcrumbs(Widget):
    """
    Basic information from computer
    """
    #def hola(self):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        panel = Panel(
            "Hello [b]World[/b]",
            title="Ruta",
            style=("purple" if self.mouse_over else ""),
            box=box.DOUBLE
        )
        return panel
    
    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

class Credits(Widget):
    """
    Basic information from computer
    """
    #def hola(self):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        panel = Panel(
            "\nProgram created by [b]Àlex Garcia Vilà[/b]\n"
            +"Opensource License: [b]MIT[/b]\n"
            +"More info: [b]https://github.com/alexgarciavila/[/b]",
            title="Més Informació",
            style=("purple" if self.mouse_over else ""),
            box=box.DOUBLE
        )
        return panel
    
    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False