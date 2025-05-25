import tkinter as tk

class PantallaIntegrantes():

    def __init__(self):
        self.windows1 = tk.Tk()
        self.windows_properties()
        self.windows_components()

    def windows_properties(self):
        self.windows1.title("Red Sismica")
        self.windows1.geometry("500x400+250+100")
        self.windows1.iconbitmap("./Resources/Images/utnfrc.ico")
        self.windows1.configure(bg="lightblue")
        self.windows1.resizable(False, False)

    def windows_components(self):       

        label_members = tk.Label(self.windows1, text="Integrantes: ")
        label_members.config(fg="black", bg="lightblue", font=("Arial", 15, "bold")) 

        label_member1 = tk.Label(self.windows1, text="\n\n* De Llamas Agustin " +
        "\n* Garzon Sergio \n* Ibañez Ignacio \n* Masino Nicolas \n* Roth Max" +
        "\n* Tarraga Ezequiel \n*Mezzopeva Juan Cruz \n*Piazza Gonzalo \n*Vaca Adriel \n\n")
        label_member1.config(fg="black", bg="lightblue", font=("Arial", 15)) 
      
        btn_quit = tk.Button(self.windows1, text="Cerrar ventana", cursor="Hand2")
        btn_quit.config(fg="white", bg="blue", font=("Arial", 15, "bold"))  
        btn_quit.config(command=self.quitar_ventana)

        label_members.pack()
        label_member1.pack()  
        btn_quit.pack()   
    
    def quitar_ventana(self):
        self.windows1.destroy()