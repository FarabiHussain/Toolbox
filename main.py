import docx, os
import customtkinter as ctk
from icecream import ic
from Path import *
from Img import *
from App import *

imgs = Img("lg")
app = App()
app.set_size(w=620, h=620)

first_button = ctk.CTkButton(app.root, text="", image=imgs.get("retag.png"), border_width=0, corner_radius=2, fg_color="transparent", command=lambda:(), width=72, height=72)
first_button.place(x=100, y=100)


app.start()


