from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Control.GestorRevManual import GestorRevManual

class PantallaRegistrarRevisionManual:
    
    def __init__(self):
        self.new_window = Tk() 
        self.table = None  
        self.gestor = None 
        self.windows_properties()    

    def salir_sistema(self):
        self.new_window.destroy() 

    #METODO 2 (Diagrama de secuencia)
    def habilitarPantalla(self): 
        self.gestor = GestorRevManual()
        self.gestor.nueva_revision_manual()         
        self.eventos_para_mostrar = self.gestor.obtener_eventos_para_mostrar()
        self.mostrar_eventos_sismicos(self.eventos_para_mostrar)        
        self.new_window.mainloop()       

    #METODO 7 (Diagrama de secuencia)
    def mostrar_eventos_sismicos(self, eventos_sismicos_lista2):
        for i, evento in enumerate(eventos_sismicos_lista2):            
            self.table.insert(parent='', index='end', values=(str(i + 1), evento[0], evento[1], evento[2], evento[3], "Seleccionar" ))

    #METODO 8 (Diagrama de secuencia)
    def tomar_seleccion_evento(self, event):
        selected_item = self.table.focus() 
        if selected_item:
            item_values = self.table.item(selected_item, 'values')
            messagebox.showinfo("Información", str(item_values))
            self.gestor.tomar_seleccion_evento(item_values)
            
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

    #Las propiedades de la pantalla las ponemos al último
    def windows_properties(self):
        self.new_window.title("Red Sismica")
        self.new_window.geometry("1000x400+500+300")
        self.new_window.iconbitmap("./Images/utnfrc.ico")
        self.new_window.configure(bg="lightblue")
        self.new_window.resizable(False, False)

        label_title = Label(self.new_window, text="Red Sismica")
        label_title.config(fg="darkblue", bg="lightblue", font=("Arial", 25, "italic"))   

        label_subtitle = Label(self.new_window, text="Eventos sismicos detectados sin revisión")
        label_subtitle.config(fg="darkblue", bg="lightblue", font=("Arial", 15, "italic"))     

        style = ttk.Style(self.new_window)
        style.configure("Treeview.Heading", font=(None, 15))

        self.table = ttk.Treeview(self.new_window, columns=('numero', "fecha", "hora", "ubicacion", "magnitud", "seleccione"), show="headings")

        self.table.heading("numero", text="Número")
        self.table.heading("fecha", text="Fecha del evento")
        self.table.heading("hora", text="Hora del evento")
        self.table.heading("ubicacion", text="Ubicación")
        self.table.heading("magnitud", text="Magnitud")
        self.table.heading("seleccione", text="Seleccione") 

        self.table.column("numero", width=80, anchor=CENTER)
        self.table.column("fecha", width=160, anchor=CENTER)
        self.table.column("hora", width=150, anchor=CENTER)
        self.table.column("ubicacion", width=150, anchor=CENTER)
        self.table.column("magnitud", width=120, anchor=CENTER)
        self.table.column("seleccione", width=120, anchor=CENTER)

        btn_quit = Button(self.new_window, text="Salir del sistema", cursor="Hand2")        
        btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))          
        btn_quit.config(command=self.salir_sistema)        

        label_title.pack()
        label_subtitle.pack()  
        self.table.pack(pady=10, fill=BOTH, expand=True)  
        btn_quit.pack(side=LEFT)    

        self.table.bind('<ButtonRelease-1>', self.tomar_seleccion_evento)