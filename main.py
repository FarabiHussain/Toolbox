import customtkinter as ctk
from Path import *
from Img import *
from GUI import *
from App import *

imgs = Img("lg")
main_app = App()
main_app.set_size(w=420, h=500)

app_list = {
    "RetAG": "Retainer agreements",
    "InvitationGen": "Invitation letters",
    "PayTrack": "Payment receipts",
    "PayLock": "Payment authorizations",
}

frame = ctk.CTkFrame(
    master=main_app.root,
    fg_color="white",
    border_width=1,
)

frame.pack(padx=10, pady=10, fill="both", expand=True)

scr_frame = ctk.CTkScrollableFrame(
    master=frame,
    fg_color="white",
    border_width=0,
)

scr_frame.pack(padx=1, pady=1, fill="both", expand=True)

for i, current_app in enumerate(app_list):
    ic(current_app)
    AppButton(
        app=main_app,
        master=scr_frame,
        app_name=current_app, 
        image=imgs.get(f"{current_app}.png"), 
        desc=app_list[current_app],
        row=i,
    )

main_app.start()
