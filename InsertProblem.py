import dearpygui.dearpygui as dpg

class InsertProblem:
    def __init__(self):
        self.oferta = [0.0, 0.0, 0.0]
        self.demanda = [0.0, 0.0, 0.0]
        self.costos = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        self.rows = 3
        self.cols = 3
        self.entries = {}
        self.result_data = None
        
        # Inicializar Dear PyGui con tema claro
        dpg.create_context()
        
        # Crear un tema personalizado con apariencia clara y moderna
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 15, 15)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 6)
                dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 6, 4)
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 8)
                dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 6, 4)
                dpg.add_theme_style(dpg.mvStyleVar_IndentSpacing, 20)
                dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 15)
                dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 10)
                
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (245, 245, 245, 255))
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (245, 245, 245, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 100))
                dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (200, 200, 200, 50))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (230, 240, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (210, 230, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (250, 250, 250, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (240, 240, 240, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (200, 200, 200, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (180, 180, 180, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (160, 160, 160, 255))
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (70, 130, 230, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (70, 130, 230, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (50, 110, 210, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 130, 230, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (80, 140, 240, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (60, 120, 220, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Header, (240, 240, 240, 255))
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (230, 230, 230, 255))
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (220, 220, 220, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Separator, (200, 200, 200, 100))
                dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, (200, 200, 200, 150))
                dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, (200, 200, 200, 200))
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (200, 200, 200, 50))
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (200, 200, 200, 100))
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (200, 200, 200, 150))
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (240, 240, 240, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (230, 230, 230, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, (245, 245, 245, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (250, 250, 250, 255))
                
                dpg.add_theme_color(dpg.mvThemeCol_Text, (40, 40, 40, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (120, 120, 120, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (70, 130, 230, 100))
                
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 8)
                dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 6)
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 6)
                dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 6)
                dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 6)
        
        dpg.bind_theme(global_theme)
        
        # Configurar viewport
        dpg.create_viewport(title='Inserción de Problema de Transporte', width=1000, height=700)
        dpg.setup_dearpygui()
        
        self.setup_ui()
    
    def setup_ui(self):
        with dpg.window(label="Problema de Transporte", width=980, height=680, no_resize=True):
            # Encabezado con título e información
            with dpg.group(horizontal=False):
                dpg.add_text("PROBLEMA DE TRANSPORTE", color=(70, 130, 230, 255))
                dpg.add_text("Método de Aproximación de Vogel", color=(100, 100, 100, 255))
                dpg.add_spacer(height=15)
                
                # Información de uso - aplicar tema claro
                info_container = dpg.add_child_window(height=60, border=False, 
                                                    horizontal_scrollbar=False)
                info_text = "Ingresa los datos del problema de transporte. Puedes agregar filas (orígenes) y columnas (destinos) según necesites. Todos los campos deben estar completos para continuar."
                dpg.add_text(info_text, wrap=900, color=(80, 80, 80, 255), parent=info_container)
                
                # Aplicar tema claro al contenedor de información
                with dpg.theme() as info_theme:
                    with dpg.theme_component(dpg.mvChildWindow):
                        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (245, 245, 245, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 100))
                dpg.bind_item_theme(info_container, info_theme)
            
            # Botones principales
            with dpg.group(horizontal=True):
                self.add_row_btn = dpg.add_button(label="➕ Agregar Fila (Origen)", 
                                                callback=self.add_row, 
                                                width=200, height=40)
                self.add_col_btn = dpg.add_button(label="➕ Agregar Columna (Destino)", 
                                                callback=self.add_column, 
                                                width=200, height=40)
                dpg.add_spacer(width=20)
                
                # Contador de dimensiones
                self.size_label = dpg.add_text(f"Tamaño actual: {self.rows}×{self.cols}", 
                                             color=(100, 100, 100, 255))
            
            dpg.add_spacer(height=15)
            
            # Contenedor principal de la tabla - aplicar tema claro
            self.main_table_container = dpg.add_child_window(height=450, border=True)
            
            # Aplicar tema claro al contenedor de la tabla
            with dpg.theme() as table_container_theme:
                with dpg.theme_component(dpg.mvChildWindow):
                    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (245, 245, 245, 255))
                    dpg.add_theme_color(dpg.mvThemeCol_Border, (200, 200, 200, 100))
            dpg.bind_item_theme(self.main_table_container, table_container_theme)
                
            # Título de la tabla
            dpg.add_text("MATRIZ DE COSTOS Y RECURSOS", 
                       color=(70, 130, 230, 255), 
                       parent=self.main_table_container,
                       indent=10)
            dpg.add_spacer(height=5, parent=self.main_table_container)
            
            # Tabla principal
            self.table_container = dpg.add_table(header_row=True, 
                                               borders_innerH=True, 
                                               borders_outerH=True, 
                                               borders_innerV=True, 
                                               borders_outerV=True,
                                               resizable=True,
                                               row_background=True,
                                               policy=dpg.mvTable_SizingStretchProp,
                                               parent=self.main_table_container)
            
            # Definir el ancho inicial de las columnas
            col_widths = [80] + [100] * (self.cols + 1)
            
            for i, width in enumerate(col_widths):
                if i == 0:
                    dpg.add_table_column(label="", width_fixed=True, init_width_or_weight=width, parent=self.table_container)
                elif i <= self.cols:
                    dpg.add_table_column(label=f"D{i}", width_fixed=True, init_width_or_weight=width, parent=self.table_container)
                else:
                    dpg.add_table_column(label="OFERTA", width_fixed=True, init_width_or_weight=width, parent=self.table_container)
            
            self.create_table_rows()
            
            # Mensaje de estado
            self.status_label = dpg.add_text("", 
                                           color=(150, 100, 0, 255), 
                                           indent=10)
            
            # Botón final
            dpg.add_spacer(height=15)
            self.finish_button = dpg.add_button(label="✅ Finalizar y Obtener Datos", 
                                              callback=self.finish, 
                                              width=250, 
                                              height=50,
                                              enabled=False)
            
            # Aplicar estilo al botón final
            with dpg.theme() as finish_theme:
                with dpg.theme_component(dpg.mvButton):
                    dpg.add_theme_color(dpg.mvThemeCol_Button, (76, 175, 80, 255))
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (60, 150, 65, 255))
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (40, 130, 45, 255))
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.bind_item_theme(self.finish_button, finish_theme)
        
        # Inicializar el estado de los botones
        self.update_button_states()
    
    def update_button_states(self):
        """Actualizar el estado de los botones de agregar fila/columna"""
        # Deshabilitar botón de agregar fila si se alcanzó el límite
        dpg.configure_item(self.add_row_btn, 
                         enabled=(self.rows < 6),
                         label="➕ Agregar Fila (Origen)" if self.rows < 6 else f"✅ Máximo de filas ({self.rows}/6)")
        
        # Deshabilitar botón de agregar columna si se alcanzó el límite
        dpg.configure_item(self.add_col_btn, 
                         enabled=(self.cols < 6),
                         label="➕ Agregar Columna (Destino)" if self.cols < 6 else f"✅ Máximo de columnas ({self.cols}/6)")
    
    def create_table_rows(self):
        """Crear las filas de la tabla"""
        # Limpiar filas anteriores si existen
        table_children = dpg.get_item_children(self.table_container, 1)
        if len(table_children) > 1:  # Hay más de una columna definida
            for child in table_children[1:]:  # Saltar la primera que es la definición de columnas
                dpg.delete_item(child)
        
        # Filas de orígenes
        for i in range(self.rows):
            with dpg.table_row(parent=self.table_container):
                # Celda de etiqueta de origen
                with dpg.table_cell():
                    dpg.add_text(f"O{i+1}", color=(40, 40, 40, 255), 
                               indent=30)
                
                # Celdas de costos
                for j in range(self.cols):
                    value = self.costos[i][j] if i < len(self.costos) and j < len(self.costos[i]) else 0.0
                    tag = f"cost_{i}_{j}"
                    input_widget = dpg.add_input_text(default_value=str(value), 
                                                     tag=tag, 
                                                     callback=self.on_value_change,
                                                     width=-1,
                                                     no_spaces=True,
                                                     decimal=True)
                    # Aplicar tema claro al input
                    with dpg.theme() as input_theme:
                        with dpg.theme_component(dpg.mvInputText):
                            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 255))
                            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (230, 240, 255, 255))
                            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (210, 230, 255, 255))
                            dpg.add_theme_color(dpg.mvThemeCol_Text, (40, 40, 40, 255))
                            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                    dpg.bind_item_theme(input_widget, input_theme)
                    
                    self.entries[tag] = (i, j, "costo")
                
                # Celda de oferta
                value = self.oferta[i] if i < len(self.oferta) else 0.0
                tag = f"oferta_{i}"
                input_widget = dpg.add_input_text(default_value=str(value), 
                                                 tag=tag, 
                                                 callback=self.on_value_change,
                                                 width=-1,
                                                 no_spaces=True,
                                                 decimal=True)
                # Aplicar tema claro al input
                with dpg.theme() as input_theme:
                    with dpg.theme_component(dpg.mvInputText):
                        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (230, 240, 255, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (210, 230, 255, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_Text, (40, 40, 40, 255))
                        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                dpg.bind_item_theme(input_widget, input_theme)
                
                self.entries[tag] = (i, -1, "oferta")
        
        # Fila de demandas
        with dpg.table_row(parent=self.table_container):
            # Celda de etiqueta de demanda
            with dpg.table_cell():
                dpg.add_text("DEMANDA", color=(40, 40, 40, 255), 
                           indent=10)
            
            # Celdas de demandas
            for j in range(self.cols):
                value = self.demanda[j] if j < len(self.demanda) else 0.0
                tag = f"demand_{j}"
                input_widget = dpg.add_input_text(default_value=str(value), 
                                                 tag=tag, 
                                                 callback=self.on_value_change,
                                                 width=-1,
                                                 no_spaces=True,
                                                 decimal=True)
                # Aplicar tema claro al input
                with dpg.theme() as input_theme:
                    with dpg.theme_component(dpg.mvInputText):
                        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (230, 240, 255, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (210, 230, 255, 255))
                        dpg.add_theme_color(dpg.mvThemeCol_Text, (40, 40, 40, 255))
                        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                dpg.bind_item_theme(input_widget, input_theme)
                
                self.entries[tag] = (-1, j, "demanda")
            
            # Celda vacía en la esquina inferior derecha
            with dpg.table_cell():
                pass
    
    def on_value_change(self, sender, app_data):
        """Callback cuando cambia un valor en la tabla"""
        if sender in self.entries:
            i, j, tipo = self.entries[sender]
            try:
                value = float(app_data)
                if tipo == "costo":
                    if i < len(self.costos) and j < len(self.costos[i]):
                        self.costos[i][j] = value
                elif tipo == "oferta":
                    if i < len(self.oferta):
                        self.oferta[i] = value
                elif tipo == "demanda":
                    if j < len(self.demanda):
                        self.demanda[j] = value
            except ValueError:
                pass
            
            # Verificar si todas las casillas están llenas
            self.check_all_filled()
    
    def add_row(self):
        """Agregar una nueva fila (origen)"""
        # Verificar límite antes de agregar
        if self.rows >= 6:
            return  # No hacer nada si ya se alcanzó el límite
        
        # Guardar datos actuales
        self.save_current_data()
        
        # Aumentar número de filas
        self.rows += 1
        
        # Agregar fila vacía a oferta
        self.oferta.append(0.0)
        
        # Agregar fila vacía a costos
        new_cost_row = [0.0] * self.cols
        self.costos.append(new_cost_row)
        
        # Recrear la tabla completa
        self.recreate_table()
        
        # Actualizar estado de los botones
        self.update_button_states()
    
    def add_column(self):
        """Agregar una nueva columna (destino)"""
        # Verificar límite antes de agregar
        if self.cols >= 6:
            return  # No hacer nada si ya se alcanzó el límite
        
        # Guardar datos actuales
        self.save_current_data()
        
        # Aumentar número de columnas
        self.cols += 1
        
        # Agregar columna vacía a demanda
        self.demanda.append(0.0)
        
        # Agregar columna a costos
        for i in range(len(self.costos)):
            if len(self.costos[i]) < self.cols:
                self.costos[i].append(0.0)
        
        # Asegurarse de que la matriz tenga las dimensiones correctas
        if len(self.costos) < self.rows:
            while len(self.costos) < self.rows:
                self.costos.append([0.0] * self.cols)
        
        # Recrear la tabla completa
        self.recreate_table()
        
        # Actualizar estado de los botones
        self.update_button_states()
    
    def recreate_table(self):
        """Recrear la tabla completa con nuevas dimensiones"""
        # Eliminar la tabla existente
        dpg.delete_item(self.table_container)
        
        # Crear nueva tabla con nuevas columnas
        self.table_container = dpg.add_table(header_row=True, 
                                           borders_innerH=True, 
                                           borders_outerH=True, 
                                           borders_innerV=True, 
                                           borders_outerV=True,
                                           resizable=True,
                                           row_background=True,
                                           policy=dpg.mvTable_SizingStretchProp,
                                           parent=self.main_table_container)
        
        # Definir el ancho inicial de las columnas
        col_widths = [80] + [100] * (self.cols + 1)
        
        for i, width in enumerate(col_widths):
            if i == 0:
                dpg.add_table_column(label="", width_fixed=True, init_width_or_weight=width, parent=self.table_container)
            elif i <= self.cols:
                dpg.add_table_column(label=f"D{i}", width_fixed=True, init_width_or_weight=width, parent=self.table_container)
            else:
                dpg.add_table_column(label="OFERTA", width_fixed=True, init_width_or_weight=width, parent=self.table_container)
        
        self.create_table_rows()
        
        # Actualizar contador de tamaño
        dpg.set_value(self.size_label, f"Tamaño actual: {self.rows}×{self.cols}")
        
        # Verificar estado de llenado
        self.check_all_filled()
        
        # Actualizar mensaje de estado
        dpg.set_value(self.status_label, f"Tabla actualizada a {self.rows} filas × {self.cols} columnas")
    
    def save_current_data(self):
        """Guardar los datos actuales de las entradas"""
        for sender, (i, j, tipo) in self.entries.items():
            try:
                value_str = dpg.get_value(sender)
                if value_str and self.is_number(value_str):
                    value = float(value_str)
                    if tipo == "costo":
                        if i < len(self.costos) and j < len(self.costos[i]):
                            self.costos[i][j] = value
                    elif tipo == "oferta":
                        if i < len(self.oferta):
                            self.oferta[i] = value
                    elif tipo == "demanda":
                        if j < len(self.demanda):
                            self.demanda[j] = value
            except:
                pass
    
    def is_number(self, value):
        """Verificar si un valor es numérico"""
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def check_all_filled(self):
        """Verificar si todas las casillas están llenas"""
        all_filled = True
        
        # Verificar costos y ofertas
        for i in range(self.rows):
            for j in range(self.cols):
                tag = f"cost_{i}_{j}"
                if tag in self.entries:
                    value = dpg.get_value(tag)
                    if not value or not self.is_number(value):
                        all_filled = False
                        break
            if not all_filled:
                break
                
            tag = f"oferta_{i}"
            if tag in self.entries:
                value = dpg.get_value(tag)
                if not value or not self.is_number(value):
                    all_filled = False
                    break
        
        # Verificar demandas
        if all_filled:
            for j in range(self.cols):
                tag = f"demand_{j}"
                if tag in self.entries:
                    value = dpg.get_value(tag)
                    if not value or not self.is_number(value):
                        all_filled = False
                        break
        
        # Actualizar estado del botón y mensaje
        dpg.configure_item(self.finish_button, enabled=all_filled)
        
        if all_filled:
            dpg.set_value(self.status_label, "✓ Todos los datos completos. Puedes finalizar.")
        else:
            dpg.set_value(self.status_label, "⚠ Completa todas las casillas para continuar.")
    
    def finish(self):
        """Finalizar y obtener los datos"""
        # Recoger todos los datos finales
        self.oferta = []
        self.demanda = []
        self.costos = []
        
        # Recoger costos y ofertas
        for i in range(self.rows):
            fila_costos = []
            for j in range(self.cols):
                tag = f"cost_{i}_{j}"
                value = dpg.get_value(tag)
                fila_costos.append(float(value) if self.is_number(value) else 0.0)
            self.costos.append(fila_costos)
            
            tag = f"oferta_{i}"
            value = dpg.get_value(tag)
            self.oferta.append(float(value) if self.is_number(value) else 0.0)
        
        # Recoger demandas
        for j in range(self.cols):
            tag = f"demand_{j}"
            value = dpg.get_value(tag)
            self.demanda.append(float(value) if self.is_number(value) else 0.0)
        
        # Guardar resultado
        self.result_data = {
            'oferta': self.oferta,
            'demanda': self.demanda,
            'costos': self.costos
        }
        
        # Mostrar mensaje de éxito
        dpg.set_value(self.status_label, "✓ Datos guardados correctamente. Cerrando...")
        
        # Cerrar después de un breve retraso
        dpg.stop_dearpygui()
    
    def get_data(self):
        """Ejecutar la interfaz y retornar los datos"""
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
        
        return self.result_data

def get_problem_data():
    app = InsertProblem()
    return app.get_data()

if __name__ == "__main__":
    data = get_problem_data()
    print("Datos obtenidos:")
    print(f"Oferta: {data['oferta']}")
    print(f"Demanda: {data['demanda']}")
    print(f"Costos: {data['costos']}")