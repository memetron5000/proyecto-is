import gui
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


try:
    ruta_escritorio = Path.home() / "Desktop"
    ruta_completa = ruta_escritorio / "is" / "aa" / "build" / "assets"/"frame1"
        
except Exception as e:
    print(f"Error al obtener la ruta del escritorio: {e}")
        
#llama la ventana de login
gui.login()


