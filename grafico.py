import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def create_static_seismogram_gui():
    root = tk.Tk()
    root.title("Sismograma Simulado")

    time = np.linspace(0, 10, 500) # 10 segundos, 500 muestras
    amplitude = np.sin(time * 5) * np.exp(-time / 2) + np.random.randn(len(time)) * 0.1

    fig, ax_sismogram = plt.subplots(figsize=(10, 6)) 

    ax_sismogram.plot(time, amplitude, color='purple')
    ax_sismogram.set_title("Sismograma Simulado")
    ax_sismogram.set_xlabel("Tiempo (s)")
    ax_sismogram.set_ylabel("Amplitud")
    ax_sismogram.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    toolbar_frame = ttk.Frame(root)
    toolbar_frame.pack(side=tk.BOTTOM, fill=tk.X)
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()
    canvas.draw()

    exit_button = ttk.Button(root, text="Salir", command=root.quit)
    exit_button.pack(side=tk.BOTTOM, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_static_seismogram_gui()