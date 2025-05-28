import tkinter as tk
import platform
from PIL import ImageTk, Image
from Domain.Boundary.PantallaRegistrarRevisionManual import PantallaRegistrarRevisionManual
from Utils.pantallaIntegrantes import PantallaIntegrantes

class PantallaInicial():

    def __init__(self):
        self.windows1 = tk.Tk()
        self.windows_properties()
        self.windows_components()

    def ingresar_sistema(self):
        self.windows1.destroy()
        PantallaRegistrarRevisionManual()

    def salir_sistema(self):
        self.windows1.destroy()

    def pantalla_integrantes(self):
        self.pantallaIntegrantes = PantallaIntegrantes()

    def windows_properties(self):
        self.windows1.title("Red Sismica")
        self.windows1.geometry("800x800+250+100")

        if str(platform.system()) == "Windows":
            self.windows1.iconbitmap("./Resources/Images/utnfrc.ico")

        self.windows1.configure(bg="lightblue")
        self.windows1.resizable(False, False)

    def windows_components(self):
        frame1 = tk.Frame(self.windows1)   
        frame1.configure(bg="lightblue")    

        label_name = tk.Label(frame1, text="Red Sismica")        

        label_subject = tk.Label(frame1, text="Diseño de sistemas de información")       

        label_group = tk.Label(frame1, text="Grupo 11. CU: 23 Registrar resultado de revisión manual")
        
        if str(platform.system()) == "Windows":
            label_name.config(fg="darkblue", bg="lightblue", font=("Arial", 25, "italic"))    
            label_group.config(fg="black", bg="lightblue", font=("Arial", 15, "bold"))
            label_subject.config(fg="black", bg="lightblue", font=("Arial", 15, "bold"))    
        else:
             label_group.config(fg="black", bg="lightblue")    
             label_name.config(fg="darkblue", bg="lightblue")    
             label_subject.config(fg="black", bg="lightblue")  

        if str(platform.system()) == "Windows":
            btn_integrantes = tk.Button(frame1, text="Integrantes (Grupo 11)", cursor="Hand2")
        else:
            btn_integrantes = tk.Button(frame1, text="Integrantes (Grupo 11)")

        btn_integrantes.config(fg="white", bg="gray", font=("Arial", 15, "bold"))
        btn_integrantes.config(command=self.pantalla_integrantes)

        image_open = Image.open("./Resources/Images/ImageRedSismica.png")
        image_open = ImageTk.PhotoImage(image_open)

        image_label = tk.Label(frame1, image=image_open)
        image_label.image = image_open    

        if str(platform.system()) == "Windows":
            btn_enter = tk.Button(frame1, text="Ingresar al sistema", cursor="Hand2")
        else:
            btn_enter = tk.Button(frame1, text="Ingresar al sistema")

        btn_enter.config(fg="white", bg="darkblue", font=("Arial", 15, "bold"))
        btn_enter.config(command=self.ingresar_sistema)

        if str(platform.system()) == "Windows":
            btn_quit = tk.Button(frame1, text="Salir del sistema", cursor="Hand2")
        else:
            btn_quit = tk.Button(frame1, text="Salir del sistema")

        btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))  
        btn_quit.config(command=self.salir_sistema)

        frame1.pack()
        label_name.pack() 
        label_subject.pack() 
        label_group.pack()
        btn_integrantes.pack()  
        image_label.pack(pady=45)       
        btn_quit.pack(side="left")    
        btn_enter.pack(side="right")   
    
if __name__ == "__main__":
    app_inicial = PantallaInicial()
    app_inicial.windows1.mainloop()