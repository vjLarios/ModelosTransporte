from rich.console import Console
from rich.table import Table

from InsertProblem import get_problem_data

def metodo_vogel():
    """
    Algoritmo de Vogel para resolver problemas de transporte
    """
    console = Console()
    
    console.rule("[bold blue]ALGORITMO DE APROXIMACIÓN DE VOGEL[/bold blue]")
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
    
    console.rule("[bold yellow]INICIALIZACIÓN[/bold yellow]")
    
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
        console.rule(f"[bold green]ITERACIÓN {iteracion}[/bold green]")
        
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
        
        # ! Calculamos la penalidad por fila    
        console.print("\n[bold blue]CÁLCULO DE PENALIDADES POR FILA:[/bold blue]")
        penalidades_filas = []
        for i in range(len(oferta)):
            # ? Si la oferta en esta fila ya se ha agotado (es 0 o negativa), no se puede asignar más.
            #   Por lo tanto, no tiene sentido calcular una penalidad → se marca como None.
            if oferta_actual[i] <= 0:
                penalidades_filas.append(None)
                console.print(f"  Fila {i+1}: Sin oferta disponible -> penalidad = N/A")
                continue
            
            # ? Recopilamos los costos de esta fila, pero solo para aquellas columnas (destinos)
            #   que aún tienen demanda pendiente (> 0). Esto asegura que solo consideramos celdas viables.
            costos_disponibles = []
            for j in range(len(demanda)):
                if demanda_actual[j] > 0:
                    costos_disponibles.append(costos[i][j])
            
            # ? Si hay menos de dos destinos disponibles, no se puede calcular una penalidad válida
            #   (porque la penalidad requiere los dos costos más bajos). En este caso, se asigna 0.
            if len(costos_disponibles) < 2:
                penalidades_filas.append(0)
                console.print(f"  Fila {i+1}: Solo hay {len(costos_disponibles)} destino(s) disponible(s) -> penalidad = 0")
            else:
                # ? Ordenamos los costos disponibles de menor a mayor para identificar
                #   los dos más pequeños. Aquí se usa ordenamiento burbuja
                costos_ord = costos_disponibles[:]  # Copia para no alterar la original
                n = len(costos_ord)
                for k in range(n):
                    for l in range(0, n - k - 1):
                        if costos_ord[l] > costos_ord[l + 1]:
                            costos_ord[l], costos_ord[l + 1] = costos_ord[l + 1], costos_ord[l]
                
                # ? La penalidad de Vogel para una fila es la diferencia entre
                #   el segundo menor costo y el menor costo disponibles.
                penalidad = costos_ord[1] - costos_ord[0]
                penalidades_filas.append(penalidad)
                console.print(f"  Fila {i+1}: Costos disponibles: {costos_disponibles}, ordenados: {costos_ord}")
                console.print(f"           Diferencia entre 2 menores: {costos_ord[1]} - {costos_ord[0]} = {penalidad}")
        
        input("Presiona Enter para continuar...")
        
        # ! Calculamos la penalidad por columna
        console.print("\n[bold blue]CÁLCULO DE PENALIDADES POR COLUMNA:[/bold blue]")
        penalidades_columnas = []
        for j in range(len(demanda)):
            # ? Si la demanda en esta columna ya se ha satisfecho por completo (es 0 o negativa),
            #   no se pueden hacer más asignaciones a este destino. Por tanto, su penalidad
            #   no se considera y se marca como None.
            if demanda_actual[j] <= 0:
                penalidades_columnas.append(None)
                console.print(f"  Columna {j+1}: Sin demanda disponible -> penalidad = N/A")
                continue
            
            # ? Recopilamos los costos de esta columna, pero solo para aquellas filas (orígenes)
            #   que aún tienen oferta pendiente (> 0). Esto asegura que solo se consideran
            #   celdas donde aún es posible enviar unidades.
            costos_disponibles = []
            for i in range(len(oferta)):
                if oferta_actual[i] > 0:
                    costos_disponibles.append(costos[i][j])
            
            # ? Si hay menos de dos orígenes disponibles (es decir, menos de dos costos),
            #   no se puede calcular una penalidad válida según el método de Vogel,
            #   porque se necesitan los dos costos más bajos. En ese caso, se asigna 0.
            if len(costos_disponibles) < 2:
                penalidades_columnas.append(0)
                console.print(f"  Columna {j+1}: Solo hay {len(costos_disponibles)} origen(s) disponible(s) -> penalidad = 0")
            else:
                # ? Ordenamos los costos disponibles de menor a mayor para identificar
                #   los dos más pequeños. Se usa bubble sort por motivos didácticos.
                costos_ord = costos_disponibles[:]  # Copia para no modificar la lista original
                n = len(costos_ord)
                for k in range(n):
                    for l in range(0, n - k - 1):
                        if costos_ord[l] > costos_ord[l + 1]:
                            costos_ord[l], costos_ord[l + 1] = costos_ord[l + 1], costos_ord[l]
                
                # ? La penalidad de Vogel para una columna es la diferencia entre
                #   el segundo menor costo y el menor costo entre los orígenes disponibles.
                penalidad = costos_ord[1] - costos_ord[0]
                penalidades_columnas.append(penalidad)
                console.print(f"  Columna {j+1}: Costos disponibles: {costos_disponibles}, ordenados: {costos_ord}")
                console.print(f"           Diferencia entre 2 menores: {costos_ord[1]} - {costos_ord[0]} = {penalidad}")
        
        input("Presiona Enter para continuar...")
        
        # ! Encontrar la penalidad más alta entre todas las filas y columnas
        # ? Primero buscamos la mayor penalidad entre las filas.
        #   Inicializamos con -1 porque las penalidades reales son ≥ 0,
        #   y usamos -1 como valor "menor que cualquier penalidad válida".
        max_pen_fila = -1
        max_idx_fila = -1  # Índice de la fila con mayor penalidad (0-based)
        for idx, pen in enumerate(penalidades_filas):
            # ? Solo consideramos penalidades que no sean None (es decir, filas aún activas).
            #   Comparamos y actualizamos si encontramos una penalidad mayor.
            if pen is not None and pen > max_pen_fila:
                max_pen_fila = pen
                max_idx_fila = idx

        # ? Luego buscamos la mayor penalidad entre las columnas,
        #   con la misma lógica que para las filas.
        max_pen_col = -1
        max_idx_col = -1  # Índice de la columna con mayor penalidad (0-based)
        for idx, pen in enumerate(penalidades_columnas):
            if pen is not None and pen > max_pen_col:
                max_pen_col = pen
                max_idx_col = idx

        # ? Mostramos las penalidades máximas encontradas para fines informativos y depuración.
        #   Si no hay ninguna fila/columna activa, los índices serían -1,
        #   por lo que se muestra "N/A" en lugar del número de fila/columna.
        console.print(f"\n[bold]PENALIDADES CALCULADAS:[/bold]")
        console.print(f"  Penalidad máxima por filas: {max_pen_fila} en fila {max_idx_fila+1 if max_idx_fila >= 0 else 'N/A'}")
        console.print(f"  Penalidad máxima por columnas: {max_pen_col} en columna {max_idx_col+1 if max_idx_col >= 0 else 'N/A'}")
        
        input("Presiona Enter para continuar...")
        
        # ! Determinar si la penalidad más alta corresponde a una fila o a una columna
        # ? Se compara la mayor penalidad de filas contra la de columnas.
        #   En caso de empate (>=), se da prioridad a la FILA.
        if max_pen_fila >= max_pen_col:
            tipo_seleccion = "fila"
            idx_seleccionado = max_idx_fila  # Índice de la fila elegida (0-based)
            console.print(f"\n[bold green]SELECCIÓN: Mayor penalidad es por FILA ({max_pen_fila}) en fila {idx_seleccionado+1}[/bold green]")
            
            # ? Ahora, dentro de esa fila seleccionada, buscamos la celda con el COSTO MÍNIMO
            #   entre los destinos que aún tienen demanda pendiente (> 0).
            #   Inicializamos 'costo_min' con infinito para asegurar que cualquier costo real lo reemplace.
            costo_min = float('inf')
            col_min = -1  # Índice de la columna con costo mínimo (0-based)
            for j in range(len(demanda)):
                # ? Solo consideramos columnas con demanda aún disponible
                if demanda_actual[j] > 0 and costos[idx_seleccionado][j] < costo_min:
                    costo_min = costos[idx_seleccionado][j]
                    col_min = j  # Guardamos la columna del menor costo
            
            console.print(f"  En fila {idx_seleccionado+1}, costo mínimo es {costo_min} en columna {col_min+1}")

        else:
            # ? Si la penalidad más alta está en una columna, entonces trabajamos sobre esa columna.
            tipo_seleccion = "columna"
            idx_seleccionado = max_idx_col  # Este es el índice de la COLUMNA con mayor penalidad
            console.print(f"\n[bold green]SELECCIÓN: Mayor penalidad es por COLUMNA ({max_pen_col}) en columna {idx_seleccionado+1}[/bold green]")
            
            # ? En esta columna seleccionada, buscamos el COSTO MÍNIMO entre los orígenes
            #   que aún tienen oferta disponible (> 0).
            costo_min = float('inf')
            fila_min = -1  # Índice de la fila con costo mínimo en esta columna
            for i in range(len(oferta)):
                if oferta_actual[i] > 0 and costos[i][idx_seleccionado] < costo_min:
                    costo_min = costos[i][idx_seleccionado]
                    fila_min = i  # Guardamos la fila del menor costo
            
            console.print(f"  En columna {idx_seleccionado+1}, costo mínimo es {costo_min} en fila {fila_min+1}")
            
            # ! IMPORTANTE
            # ? Aunque la penalidad vino de una columna, la asignación final siempre se hace
            #   en términos de (fila, columna). Para mantener coherencia con el resto del código
            #   (especialmente con la asignación posterior), actualizamos las variables:
            #   - 'idx_seleccionado' pasa a ser la FILA donde está el costo mínimo.
            #   - 'col_min' pasa a ser la COLUMNA que originalmente tenía la mayor penalidad.
            #   - 'tipo_seleccion' se cambia a "fila" solo para alinear la lógica posterior,
            #     aunque conceptualmente la decisión vino de una columna.
            idx_seleccionado = fila_min
            tipo_seleccion = "fila"  # Ajuste técnico para simplificar la asignación después
            col_min = max_idx_col
        
        input("Presiona Enter para continuar...")
        
        # ! Realizar la asignación en la celda seleccionada (fila, columna)
        # ? La cantidad a asignar está limitada por la menor entre:
        #   - la oferta disponible en el origen (fila)
        #   - la demanda pendiente en el destino (columna)
        #   Esto asegura que no se sobrepase ni la capacidad del origen ni la necesidad del destino.
        cantidad_asignar = min(oferta_actual[idx_seleccionado], demanda_actual[col_min])

        # ? Se acumula la asignación en la matriz de resultados.
        #   Usamos '+=' porque, en teoría, una celda podría recibir más de una asignación
        #   en implementaciones más complejas, aunque en Vogel usualmente se asigna una vez.
        #   Aquí es seguro, pero el operador '+=' garantiza robustez.
        asignaciones[idx_seleccionado][col_min] += cantidad_asignar

        # ? Mostramos al usuario los detalles de esta asignación para transparencia y seguimiento.
        console.print(f"\n[bold yellow]ASIGNACIÓN:[/bold yellow]")
        console.print(f"  Asignando {cantidad_asignar} unidades de O{idx_seleccionado+1} a D{col_min+1}")
        console.print(f"  Costo unitario: {costos[idx_seleccionado][col_min]}")
        console.print(f"  Costo total para esta asignación: {cantidad_asignar} x {costos[idx_seleccionado][col_min]} = {cantidad_asignar * costos[idx_seleccionado][col_min]}")

        # ! Actualizar los saldos restantes de oferta y demanda
        # ? Restamos la cantidad asignada tanto de la oferta del origen
        #   como de la demanda del destino. Al menos uno de los dos quedará en 0,
        #   lo que "saturará" esa fila o columna para iteraciones futuras.
        oferta_actual[idx_seleccionado] -= cantidad_asignar
        demanda_actual[col_min] -= cantidad_asignar

        # ? Mostramos los nuevos saldos para que el usuario vea el progreso del algoritmo.
        console.print(f"  Oferta restante O{idx_seleccionado+1}: {oferta_actual[idx_seleccionado]}")
        console.print(f"  Demanda restante D{col_min+1}: {demanda_actual[col_min]}")
                
        input("Presiona Enter para continuar...")
        
        # ! Mostrar la matriz de asignaciones actualizada después de la asignación reciente
        # ? Esta visualización permite al usuario ver el progreso del algoritmo en cada iteración.
        #   Muestra cuántas unidades se han asignado de cada origen (fila) a cada destino (columna).
        console.print("\n[bold]MATRIZ DE ASIGNACIONES ACTUAL:[/bold]")
        table_asig = Table(show_header=True, header_style="bold magenta")
        table_asig.add_column("Origen", style="dim")  # Primera columna: nombres de los orígenes (O1, O2, ...)

        # ? Agregamos una columna por cada destino (D1, D2, ..., Dn)
        for j in range(len(demanda)):
            table_asig.add_column(f"D{j+1}")

        # ? Llenamos la tabla con los valores actuales de la matriz 'asignaciones'
        for i, fila in enumerate(asignaciones):
            row = [f"O{i+1}"]  # Primera celda de la fila: nombre del origen
            for val in fila:
                # ? Convertimos cada valor numérico a cadena para mostrarlo en la tabla
                row.append(str(val))
            table_asig.add_row(*row)  # Añadimos la fila completa a la tabla

        console.print(table_asig)

        # ! Verificar si la asignación actual saturó completamente una fila, una columna, o ambas
        # ? Cuando la oferta restante de un origen llega a 0, esa fila ya no puede enviar más unidades.
        if oferta_actual[idx_seleccionado] == 0:
            console.print(f"  -> [bold red]Fila {idx_seleccionado+1} ha sido completamente satisfecha[/bold red]")

        # ? Cuando la demanda restante de un destino llega a 0, esa columna ya no necesita más unidades.
        if demanda_actual[col_min] == 0:
            console.print(f"  -> [bold red]Columna {col_min+1} ha sido completamente satisfecha[/bold red]")

        # ? Pausa para que el usuario pueda revisar la salida antes de la siguiente iteración.
        #   Esto mejora la experiencia educativa al permitir seguir el algoritmo paso a paso.
        input("Presiona Enter para continuar...")

        # ? Incrementamos el contador de iteraciones para el próximo ciclo.
        iteracion += 1
    
    # ! Mostrar la solución final del problema de transporte
    # ? Esta sección se ejecuta cuando ya no queda oferta ni demanda por asignar.
    #   Presenta los resultados de forma clara para que el usuario pueda interpretarlos.
    console.rule("[bold blue]SOLUCIÓN FINAL[/bold blue]")

    # ? Mostramos la matriz completa de asignaciones (no solo las celdas activas),
    #   para que se vea la solución en su contexto total, incluyendo ceros donde no hubo envío.
    console.print("Matriz de asignaciones final:")
    table_final = Table(show_header=True, header_style="bold magenta")
    table_final.add_column("Origen", style="dim")  # Primera columna: etiquetas de orígenes

    # ? Agregamos una columna por cada destino (D1, D2, ..., Dn)
    for j in range(len(demanda)):
        table_final.add_column(f"D{j+1}")

    # ? Rellenamos la tabla con todos los valores de la matriz 'asignaciones'
    for i, fila in enumerate(asignaciones):
        row = [f"O{i+1}"]  # Nombre del origen
        for val in fila:
            row.append(str(val))  # Convertimos cada valor a texto
        table_final.add_row(*row)

    console.print(table_final)
    input("Presiona Enter para continuar...")

    # ! Desglose detallado de las asignaciones y cálculo del costo total
    # ? Aquí se listan solo las rutas donde hubo asignación real (> 0),
    #   mostrando cuánto se envió, a qué costo unitario, y el subtotal.
    console.print("\n[bold]Asignaciones detalladas:[/bold]")
    total_costo = 0  # Acumulador para el costo total de transporte
    for i in range(len(oferta)):
        for j in range(len(demanda)):
            if asignaciones[i][j] > 0:
                # ? Calculamos el costo de esta asignación específica: cantidad × costo unitario
                costo_asignacion = asignaciones[i][j] * costos[i][j]
                total_costo += costo_asignacion
                console.print(f"  O{i+1} -> D{j+1}: {asignaciones[i][j]} unidades x {costos[i][j]} = {costo_asignacion}")

    # ? Mostramos el costo total resultante, que es el objetivo principal del método de Vogel
    #   (minimizar el costo total de transporte).
    console.print(f"\n[bold green]COSTO TOTAL DE TRANSPORTE: {total_costo}[/bold green]")
    input("Presiona Enter para continuar...")

    # ! Verificación de balance del problema (oferta = demanda)
    # ? En un problema de transporte balanceado, la suma total de oferta debe ser igual
    #   a la suma total de demanda, y también debe coincidir con la suma de todas las asignaciones.
    #   Esta comprobación ayuda a detectar errores lógicos o malentendidos en los datos.
    console.print("\n[bold]Verificación de oferta y demanda:[/bold]")
    console.print(f"Oferta total original: {sum(oferta)}")
    console.print(f"Demanda total original: {sum(demanda)}")
    console.print(f"Suma de asignaciones: {sum(sum(fila) for fila in asignaciones)}")

    # ? Pausa final antes de terminar, para que el usuario pueda revisar todos los resultados.
    input("Presiona Enter para continuar...")

    # ? Línea decorativa que marca el final del algoritmo.
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