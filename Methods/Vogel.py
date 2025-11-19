from rich.console import Console
from rich.table import Table

from InsertProblem import get_problem_data

def metodo_vogel():
    """
    Algoritmo de Vogel para resolver problemas de transporte
    """
    console = Console()
    
    console.rule("[bold blue]ALGORITMO DE APROXIMACION DE VOGEL[/bold blue]")
    console.print()

    console.print("\n[bold]INGRESO DE DATOS[/bold]")
    console.print("\n[bold]Se abrirá una ventana para ingresar los datos del problema.[/bold]")
    console.print("\n[bold]Presiona Enter para continuar...")
    input()
    try:
        data = get_problem_data()
    except Exception as e:
        console.print("\n[bold red]⚠ Operación cancelada: Se cerró la ventana sin finalizar.[/bold red]")
        input("Presiona Enter para continuar...")
        return None

    # Verificar si el usuario canceló la entrada de datos
    if data is None:
        console.print("\n[bold red]⚠ Operación cancelada: Se cerró la ventana sin finalizar.[/bold red]")
        input("Presiona Enter para continuar...")
        return None

    oferta = data['oferta']
    demanda = data['demanda']
    costos = data['costos']
    
    console.print("[bold]DATOS DEL PROBLEMA:[/bold]")
    console.print(f"Oferta: {oferta}")
    console.print(f"Demanda: {demanda}")
    
    # Mostrar matriz de costos en tabla
    console.print("\n[bold]Matriz de costos:[/bold]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Origen", style="dim")
    for j in range(len(demanda)):
        table.add_column(f"D{j+1}")
    
    for i, fila in enumerate(costos):
        row = [f"O{i+1}"]
        for costo in fila:
            row.append(str(costo))
        table.add_row(*row)
    
    console.print(table)
    input("Presiona Enter para continuar...")
    
    console.rule("[bold yellow]INICIALIZACION[/bold yellow]")
    
    # Copias para trabajar sin alterar los datos originales
    oferta_actual = oferta[:]
    demanda_actual = demanda[:]
    asignaciones = [[0 for _ in range(len(demanda))] for _ in range(len(oferta))]
    
    console.print(f"Oferta restante: {oferta_actual}")
    console.print(f"Demanda restante: {demanda_actual}")
    
    console.print("\n[bold]Matriz de asignaciones inicial:[/bold]")
    table_asig = Table(show_header=True, header_style="bold magenta")
    table_asig.add_column("Origen", style="dim")
    for j in range(len(demanda)):
        table_asig.add_column(f"D{j+1}")
    
    for i, fila in enumerate(asignaciones):
        row = [f"O{i+1}"]
        for val in fila:
            row.append(str(val))
        table_asig.add_row(*row)
    
    console.print(table_asig)
    input("Presiona Enter para continuar...")
    
    iteracion = 1
    
    while sum(oferta_actual) > 0 and sum(demanda_actual) > 0:
        console.rule(f"[bold green]ITERACION {iteracion}[/bold green]")
        
        # Mostrar matriz actual (solo celdas no cubiertas)
        console.print("\n[bold]MATRIZ DE COSTOS ACTUAL (celdas no asignadas):[/bold]")
        table_actual = Table(show_header=True, header_style="bold magenta")
        table_actual.add_column("Origen", style="dim")
        
        # Agregar solo columnas con demanda restante > 0
        col_indices = []
        for j in range(len(demanda)):
            if demanda_actual[j] > 0:
                table_actual.add_column(f"D{j+1}")
                col_indices.append(j)
        
        for i in range(len(oferta)):
            if oferta_actual[i] > 0:
                row = [f"O{i+1}"]
                for j in col_indices:
                    row.append(str(costos[i][j]))
                table_actual.add_row(*row)
        
        console.print(table_actual)
        input("Presiona Enter para continuar...")
        
        # Calcular penalidades por fila
        console.print("\n[bold blue]CALCULO DE PENALIDADES POR FILA:[/bold blue]")
        penalidades_filas = []
        for i in range(len(oferta)):
            if oferta_actual[i] <= 0:
                penalidades_filas.append(None)
                console.print(f"  Fila {i+1}: Sin oferta disponible -> penalidad = N/A")
                continue
            
            # Obtener costos disponibles en la fila
            costos_disponibles = []
            for j in range(len(demanda)):
                if demanda_actual[j] > 0:
                    costos_disponibles.append(costos[i][j])
            
            if len(costos_disponibles) < 2:
                penalidades_filas.append(0)
                console.print(f"  Fila {i+1}: Solo hay {len(costos_disponibles)} destino(s) disponible(s) -> penalidad = 0")
            else:
                # Ordenar manualmente (bubble sort)
                costos_ord = costos_disponibles[:]
                n = len(costos_ord)
                for k in range(n):
                    for l in range(0, n-k-1):
                        if costos_ord[l] > costos_ord[l+1]:
                            costos_ord[l], costos_ord[l+1] = costos_ord[l+1], costos_ord[l]
                
                penalidad = costos_ord[1] - costos_ord[0]
                penalidades_filas.append(penalidad)
                console.print(f"  Fila {i+1}: Costos disponibles: {costos_disponibles}, ordenados: {costos_ord}")
                console.print(f"           Diferencia entre 2 menores: {costos_ord[1]} - {costos_ord[0]} = {penalidad}")
        
        input("Presiona Enter para continuar...")
        
        # Calcular penalidades por columna
        console.print("\n[bold blue]CALCULO DE PENALIDADES POR COLUMNA:[/bold blue]")
        penalidades_columnas = []
        for j in range(len(demanda)):
            if demanda_actual[j] <= 0:
                penalidades_columnas.append(None)
                console.print(f"  Columna {j+1}: Sin demanda disponible -> penalidad = N/A")
                continue
            
            # Obtener costos disponibles en la columna
            costos_disponibles = []
            for i in range(len(oferta)):
                if oferta_actual[i] > 0:
                    costos_disponibles.append(costos[i][j])
            
            if len(costos_disponibles) < 2:
                penalidades_columnas.append(0)
                console.print(f"  Columna {j+1}: Solo hay {len(costos_disponibles)} origen(s) disponible(s) -> penalidad = 0")
            else:
                # Ordenar manualmente (bubble sort)
                costos_ord = costos_disponibles[:]
                n = len(costos_ord)
                for k in range(n):
                    for l in range(0, n-k-1):
                        if costos_ord[l] > costos_ord[l+1]:
                            costos_ord[l], costos_ord[l+1] = costos_ord[l+1], costos_ord[l]
                
                penalidad = costos_ord[1] - costos_ord[0]
                penalidades_columnas.append(penalidad)
                console.print(f"  Columna {j+1}: Costos disponibles: {costos_disponibles}, ordenados: {costos_ord}")
                console.print(f"           Diferencia entre 2 menores: {costos_ord[1]} - {costos_ord[0]} = {penalidad}")
        
        input("Presiona Enter para continuar...")
        
        # Encontrar la penalidad más alta entre filas y columnas
        max_pen_fila = -1
        max_idx_fila = -1
        for idx, pen in enumerate(penalidades_filas):
            if pen is not None and pen > max_pen_fila:
                max_pen_fila = pen
                max_idx_fila = idx
        
        max_pen_col = -1
        max_idx_col = -1
        for idx, pen in enumerate(penalidades_columnas):
            if pen is not None and pen > max_pen_col:
                max_pen_col = pen
                max_idx_col = idx
        
        console.print(f"\n[bold]PENALIDADES CALCULADAS:[/bold]")
        console.print(f"  Penalidad máxima por filas: {max_pen_fila} en fila {max_idx_fila+1 if max_idx_fila >= 0 else 'N/A'}")
        console.print(f"  Penalidad máxima por columnas: {max_pen_col} en columna {max_idx_col+1 if max_idx_col >= 0 else 'N/A'}")
        
        input("Presiona Enter para continuar...")
        
        # Determinar si es fila o columna con mayor penalidad
        if max_pen_fila >= max_pen_col:
            tipo_seleccion = "fila"
            idx_seleccionado = max_idx_fila
            console.print(f"\n[bold green]SELECCION: Mayor penalidad es por FILA ({max_pen_fila}) en fila {idx_seleccionado+1}[/bold green]")
            
            # Encontrar el costo mínimo en esa fila
            costo_min = float('inf')
            col_min = -1
            for j in range(len(demanda)):
                if demanda_actual[j] > 0 and costos[idx_seleccionado][j] < costo_min:
                    costo_min = costos[idx_seleccionado][j]
                    col_min = j
            
            console.print(f"  En fila {idx_seleccionado+1}, costo mínimo es {costo_min} en columna {col_min+1}")
            
        else:
            tipo_seleccion = "columna"
            idx_seleccionado = max_idx_col
            console.print(f"\n[bold green]SELECCION: Mayor penalidad es por COLUMNA ({max_pen_col}) en columna {idx_seleccionado+1}[/bold green]")
            
            # Encontrar el costo mínimo en esa columna
            costo_min = float('inf')
            fila_min = -1
            for i in range(len(oferta)):
                if oferta_actual[i] > 0 and costos[i][idx_seleccionado] < costo_min:
                    costo_min = costos[i][idx_seleccionado]
                    fila_min = i
            
            console.print(f"  En columna {idx_seleccionado+1}, costo mínimo es {costo_min} en fila {fila_min+1}")
            
            # Cambiar para que use la fila encontrada
            idx_seleccionado = fila_min
            tipo_seleccion = "fila"
            col_min = max_idx_col
        
        input("Presiona Enter para continuar...")
        
        # Realizar la asignación
        cantidad_asignar = min(oferta_actual[idx_seleccionado], demanda_actual[col_min])
        asignaciones[idx_seleccionado][col_min] += cantidad_asignar
        
        console.print(f"\n[bold yellow]ASIGNACION:[/bold yellow]")
        console.print(f"  Asignando {cantidad_asignar} unidades de O{idx_seleccionado+1} a D{col_min+1}")
        console.print(f"  Costo unitario: {costos[idx_seleccionado][col_min]}")
        console.print(f"  Costo total para esta asignación: {cantidad_asignar} x {costos[idx_seleccionado][col_min]} = {cantidad_asignar * costos[idx_seleccionado][col_min]}")
        
        # Actualizar oferta y demanda
        oferta_actual[idx_seleccionado] -= cantidad_asignar
        demanda_actual[col_min] -= cantidad_asignar
        
        console.print(f"  Oferta restante O{idx_seleccionado+1}: {oferta_actual[idx_seleccionado]}")
        console.print(f"  Demanda restante D{col_min+1}: {demanda_actual[col_min]}")
        
        input("Presiona Enter para continuar...")
        
        # Mostrar matriz de asignaciones actual
        console.print("\n[bold]MATRIZ DE ASIGNACIONES ACTUAL:[/bold]")
        table_asig = Table(show_header=True, header_style="bold magenta")
        table_asig.add_column("Origen", style="dim")
        for j in range(len(demanda)):
            table_asig.add_column(f"D{j+1}")
        
        for i, fila in enumerate(asignaciones):
            row = [f"O{i+1}"]
            for val in fila:
                row.append(str(val))
            table_asig.add_row(*row)
        
        console.print(table_asig)
        
        # Verificar si hay fila o columna completamente satisfecha
        if oferta_actual[idx_seleccionado] == 0:
            console.print(f"  -> [bold red]Fila {idx_seleccionado+1} ha sido completamente satisfecha[/bold red]")
        if demanda_actual[col_min] == 0:
            console.print(f"  -> [bold red]Columna {col_min+1} ha sido completamente satisfecha[/bold red]")
        
        input("Presiona Enter para continuar...")
        iteracion += 1
    
    console.rule("[bold blue]SOLUCION FINAL[/bold blue]")
    
    console.print("Matriz de asignaciones final:")
    table_final = Table(show_header=True, header_style="bold magenta")
    table_final.add_column("Origen", style="dim")
    for j in range(len(demanda)):
        table_final.add_column(f"D{j+1}")
    
    for i, fila in enumerate(asignaciones):
        row = [f"O{i+1}"]
        for val in fila:
            row.append(str(val))
        table_final.add_row(*row)
    
    console.print(table_final)
    
    input("Presiona Enter para continuar...")
    
    console.print("\n[bold]Asignaciones detalladas:[/bold]")
    total_costo = 0
    for i in range(len(oferta)):
        for j in range(len(demanda)):
            if asignaciones[i][j] > 0:
                costo_asignacion = asignaciones[i][j] * costos[i][j]
                total_costo += costo_asignacion
                console.print(f"  O{i+1} -> D{j+1}: {asignaciones[i][j]} unidades x {costos[i][j]} = {costo_asignacion}")
    
    console.print(f"\n[bold green]COSTO TOTAL DE TRANSPORTE: {total_costo}[/bold green]")
    
    input("Presiona Enter para continuar...")
    
    console.print("\n[bold]Verificación de oferta y demanda:[/bold]")
    console.print(f"Oferta total original: {sum(oferta)}")
    console.print(f"Demanda total original: {sum(demanda)}")
    console.print(f"Suma de asignaciones: {sum(sum(fila) for fila in asignaciones)}")
    
    input("Presiona Enter para continuar...")
    
    console.rule("[bold blue]FIN DEL ALGORITMO DE VOGEL[/bold blue]")
    
    # EMPAQUETAR Y RETORNAR PARA QUE MAIN LO GUARDE
    solucion_vogel = {
        'asignaciones': asignaciones,
        'costo_total': total_costo,
        'oferta': oferta,
        'demanda': demanda,
        'costos': costos
    }
    
    return solucion_vogel

# Ejecutar el algoritmo
if __name__ == "__main__":
    metodo_vogel()