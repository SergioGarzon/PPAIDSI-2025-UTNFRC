from tkinter import *
from tkinter import ttk

new_window = Tk()
 
def habilitarPantalla():

    new_window.title("Red Sismica")
    new_window.geometry("1000x400+500+300")
    new_window.iconbitmap("./Images/utnfrc.ico")
    new_window.configure(bg="lightblue")
    new_window.resizable(False, False)

    label_title = Label(new_window, text="Red Sismica")
    label_title.config(fg="darkblue", bg="lightblue", font=("Arial", 25, "italic"))   

    label_subtitle = Label(new_window, text="Eventos sismicos detectados sin revisión")
    label_subtitle.config(fg="darkblue", bg="lightblue", font=("Arial", 15, "italic"))     

    table = ttk.Treeview(new_window, columns=('numero', "fecha", "hora", "ubicación", "magnitud", "seleccione"), show="headings")

    style = ttk.Style(new_window)
    style.configure("Treeview.Heading", font=(None, 15))

    table.heading("numero", text="Número")   
    table.heading("fecha", text="Fecha del evento")
    table.heading("hora", text="Hora del evento")
    table.heading("ubicación", text="Ubicación")
    table.heading("magnitud", text="Magnitud")
    table.heading("seleccione", text="Seleccione")

    table.column("numero", width=80)
    table.column("fecha", width=160)
    table.column("hora", width=150)
    table.column("ubicación", width=150)
    table.column("magnitud", width=120)
    table.column("seleccione", width=120)

    btn_quit = Button(new_window, text="Salir del sistema", cursor="Hand2")
    btn_quit.config(fg="white", bg="red", font=("Arial", 15, "bold"))  
    btn_quit.config(command=salir_sistema)

    label_title.pack()
    label_subtitle.pack()
    table.pack()
    btn_quit.pack(side=LEFT)    

    mostrar_datos_sismos(table)
    

def salir_sistema():
    new_window.destroy()


#DATOS DE PRUEBA UNICAMENTE
def mostrar_datos_sismos(table):
    table.insert(parent='', index=0, values=('0', '15/05/2025', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=1, values=('1', '20/05/2024', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=2, values=('2', '11/05/2023', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=3, values=('3', '13/05/2022', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=4, values=('4', '09/05/2020', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=5, values=('5', '13/05/2022', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=6, values=('6', '09/05/2020', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=7, values=('7', '13/05/2022', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=8, values=('8', '09/05/2020', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=9, values=('9', '13/05/2022', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=10, values=('10', '09/05/2020', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=11, values=('11', '13/05/2022', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))
    table.insert(parent='', index=12, values=('12', '09/05/2020', '11:30:00', '39°17′ N, 76°36′ O', '15°', 'Seleccione'))


habilitarPantalla()

new_window.mainloop()
