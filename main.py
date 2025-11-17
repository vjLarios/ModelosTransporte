# main.py
import sys
from pyfiglet import Figlet
from rich.console import Console
from rich.align import Align
import questionary

from Methods.Vogel import metodo_vogel

console = Console()

def show_logo():
    """Muestra un logo ASCII centrado con estilo."""
    f = Figlet(font='big')
    logo = f.renderText('Modelos de Transporte')
    console.print(Align.center(logo, vertical="middle"), style="bold cyan")

def interactive_menu():
    """Menú principal con questionary que llama a módulos externos."""
    while True:
        console.clear()
        show_logo()

        opciones = [
            "Método de Vogel",
            "Salir"
        ]

        seleccion = questionary.select(
            "Elige un método para resolver tu problema:",
            choices=opciones,
            qmark="",
            pointer="➡️  ",
            style=questionary.Style([
                ('pointer', 'fg:#ff9d00 bold'),
                ('highlighted', 'fg:#ff9d00 bold'),
            ])
        ).ask()

        if seleccion == "Salir" or seleccion == None:
            console.print("\n¡Hasta pronto!", style="bold green")
            break
        elif seleccion == "Método de Vogel":
            metodo_vogel()

if __name__ == "__main__":
    try:
        interactive_menu()
    except KeyboardInterrupt:
        console.print("\n\nInterrumpido por el usuario. ¡Adiós!", style="bold red")
        sys.exit(0)