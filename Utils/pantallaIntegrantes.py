import tkinter as tk

class PantallaIntegrantes():

    def __init__(self):
        self.windows1 = tk.Tk()
        self.windows_properties()
        self.windows_components()

    def windows_properties(self):
        self.windows1.title("Red Sismica")
        self.windows1.geometry("600x600+250+100")
        self.windows1.iconbitmap("./Resources/Images/utnfrc.ico")
        self.windows1.configure(bg="yellow")
        self.windows1.resizable(False, False)

    def windows_components(self):
        frame1 = tk.Frame(self.windows1)   
        frame1.configure(bg="lightblue")    
        
        label_members = tk.Label(frame1, text="Integrantes: \n\n*de Llamas Agustin \n*Garzon Sergio \n*Ibañez Ignacio \n*Masino Nicolas" +
        "\n*Mezzopeva Juan Cruz \n*Piazza Gonzalo \n*Roth Max \n*Tarraga Ezequiel \n*Vaca Adriel")
        label_members.config(fg="black", bg="lightblue", font=("Arial", 15)) 
        
        btn_quit = tk.Button(frame1, text="Salir del sistema", cursor="Hand2")
        btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))  
        btn_quit.config(command=self.quitar_ventana)

        frame1.pack()
        label_members.pack()
        btn_quit.pack(side="left")   
    
    def quitar_ventana(self):
        self.windows1.destroy()