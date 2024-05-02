import customtkinter as ctk, os
from Path import *


class App():
    def __init__(self) -> None:
        os.system("cls")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.root.configure(fg_color='white')
        self.version = "v0.0.1"
        self.root.title(f"AMCAIM Toolbox")
        self.generic_counter = 0

        try:
            self.root.iconbitmap(f"app.ico")
        except Exception as e:
            print(e)


    def get_size(self) -> tuple:
        return (self.root.winfo_screenwidth(), self.root.winfo_screenheight())


    def set_size(self, w, h):
        x, y = self.get_position(w, h)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def get_position(self, w, h) -> tuple:
        return (
            (self.root.winfo_screenwidth()/2) - (w/2),
            (self.root.winfo_screenheight()/2) - (h/2)
        )


    def get_counter(self) -> int:
        return self.generic_counter


    def start(self) -> None:
        self.root.mainloop()

