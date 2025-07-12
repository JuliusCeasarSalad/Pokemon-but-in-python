import tkinter as tk

Showdown = tk.Tk()
Showdown.title("Pykemon")

window_width = 500
window_height = 350

Showdown.columnconfigure(0, weight=1)
Showdown.columnconfigure(1, weight=3)

screen_width = Showdown.winfo_screenwidth()
screen_height = Showdown.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

Showdown.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Showdown.resizable(False, False)