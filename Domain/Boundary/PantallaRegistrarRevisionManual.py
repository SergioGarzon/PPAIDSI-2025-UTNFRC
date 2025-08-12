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
        #METODO 3 (Diagrama de secuencia), hace la instancia de la clase que contiene el metodo
        self.gestor = GestorRevManual()
        #METODO 3 (Diagrama de secuencia), aqui es donde invoca al metodo 3
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
        
        # METODO 17 (Diagrama de secuencia)
        #self.table.bind('<ButtonRelease-1>', self.tomar_seleccion_evento)

    def salir_sistema(self):      
        self.new_window.quit()
        self.new_window.destroy()
    