import tkinter as tk
window = tk.Tk(width=100,height=100)
greeting = tk.Label(text="Привет, Tkinter!",
                    bg="grey",
                    fg="black",
)
greeting.pack()
window.mainloop()