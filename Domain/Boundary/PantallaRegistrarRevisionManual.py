from tkinter import *
from tkinter import ttk
from datetime import datetime
from Domain.Control.GestorRevManual import GestorRevManual
import platform

class PantallaRegistrarRevisionManual:
    
    def __init__(self):
        self.new_window = Tk() 
        self.windows_properties() 
        self.gestor = None          

    #METODO 1 (Diagrama de secuencia)
    def opcion_reg_rev_manual(self):
        self.btn_enter.pack_forget()
        self.btn_quit.pack_forget() 
        self.label_subtitle.pack()
        self.table.pack(pady=10, fill=BOTH, expand=True)
        self.label_selection.pack()
        self.btn_quit_2.pack(side=LEFT)  
        self.habilitar_pantalla()

    #METODO 2 (Diagrama de secuencia)
    def habilitar_pantalla(self): 
        self.gestor = GestorRevManual()
        self.gestor.nueva_rev_manual()  
        self.eventos_para_mostrar = self.gestor.obtener_eventos_para_mostrar()    
        self.mostrar_eventos_sismicos(self.eventos_para_mostrar)        
        self.new_window.mainloop()       

    # METODO 16 (Diagrama de secuencia) 
    def mostrar_eventos_sismicos(self, eventos_sismicos_lista2):
        
        for i, evento in enumerate(eventos_sismicos_lista2):

            fecha_ocurrencia_str = evento[0].strftime("%d/%m/%Y")
            hora_ocurrencia_str = evento[0].strftime("%H:%M:%S")
            epicentro_str = f"Latitud: {evento[2]} Longitud: {evento[4]}"
            hipocentro_str = f"Latitud: {evento[3]} Longitud: {evento[5]}"
            magnitud_str = f"{evento[6]}°"

            self.table.insert(parent='', index='end', values=(str(i + 1), fecha_ocurrencia_str, hora_ocurrencia_str, epicentro_str, hipocentro_str, magnitud_str, "Seleccionar"))
            
    # METODO 17 (Diagrama de secuencia)
    def tomar_seleccion_evento(self, event):
        selected_item = self.table.focus() 
        if selected_item:
            item_values = self.table.item(selected_item, 'values')     
                 
            fecha_evento_str = item_values[1]
            hora_evento_str = item_values[2]
            ubicacion_epicentro_str = str(item_values[3])
            ubicacion_hipocentro_str = str(item_values[4])
            magnitud_str = item_values[5]   

            fecha_hora_combinada_str = f"{fecha_evento_str} {hora_evento_str}"

            try:
                fecha_hora_ocurrencia_dt = datetime.strptime(fecha_hora_combinada_str, "%d/%m/%Y %H:%M:%S")
            except ValueError as e:
                fecha_hora_ocurrencia_dt = None        

            cadena = ubicacion_epicentro_str
            posicion = 0
            lista_espacio = []

            while True:
                posicion = cadena.find(" ", posicion)
                if posicion == -1:
                    break 
                lista_espacio.append(posicion)
                posicion += 1  

            cadena_2 = ubicacion_hipocentro_str
            posicion_2 = 0
            lista_espacio_2 = []

            while True:
                posicion_2 = cadena_2.find(" ", posicion_2)
                if posicion_2 == -1:
                    break 
                lista_espacio_2.append(posicion_2)
                posicion_2 += 1  
        
            latitud_epicentro = float(ubicacion_epicentro_str[lista_espacio[0]:lista_espacio[1]])
            longitud_epicentro = float(ubicacion_epicentro_str[lista_espacio[2]:len(ubicacion_epicentro_str)])
            latitud_hipocentro = float(ubicacion_hipocentro_str[lista_espacio_2[0]:lista_espacio_2[1]])
            longitud_hipocentro = float(ubicacion_hipocentro_str[lista_espacio_2[2]:len(ubicacion_hipocentro_str)])
            magnitud = float(magnitud_str[:-1])

            lista_devolucion = [fecha_hora_ocurrencia_dt, latitud_epicentro, latitud_hipocentro, longitud_epicentro, longitud_hipocentro, magnitud]
            
            self.gestor.tomar_seleccion_evento(lista_devolucion)
            self.table.delete(*self.table.get_children())
            self.table.pack_forget()
            self.label_selection.pack_forget()

    '''   
    def habilitar_visualizacion_mapa_eventos():
        pass

    def opcion_seleccion_no_visualizacion():
        pass

    def habilitar_modificacion_magnitud():
        pass

    def habilitar_modificacion_alcance():
        pass

    def habilitar_modificacion_origen_generacion():
        pass

    def opcion_no_modificar_datos_evento_sismico():
        pass

    '''

    ############################################################
    ##### METODOS PROPIEDADES VENTANA###########################
    ############################################################

    def windows_properties(self):
        self.new_window.title("Red Sismica")
        self.new_window.geometry("1100x500+500+300")

        if str(platform.system()) == "Windows":
            self.new_window.iconbitmap("./Resources/Images/utnfrc.ico")

        self.new_window.configure(bg="lightblue")
        self.new_window.resizable(False, False)

        if str(platform.system()) == "Windows":
            self.btn_enter = Button(self.new_window, text="Registrar resultado revisión manual", cursor="Hand2")
        else:
            self.btn_enter = Button(self.new_window, text="Registrar resultado revisión manual")

        self.btn_enter.config(fg="white", bg="darkgreen", font=("Arial", 15, "bold"))
        self.btn_enter.config(command=self.opcion_reg_rev_manual)

        label_title = Label(self.new_window, text="Red Sismica")
        label_title.config(fg="darkblue", bg="lightblue", font=("Arial", 25, "italic"))   

        self.label_subtitle = Label(self.new_window, text="Eventos sismicos detectados sin revisión")
        self.label_subtitle.config(fg="darkblue", bg="lightblue", font=("Arial", 15, "italic"))     

        style = ttk.Style(self.new_window)
        style.configure("Treeview.Heading", font=(None, 15))

        self.table = ttk.Treeview(self.new_window, columns=('numero', "fecha", "hora", "ubicacion_epicentro", "ubicacion_hipocentro", "magnitud", "seleccione"), show="headings")

        self.table.heading("numero", text="Número")
        self.table.heading("fecha", text="Fecha del evento")
        self.table.heading("hora", text="Hora del evento")
        self.table.heading("ubicacion_epicentro", text="Ubicación Epicentro")
        self.table.heading("ubicacion_hipocentro", text="Ubicación Hipocentro")
        self.table.heading("magnitud", text="Magnitud")
        self.table.heading("seleccione", text="Seleccione") 

        self.table.column("numero", width=80, anchor=CENTER)
        self.table.column("fecha", width=160, anchor=CENTER)
        self.table.column("hora", width=150, anchor=CENTER)
        self.table.column("ubicacion_epicentro", width=200, anchor=CENTER)
        self.table.column("ubicacion_hipocentro", width=200, anchor=CENTER)
        self.table.column("magnitud", width=120, anchor=CENTER)
        self.table.column("seleccione", width=120, anchor=CENTER)

        self.label_selection = Label(self.new_window, text=">>>Debe seleccionar un evento de la lista<<<")
        self.label_selection.config(fg="darkred", bg="lightblue", font=("Arial", 15, "bold"))

        if str(platform.system()) == "Windows":
            self.btn_quit = Button(self.new_window, text="Salir del sistema", cursor="Hand2")  
        else:
            self.btn_quit = Button(self.new_window, text="Salir del sistema")

        self.btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))          
        self.btn_quit.config(command=self.salir_sistema)
        
        if str(platform.system()) == "Windows":
            self.btn_quit_2 = Button(self.new_window, text="Salir del sistema", cursor="Hand2")    
        else:
            self.btn_quit_2 = Button(self.new_window, text="Salir del sistema")

        self.btn_quit_2.config(fg="white", bg="red", font=("Arial", 15, "bold"))          
        self.btn_quit_2.config(command=self.salir_sistema)
        
        label_title.pack()          
        self.btn_enter.pack()        
        self.btn_quit.pack(side=LEFT)
        self.table.bind('<ButtonRelease-1>', self.tomar_seleccion_evento)

    def salir_sistema(self):      
        self.new_window.quit()
        self.new_window.destroy()