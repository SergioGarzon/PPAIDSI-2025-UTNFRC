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
            
            self.label_subtitle.pack_forget() 
            self.gestor.tomar_seleccion_evento(lista_devolucion)
            self.table.delete(*self.table.get_children())
            self.table.pack_forget() 
            self.btn_quit_2.pack_forget() 
            self.label_selection.pack_forget() 
        
        self.mostrar_datos()
    
    # METODO 46 (Diagrama de secuencia)
    def mostrar_datos(self):

        self.datos_mostrar = self.gestor.obtener_lista_datos_totales()

        self.label_eventsel = Label(self.new_window, text="\nDATOS DEL EVENTO SISMICO SELECCIONADO:")
        self.label_eventsel.config(fg="darkblue", bg="lightblue", font=("Arial", 25, "italic")) 
        self.label_eventsel.place(x = 10 , y = 30)

        self.label_alcance = Label(self.new_window, text="\nAlcance:")
        self.label_alcance.config(fg="black", bg="lightblue", font=("Arial", 15, "italic")) 
        self.label_alcance.place(x = 10 , y = 30)
        
        self.text_box_alcance = Text(self.new_window, width=40, height=2, wrap="word") 
        self.text_box_alcance.config(font=("Arial", 14)) 
        self.text_box_alcance.insert("1.0", self.datos_mostrar[0])
        self.text_box_alcance.config(state="disabled")         

        self.label_clasificacion = Label(self.new_window, text="Clasificacion:")
        self.label_clasificacion.config(fg="black", bg="lightblue", font=("Arial", 15, "italic")) 
        self.label_clasificacion.place(x = 10 , y = 30)

        self.text_box_clasificacion = Text(self.new_window, width=40, height=2, wrap="word") 
        self.text_box_clasificacion.config(font=("Arial", 14)) 
        self.text_box_clasificacion.insert("1.0", self.datos_mostrar[2])
        self.text_box_clasificacion.config(state="disabled")

        self.label_origen_generacion = Label(self.new_window, text="Origen Generación:")
        self.label_origen_generacion.config(fg="black", bg="lightblue", font=("Arial", 15, "italic")) 
        self.label_origen_generacion.place(x = 10 , y = 30)

        self.text_box_origen_generacion = Text(self.new_window, width=40, height=2, wrap="word") 
        self.text_box_origen_generacion.config(font=("Arial", 14)) 
        self.text_box_origen_generacion.insert("1.0", self.datos_mostrar[1])
        self.text_box_origen_generacion.config(state="disabled")

        self.label_magnitud = Label(self.new_window, text="Magnitud:")
        self.label_magnitud.config(fg="black", bg="lightblue", font=("Arial", 15, "italic")) 
        self.label_magnitud.place(x = 10 , y = 30)

        self.text_box_magnitud = Text(self.new_window, width=40, height=2, wrap="word") 
        self.text_box_magnitud.config(font=("Arial", 14)) 
        self.text_box_magnitud.insert("1.0", self.gestor.obtener_lista_evento_seleccionado().get_valor_magnitud())
        self.text_box_magnitud.config(state="disabled")

        if str(platform.system()) == "Windows":
            self.btn_quit_3 = Button(self.new_window, text="Salir del sistema", cursor="Hand2")    
        else:
            self.btn_quit_3 = Button(self.new_window, text="Salir del sistema")

        self.btn_quit_3.config(fg="white", bg="red", font=("Arial", 15, "bold"))          
        self.btn_quit_3.config(command=self.salir_sistema)

        if str(platform.system()) == "Windows":
            self.btn_editar_datos = Button(self.new_window, text="Editar datos", width=15, height=1, cursor="Hand2")    
        else:
            self.btn_editar_datos = Button(self.new_window, text="Editar datos", width=15, height=1)

        self.btn_editar_datos.config(fg="white", bg="blue", font=("Arial", 15, "bold")) 

        if str(platform.system()) == "Windows":
            self.btn_NO_editar_datos = Button(self.new_window, text="NO editar datos", width=15, height=1, cursor="Hand2")    
        else:
            self.btn_NO_editar_datos = Button(self.new_window, text="NO Editar datos", width=15, height=1)

        self.btn_NO_editar_datos.config(fg="white", bg="red", font=("Arial", 15, "bold"))
        self.btn_NO_editar_datos.config(command=self.opcion_no_modificar_datos_evento_sismico)

        self.label_eventsel.pack()
        self.label_alcance.pack()
        self.text_box_alcance.pack(pady=10) 
        self.btn_editar_datos.pack_forget()
        self.btn_NO_editar_datos.pack_forget()
        self.label_clasificacion.pack()
        self.text_box_clasificacion.pack(pady=10)
        self.label_origen_generacion.pack()
        self.text_box_origen_generacion.pack(pady=10)
        self.label_magnitud.pack()
        self.text_box_magnitud.pack(pady=10)
        self.btn_quit.pack(side=LEFT)

        # METODO 47 (Diagrama de secuencia)
        self.habilitar_visualizacion_mapa_eventos()

    # METODO 47 (Diagrama de secuencia)
    def habilitar_visualizacion_mapa_eventos(self):

        self.label_visualizacion_evento = Label(self.new_window, text="¿Desea visualizar el mapa de eventos?")
        self.label_visualizacion_evento.config(fg="black", bg="lightblue", font=("Arial", 15, "italic")) 
        self.label_visualizacion_evento.place(x = 10 , y = 30)

        if str(platform.system()) == "Windows":
            self.btn_visualizacion_evento_si = Button(self.new_window, text="SI", width=10, height=1, cursor="Hand2")    
        else:
            self.btn_visualizacion_evento_si = Button(self.new_window, text="SI", width=10, height=1)

        self.btn_visualizacion_evento_si.config(fg="white", bg="green", font=("Arial", 15, "bold")) 

        if str(platform.system()) == "Windows":
            self.btn_visualizacion_evento_no = Button(self.new_window, text="NO", width=10, height=1, cursor="Hand2")    
        else:
            self.btn_visualizacion_evento_no = Button(self.new_window, text="NO", width=10, height=1)

        self.btn_visualizacion_evento_no.config(fg="white", bg="red", font=("Arial", 15, "bold"))  
         # METODO 47 (Diagrama de secuencia)       
        self.btn_visualizacion_evento_no.config(command=self.opcion_seleccion_no_visualizacion) 

        self.label_visualizacion_evento.pack()
        self.btn_visualizacion_evento_si.pack(side="right", padx=5, pady=10)
        self.btn_visualizacion_evento_no.pack(side="right", padx=5, pady=10)

    # METODO 47 (Diagrama de secuencia)
    def opcion_seleccion_no_visualizacion(self):
        self.btn_visualizacion_evento_si.pack_forget() 
        self.btn_visualizacion_evento_no.pack_forget() 
        self.label_visualizacion_evento.pack_forget() 

        self.label_edicion_datos = Label(self.new_window, text="Puede editar el alcance, origen clasificacion y magnitud")
        self.label_edicion_datos.config(fg="black", bg="lightblue", font=("Arial", 15, "italic")) 
        self.label_edicion_datos.place(x = 10 , y = 30)
        
        self.label_edicion_datos.pack()
        self.btn_editar_datos.pack(side="right", padx=5, pady=10)     
        self.btn_NO_editar_datos.pack(side="right", padx=5, pady=10) 

        # METODO 48 (Diagrama de secuencia)
        self.gestor.tomar_seleccion_no_visualizacion()

        # METODO 49 (Diagrama de secuencia)
        self.habilitar_modificacion_magnitud()
        # METODO 50 (Diagrama de secuencia)
        self.habilitar_modificacion_alcance() 
        # METODO 51 (Diagrama de secuencia)
        self.habilitar_modificacion_origen_generacion() 
        
        #self.text_box_clasificacion.config(state="normal")

    # METODO 49 (Diagrama de secuencia)
    def habilitar_modificacion_magnitud(self):
        self.text_box_magnitud.config(state="normal")

    # METODO 50 (Diagrama de secuencia)
    def habilitar_modificacion_alcance(self):
        self.text_box_alcance.config(state="normal") 

    # METODO 51 (Diagrama de secuencia)
    def habilitar_modificacion_origen_generacion(self):
        self.text_box_origen_generacion.config(state="normal")

    # METODO 52 (Diagrama de secuencia)
    def opcion_no_modificar_datos_evento_sismico(self):
        self.label_edicion_datos.pack_forget()
        self.btn_editar_datos.pack_forget()     
        self.btn_NO_editar_datos.pack_forget() 
        self.text_box_alcance.delete("1.0", END)
        self.text_box_clasificacion.delete("1.0", END)
        self.text_box_origen_generacion.delete("1.0", END)    
        self.text_box_magnitud.delete("1.0", END)
        self.text_box_alcance.insert("1.0", self.datos_mostrar[0])
        self.text_box_clasificacion.insert("1.0", self.datos_mostrar[2])
        self.text_box_origen_generacion.insert("1.0", self.datos_mostrar[1])
        self.text_box_magnitud.insert("1.0", self.gestor.obtener_lista_evento_seleccionado().get_valor_magnitud())
        self.text_box_magnitud.config(state="disabled")
        self.text_box_alcance.config(state="disabled") 
        self.text_box_origen_generacion.config(state="disabled")

        # METODO 53 (Diagrama de secuencia)
        self.gestor.tomar_opcion_no_modificar_datos_evento_sismico()

        # METODO 54 (Diagrama de secuencia)
        self.mostrar_opciones_eventos()
    
    # METODO 54 (Diagrama de secuencia)
    def mostrar_opciones_eventos(self):

        if str(platform.system()) == "Windows":
            self.btn_confirmar_evento = Button(self.new_window, text="Confirmar evento", width=20, height=1, cursor="Hand2")    
        else:
            self.btn_confirmar_evento = Button(self.new_window, text="Confirmar evento", width=20, height=1)

        self.btn_confirmar_evento.config(fg="white", bg="springgreen", font=("Arial", 15, "bold"))  

        if str(platform.system()) == "Windows":
            self.btn_rechazar_evento = Button(self.new_window, text="Rechazar evento", width=20, height=1, cursor="Hand2")    
        else:
            self.btn_rechazar_evento = Button(self.new_window, text="Rechazar evento", width=20, height=1)

        self.btn_rechazar_evento.config(fg="white", bg="orange", font=("Arial", 15, "bold"))
        # METODO 55 (Diagrama de secuencia)  
        self.btn_rechazar_evento.config(command=self.opcion_rechazar_evento)

        if str(platform.system()) == "Windows":
            self.btn_solicitar_revision_experto = Button(self.new_window, text="Solicitar revision experto", width=20, height=1, cursor="Hand2")    
        else:
            self.btn_solicitar_revision_experto = Button(self.new_window, text="Solicitar revision experto", width=20, height=1)

        self.btn_solicitar_revision_experto.config(fg="white", bg="dodgerblue2", font=("Arial", 15, "bold"))

        self.btn_confirmar_evento.pack(side="right", padx=5, pady=10)
        self.btn_rechazar_evento.pack(side="right", padx=5, pady=10)
        self.btn_solicitar_revision_experto.pack(side="right", padx=5, pady=10)
        
    # METODO 55 (Diagrama de secuencia)
    def opcion_rechazar_evento(self):
        self.btn_confirmar_evento.pack_forget()
        self.btn_rechazar_evento.pack_forget()
        self.btn_solicitar_revision_experto.pack_forget()

        magnitud_valor_extraido = self.text_box_magnitud.get("1.0", "end-1c") 
        alcance_valor_extraido = self.text_box_alcance.get("1.0", "end-1c") 
        origeneracion_valor_extraido = self.text_box_origen_generacion.get("1.0", "end-1c")
        clasificacion_valor_extraido = self.text_box_clasificacion.get("1.0", "end-1c")
        opcion_elegida = True

        # METODO 56 (Diagrama de secuencia)
        self.gestor.tomar_opcion_seleccionada_rechazar_evento(magnitud_valor_extraido, alcance_valor_extraido,
                                                              origeneracion_valor_extraido, clasificacion_valor_extraido,
                                                              opcion_elegida)
        
        self.label_alcance.pack_forget()
        self.label_eventsel.pack_forget()
        self.label_clasificacion.pack_forget()
        self.label_edicion_datos.pack_forget()
        self.label_magnitud.pack_forget()
        self.label_origen_generacion.pack_forget()
        self.text_box_alcance.pack_forget()
        self.text_box_clasificacion.pack_forget()
        self.text_box_magnitud.pack_forget()
        self.text_box_origen_generacion.pack_forget()
        self.btn_solicitar_revision_experto.pack_forget()
        self.btn_rechazar_evento.pack_forget()
        self.btn_confirmar_evento.pack_forget()
        self.label_agredecimiento.pack()


    ############################################################
    ##### METODOS PROPIEDADES VENTANA###########################
    ############################################################

    def windows_properties(self):
        self.new_window.title("Red Sismica")
        self.new_window.geometry("1100x680+500+300")

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

        self.label_agredecimiento = Label(self.new_window, text="GRACIAS POR HABER \nUTILIZANDO NUESTRO SISTEMA")
        self.label_agredecimiento.config(fg="darkblue", bg="lightblue", font=("Arial", 35, "italic")) 

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
        self.label_agredecimiento.pack_forget()     
        self.btn_quit.pack(side=LEFT)
        # METODO 17 (Diagrama de secuencia)
        self.table.bind('<ButtonRelease-1>', self.tomar_seleccion_evento)

    def salir_sistema(self):      
        self.new_window.quit()
        self.new_window.destroy()
    