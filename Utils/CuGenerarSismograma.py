import tkinter as tk
from tkinter import ttk
from random import randint

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class CuGenerarSismograma():

    def __init__(self):
        self.root = tk.Tk()
        self.create_static_seismogram_gui()
        #self.root.mainloop()

    def create_static_seismogram_gui(self):
        
        self.root.title("Sismograma Simulado")        

        button_generar = ttk.Button(self.root, text="Generar", command=self.regenerar_sismograma)
        button_generar.pack(side=tk.TOP, pady=5)

        exit_button = ttk.Button(self.root, text="Salir", command=self.cerrar_ventana)
        exit_button.pack(side=tk.BOTTOM, pady=5)
        
        self.generar_sismograma()       

        
    def generar_sismograma(self):

        time = np.linspace(0, randint(0, 10), randint(0, 500)) 
        amplitude = np.sin(time * 5) * np.exp(-time / 2) + np.random.randn(len(time)) * 0.1

        fig, self.ax_sismogram = plt.subplots(figsize=(8, 4)) 

        self.ax_sismogram.plot(time, amplitude, color='purple')
        self.ax_sismogram.set_title("Sismograma Simulado")
        self.ax_sismogram.set_xlabel("Tiempo (s)")
        self.ax_sismogram.set_ylabel("Amplitud")
        self.ax_sismogram.grid(True)

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar_frame = ttk.Frame(self.root)
        self.toolbar_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()
        self.canvas.draw()       


    def regenerar_sismograma(self):
        self.toolbar = None
        self.toolbar_frame.pack_forget()
        self.canvas_widget.pack_forget()
        self.generar_sismograma()

    def cerrar_ventana(self):
        self.root.quit()
        self.root.destroy()


    
        
    

