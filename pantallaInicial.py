import tkinter as tk
from PIL import ImageTk, Image
from Boundary.PantallaRegistrarRevisionManual import PantallaRegistrarRevisionManual

class PantallaInicial():

    def __init__(self):
        self.windows1 = tk.Tk()
        self.windows_properties()
        self.windows_components()

    def windows_properties(self):
        self.windows1.title("Red Sismica")
        self.windows1.geometry("750x700+250+100")
        #self.windows1.iconbitmap("./Images/utnfrc.ico")
        self.windows1.configure(bg="lightblue")
        self.windows1.resizable(False, False)

    def windows_components(self):
        frame1 = tk.Frame(self.windows1)   
        frame1.configure(bg="lightblue")    

        label_name = tk.Label(frame1, text="Red Sismica")
        label_name.config(fg="darkblue", bg="lightblue", font=("Arial", 25, "italic"))    

        label_subject = tk.Label(frame1, text="Diseño de sistemas de información")
        label_subject.config(fg="black", bg="lightblue", font=("Arial", 15, "bold"))        

        label_group = tk.Label(frame1, text="Grupo 11. CU: 23 Registrar resultado de revisión manual")
        label_group.config(fg="black", bg="lightblue", font=("Arial", 15, "bold"))      

        label_members = tk.Label(frame1, text="Integrantes: de Llamas Agustin, Garzon Sergio, Ibañez Ignacio, Masino Nicolas")
        label_members.config(fg="black", bg="lightblue", font=("Arial", 15)) 

        label_members2 = tk.Label(frame1, text="Mezzopeva Juan Cruz, Piazza Gonzalo, Roth Max, Tarraga Ezequiel, Vaca Adriel")
        label_members2.config(fg="black", bg="lightblue", font=("Arial", 15)) 

        image_open = Image.open("./Images/ImageRedSismica.png")
        image_open = ImageTk.PhotoImage(image_open)

        image_label = tk.Label(frame1, image=image_open)
        image_label.image = image_open    

        btn_enter = tk.Button(frame1, text="Registrar resultado revisión manual") #, cursor="Hand2")
        btn_enter.config(fg="white", bg="darkgreen", font=("Arial", 15, "bold"))
        btn_enter.config(command=self.opcion_registrar_resultado_revision_manual)

        btn_quit = tk.Button(frame1, text="Salir del sistema") #, cursor="Hand2")
        btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))  
        btn_quit.config(command=self.salir_sistema)

        frame1.pack()
        label_name.pack() 
        label_subject.pack() 
        label_group.pack()
        label_members.pack()
        label_members2.pack()
        image_label.pack(pady=45)  
        btn_quit.pack(side="left")    
        btn_enter.pack(side="right")


    def salir_sistema(self):
        self.windows1.destroy()

    def opcion_registrar_resultado_revision_manual(self):
        self.windows1.destroy()
        self.pantallaRegistrarRevisionManual = PantallaRegistrarRevisionManual()
        self.pantallaRegistrarRevisionManual.habilitarPantalla()
    

    # --- Ejemplo de uso ---
if __name__ == "__main__":
    app_inicial = PantallaInicial()
    app_inicial.windows1.mainloop()