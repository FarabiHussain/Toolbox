import customtkinter as ctk
import os
import json
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
        self.subapps = self.__read_subapps()

        try:
            self.root.iconbitmap(f"{os.getcwd()}\\assets\\icons\\app.ico")
        except Exception as e:
            print(e)


    def __read_subapps(self) -> dict:
        try:
            f = open('subapps.json')
            loaded = json.load(f)
            f.close()

            return loaded["subapps"]
        except Exception as e:
            print(e)

        return {}


    def get_subapps(self) -> dict:
        return self.subapps


    def get_size(self) -> tuple:
        return (self.root.winfo_screenwidth(), self.root.winfo_screenheight())


    def set_size(self, w, h):
        x, y = self.__get_position(w, h)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def __get_position(self, w, h) -> tuple:
        return (
            (self.root.winfo_screenwidth()/2) - (w/2),
            (self.root.winfo_screenheight()/2) - (h/2)
        )


    def start(self) -> None:
        self.root.mainloop()


    def hide(self) -> None:
        self.root.withdraw()


    def unhide(self) -> None:
        self.root.deiconify()

