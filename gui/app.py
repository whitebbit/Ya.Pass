import customtkinter as ui
import database.utils as db
from gui import utils
from gui.models import PassFrame
from gui.stylesheet import main_button, bg_main_color, entry_color


def window():
    ui.set_default_color_theme("blue")
    root = ui.CTk()
    root.title("Ya.Pass")
    root.geometry("250x350")
    root.resizable(False, False)

    frame = ui.CTkScrollableFrame(root, corner_radius=0, fg_color=bg_main_color, scrollbar_button_color=entry_color, scrollbar_button_hover_color=entry_color)
    frame.pack(expand=True, fill=ui.BOTH)

    add_pass_button = ui.CTkButton(root, text="ADD", command=lambda: utils.add_pass(frame), **main_button.style)\
        .pack(**main_button.pack)

    for item in list(db.all_items()):
        pass_frame = PassFrame(frame, item.service)

    root.mainloop()
