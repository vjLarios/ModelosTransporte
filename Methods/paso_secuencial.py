from rich.console import Console
from rich.table import Table
from Methods.Vogel import metodo_vogel

console = Console()

def obtener_camino_cerrado(asignaciones, celda_vacia):
    """Encuentra un ciclo cerrado (Stepping Stone)"""
    i_vacia, j_vacia = celda_vacia
    
    celdas_fila = [(i_vacia, j) for j in range(len(asignaciones[0])) 
                   if asignaciones[i_vacia][j] > 0 and j != j_vacia]
    
    celdas_col = [(i, j_vacia) for i in range(len(asignaciones)) 
                  if asignaciones[i][j_vacia] > 0 and i != i_vacia]
    
    for celda_fila in celdas_fila:
        for celda_col in celdas_col:
            i1, j1 = celda_fila
            i2, j2 = celda_col
            
            if asignaciones[i2][j1] > 0:
                return [celda_vacia, celda_fila, (i2, j1), celda_col]
    
    return None

def calcular_costo_ciclo(ciclo, costos):
    costo_neto = 0
    signo = 1
    formula_str = ""
    
    for i, j in ciclo:
        simbolo = "+" if signo > 0 else "-"
        costo_neto += signo * costos[i][j]
        formula_str += f" {simbolo}{costos[i][j]}"
        signo *= -1
    
    return costo_neto, formula_str

def aplicar_ciclo(asignaciones, ciclo, theta):
    signo = 1
    for i, j in ciclo:
        asignaciones[i][j] += signo * theta
        signo *= -1

def imprimir_tabla_detallada(costos, asignaciones, titulo="Estado Actual"):
    table = Table(title=titulo, show_header=True, header_style="bold magenta")
    filas = len(costos)
    cols = len(costos[0])
    
    table.add_column("Origen", style="dim", width=12)
    for j in range(cols):
        table.add_column(f"D{j+1}", width=15)
    
    for i in range(filas):
        row_cells = [f"O{i+1}"]
        for j in range(cols):
            costo = costos[i][j]
            asig = asignaciones[i][j]
            if asig > 0:
                texto = f"[bold green]{asig}[/bold green]\n[dim]({costo})[/dim]"
            else:
                texto = f"[dim]{asig}[/dim]\n[dim]({costo})[/dim]"
            row_cells.append(texto)
        table.add_row(*row_cells)
    
    console.print(table)

def metodo_paso_secuencial(datos_previos=None):
    """
    Algoritmo de Paso Secuencial Detallado.
    """
    console.clear()
    console.rule("[bold blue]MÉTODO DEL PASO SECUENCIAL (OPTIMIZACIÓN)[/bold blue]")
    console.print("[italic]Este método busca mejorar una solución inicial existente.[/italic]\n")
    
    solucion_vogel = None

    # LOGICA PARA USAR DATOS PREVIOS O CORRER VOGEL
    if datos_previos:
        console.print("[bold green]✓ Utilizando solución previa guardada en memoria.[/bold green]")
        solucion_vogel = datos_previos
    else:
        console.print("[bold yellow]⚠ No hay solución en memoria.[/bold yellow]")
        console.print("Se ejecutará el [bold]Método de Vogel[/bold] primero para obtener la solución inicial.")
        input("Presiona Enter para comenzar Vogel...")
        solucion_vogel = metodo_vogel()
        if solucion_vogel is None:
            return None
    
    # Extraer datos
    asignaciones = solucion_vogel['asignaciones']
    costos = solucion_vogel['costos']
    oferta = solucion_vogel['oferta']
    demanda = solucion_vogel['demanda']
    costo_inicial = solucion_vogel['costo_total']
    
    filas = len(oferta)
    cols = len(demanda)
    
    console.print("\n" + "="*50)
    console.print(f"[bold white on blue] INICIO DE OPTIMIZACIÓN [/bold white on blue]")
    console.print(f"[bold]Costo Inicial (Vogel): ${costo_inicial}[/bold]")
    
    imprimir_tabla_detallada(costos, asignaciones, "Solución Inicial")
    input("Presiona Enter para comenzar a buscar mejoras...")
    
    iteracion = 1
    optimo_encontrado = False
    
    while not optimo_encontrado:
        console.rule(f"[bold orange1]ITERACIÓN {iteracion}[/bold orange1]")
        
        mejor_celda = None
        mejor_ciclo = None
        mejor_indice = 0
        
        console.print("\n[bold]Analizando celdas no básicas (vacías):[/bold]")
        
        # Análisis detallado de celdas vacías
        for i in range(filas):
            for j in range(cols):
                if asignaciones[i][j] == 0:  # Es celda vacía
                    ciclo = obtener_camino_cerrado(asignaciones, (i, j))
                    
                    if ciclo:
                        indice, formula = calcular_costo_ciclo(ciclo, costos)
                        
                        # Mostrar detalle de cálculo
                        color = "green" if indice < 0 else "red"
                        console.print(f"  • Celda (O{i+1}, D{j+1}):")
                        console.print(f"    Ciclo: {[(r+1, c+1) for r, c in ciclo]}")
                        console.print(f"    Cálculo: {formula} = [bold {color}]{indice}[/bold {color}]")
                        
                        if indice < mejor_indice:
                            mejor_indice = indice
                            mejor_celda = (i, j)
                            mejor_ciclo = ciclo
        
        console.print(f"\n[bold]Resumen de iteración {iteracion}:[/bold]")
        console.print(f"  Mejor índice de mejora encontrado: {mejor_indice}")
        
        input("Presiona Enter para evaluar resultados...")
        
        if mejor_indice < 0:
            console.print(f"\n[bold green]¡MEJORA ENCONTRADA![/bold green]")
            console.print(f"La celda (O{mejor_celda[0]+1}, D{mejor_celda[1]+1}) ofrece un ahorro de ${abs(mejor_indice)} por unidad.")
            
            # Calcular theta
            theta = float('inf')
            celdas_resta = []
            for k in range(1, len(mejor_ciclo), 2):
                i, j = mejor_ciclo[k]
                celdas_resta.append(f"(O{i+1},D{j+1})={asignaciones[i][j]}")
                if asignaciones[i][j] < theta:
                    theta = asignaciones[i][j]
            
            console.print(f"Calculando Theta (mínimo valor en celdas negativas del ciclo):")
            console.print(f"  Celdas negativas: {', '.join(celdas_resta)}")
            console.print(f"  [bold cyan]Theta (cantidad a mover) = {theta}[/bold cyan]")
            
            input("Presiona Enter para aplicar cambios...")
            
            # Aplicar el ciclo
            aplicar_ciclo(asignaciones, mejor_ciclo, theta)
            
            console.print("\n[bold]Aplicando reasignación...[/bold]")
            imprimir_tabla_detallada(costos, asignaciones, f"Después de Iteración {iteracion}")
            
            # Recalcular costo
            nuevo_costo = sum(asignaciones[i][j] * costos[i][j] for i in range(filas) for j in range(cols))
            
            console.print(f"\n[bold]Nuevo Costo Acumulado: ${nuevo_costo}[/bold]")
            console.print(f"[bold green]Ahorro en esta iteración: ${abs(mejor_indice * theta)}[/bold green]")
            
            input("\nPresiona Enter para continuar a la siguiente iteración...")
            iteracion += 1
            
        else:
            console.print("\n" + "="*50)
            console.print("[bold green]✅ NO HAY ÍNDICES NEGATIVOS. SOLUCIÓN ÓPTIMA ALCANZADA.[/bold green]")
            optimo_encontrado = True
    
    # SOLUCIÓN FINAL
    console.clear()
    console.rule("[bold green]RESULTADO FINAL[/bold green]")
    
    console.print("\n[bold]MATRIZ DE ASIGNACIÓN ÓPTIMA:[/bold]")
    imprimir_tabla_detallada(costos, asignaciones, "Solución Final")
    
    console.print("\n[bold]DETALLE DE COSTOS FINALES:[/bold]")
    costo_total = 0
    for i in range(filas):
        for j in range(cols):
            if asignaciones[i][j] > 0:
                costo_parcial = asignaciones[i][j] * costos[i][j]
                costo_total += costo_parcial
                console.print(f"  O{i+1} → D{j+1}: {asignaciones[i][j]} × {costos[i][j]} = {costo_parcial}")
    
    console.print(f"\n[bold red] COSTO INICIAL (VOGEL): ${costo_inicial} [/bold red]")
    console.print(f"[bold green on white] COSTO FINAL MÍNIMO: ${costo_total} [/bold green on white]")
    
    ahorro_total = costo_inicial - costo_total
    if ahorro_total > 0:
        console.print(f"\n[bold yellow]✨ ¡OPTIMIZACIÓN EXITOSA! Ahorro total: ${ahorro_total} ✨[/bold yellow]")
    else:
        console.print(f"\n[bold cyan]La solución de Vogel ya era óptima.[/bold cyan]")
    
    input("\nPresiona Enter para volver al menú principal...")