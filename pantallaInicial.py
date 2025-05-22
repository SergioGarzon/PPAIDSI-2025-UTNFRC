import tkinter as tk

from PIL import ImageTk, Image

windows1 = tk.Tk()

def windows_properties(windows1):
    windows1.title("Red Sismica")
    windows1.geometry("800x780+500+300")
    windows1.iconbitmap("./Images/utnfrc.ico")
    windows1.configure(bg="lightblue")
    windows1.resizable(False, False)

def windows_components(windows1):
    frame1 = tk.Frame(windows1)   
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

    btn_enter = tk.Button(frame1, text="Registrar resultado revisión manual", cursor="Hand2")
    btn_enter.config(fg="white", bg="darkgreen", font=("Arial", 15, "bold"))
    btn_enter.config(command=opcion_registrar_resultado_revision_manual)

    btn_quit = tk.Button(frame1, text="Salir del sistema", cursor="Hand2")
    btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))  
    btn_quit.config(command=salir_sistema)

    frame1.pack()
    label_name.pack() 
    label_subject.pack() 
    label_group.pack()
    label_members.pack()
    label_members2.pack()
    image_label.pack(pady=45)  
    btn_quit.pack(side="left")    
    btn_enter.pack(side="right")

def salir_sistema():
    windows1.destroy()

def opcion_registrar_resultado_revision_manual():
    windows1.destroy()
    import PantallaRegistrarRevisionManual

windows_properties(windows1)
windows_components(windows1)

tk.mainloop()