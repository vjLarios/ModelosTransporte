import sys
from pyfiglet import Figlet
from rich.console import Console
from rich.align import Align
import questionary

from Methods.Vogel import metodo_vogel
from Methods.paso_secuencial import metodo_paso_secuencial

console = Console()

def show_logo():
    """Muestra un logo ASCII centrado con estilo."""
    f = Figlet(font='big')
    logo = f.renderText('Modelos de Transporte')
    console.print(Align.center(logo, vertical="middle"), style="bold cyan")

def interactive_menu():
    """Menú principal que guarda la solución de Vogel en memoria."""
    
    # Aquí se guarda la solución. Si se ejecuta Vogel, se actualiza.
    solucion_guardada = None

    while True:
        console.clear()
        show_logo()

        opciones = [
            "Método de Vogel",
            "Método de Paso Secuencial",
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

        if seleccion == "Salir" or seleccion is None:
            console.print("\n¡Hasta pronto!", style="bold green")
            break
            
        elif seleccion == "Método de Vogel":
            # Ejecutamos Vogel y guardamos el resultado en la variable
            solucion_guardada = metodo_vogel()
            
        elif seleccion == "Método de Paso Secuencial":
            # Pasamos la variable (tenga datos o sea None)
            metodo_paso_secuencial(solucion_guardada)

if __name__ == "__main__":
    try:
        interactive_menu()
    except KeyboardInterrupt:
        console.print("\n\nInterrumpido por el usuario. ¡Adiós!", style="bold red")
        sys.exit(0)