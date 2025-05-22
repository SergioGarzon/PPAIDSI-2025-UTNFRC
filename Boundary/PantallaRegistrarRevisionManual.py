from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Control.GestorRevManual import GestorRevManual
from datetime import datetime 

class PantallaRegistrarRevisionManual:
    
    def __init__(self):
        self.new_window = Tk() 
        self.table = None  
        self.gestor = None 
        self.windows_properties()

    def windows_properties(self):
        self.new_window.title("Red Sismica")
        self.new_window.geometry("1000x400+500+300")
        #self.new_window.iconbitmap("./Images/utnfrc.ico")
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

        btn_quit = Button(self.new_window, text="Salir del sistema") #, cursor="Hand2")        
        btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))          
        btn_quit.config(command=self.salir_sistema)        

        label_title.pack()
        label_subtitle.pack()  
        self.table.pack(pady=10, fill=BOTH, expand=True)  
        btn_quit.pack(side=LEFT)    

        self.table.bind('<ButtonRelease-1>', self.tomar_seleccion_evento)


    def salir_sistema(self):
        self.new_window.destroy() 

    def habilitarPantalla(self): 
        self.gestor = GestorRevManual()
        self.gestor.nueva_revision_manual()         
        self.eventos_para_mostrar = self.gestor.obtener_eventos_para_mostrar()
        self.mostrar_eventos_sismicos(self.eventos_para_mostrar)        
        self.new_window.mainloop()       

    def mostrar_eventos_sismicos(self, eventos_sismicos_lista):

        for i, evento in enumerate(eventos_sismicos_lista):
            
            fecha_ocurrencia_str = evento.get_fecha_hora_ocurrencia().strftime("%d/%m/%Y")
            hora_ocurrencia_str = evento.get_fecha_hora_ocurrencia().strftime("%H:%M:%S")

            ubicacion_str = f"Lat: {evento.get_latitud_epicentro()} Lon: {evento.get_longitud_epicentro()}"
            magnitud_str = f"{evento.get_valor_magnitud()}°" 

            self.table.insert(parent='', index='end', values=(str(i + 1), fecha_ocurrencia_str, hora_ocurrencia_str, ubicacion_str, magnitud_str, "Seleccionar" ))

    def tomar_seleccion_evento(self, event):
        selected_item = self.table.focus() 
        if selected_item:
            item_values = self.table.item(selected_item, 'values')

            numero_fila = item_values[0]
            fecha_evento_str = item_values[1]
            hora_evento_str = item_values[2]
            ubicacion_str = item_values[3]
            magnitud_str = item_values[4]

            fecha_hora_combinada_str = f"{fecha_evento_str} {hora_evento_str}"

            try:
                fecha_hora_ocurrencia_dt = datetime.strptime(fecha_hora_combinada_str, "%d/%m/%Y %H:%M:%S")
            except ValueError as e:
                fecha_hora_ocurrencia_dt = None 

            latitud_epicentro = ubicacion_str[5:11]
            longitud_epicentro = ubicacion_str[16:23]
            magnitud = magnitud_str[0:3]

            messagebox.showinfo("Información", 
                "Se ha seleccionado "+
                "\nUbicacion latitud epicentro: " +str(latitud_epicentro) +
                "\nUbicacion longitud epicentro: " + str(longitud_epicentro) +
                "\nfecha y hora ocurrencia: "+str(fecha_hora_ocurrencia_dt)+
                "\nMagnitud: " + str(magnitud)
            )
            
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


