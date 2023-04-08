import customtkinter as ui
from tkinter import messagebox


from gui.stylesheet import options_button, main_button, h2_label, h1_label, frame, entry_color, entry
from pass_system import utils as pass_utils
import pyperclip3 as pc
from database.utils import delete


class PassFrame(ui.CTkFrame):
    def __init__(self, root, service):
        ui.CTkFrame.__init__(self, root, **frame.style)

        self.label = ui.CTkLabel(self, text=service, **h2_label.style)
        self.label.pack(**h2_label.pack)

        self.delete_button = ui.CTkButton(self, text="D", command=self.delete_pass, **options_button.style).pack(
            **options_button.pack)
        self.edit_button = ui.CTkButton(self, text="E", command=self.edit_pass, **options_button.style).pack(
            **options_button.pack)
        self.view_button = ui.CTkButton(self, text="V", command=self.view_pass, **options_button.style).pack(
            **options_button.pack)

        self.pack(fill=ui.X, expand=True, pady=5)
        self.line = ui.CTkFrame(root, height=2, fg_color=entry_color)
        self.line.pack(fill=ui.X)
        self.service = service

    def delete_pass(self):
        value = messagebox.askquestion("deleting pass".title(),
                                       f"Do you really want to remove the pass for '{self.service}'?")
        if value == "no":
            return

        delete(self.service)
        self.line.destroy()
        self.destroy()

    def view_pass(self):
        ViewPassWindow(self.master, self.service)

    def edit_pass(self):
        EditPassWindow(self.master, self.service)


class AddPassWindow(ui.CTkToplevel):
    def __init__(self, root):
        ui.CTkToplevel.__init__(self, root, **frame.style)
        self.geometry("250x190")
        self.resizable(False, False)

        self.title("Add new pass")
        self.label = ui.CTkLabel(self, text="Enter your data", **h1_label.style).pack(**h1_label.pack)
        self.service_data = DataFrame(self, "service", "Service")
        self.login_data = DataFrame(self, "login", "User")
        self.password_data = DataFrame(self, "password", "***********")
        self.add_button = ui.CTkButton(self, text="ADD", command=self.add_data, **main_button.style).pack(
            **main_button.pack)

    def add_data(self):
        service = self.service_data.data_enter.get()
        login = self.login_data.data_enter.get()
        password = self.password_data.data_enter.get()

        if self.message(service, login, password) is False:
            return

        service_name = pass_utils.add(service, login, password)
        PassFrame(self.master, service_name)
        self.destroy()

    @staticmethod
    def message(service, login, password):
        if service == "":
            messagebox.showerror("service name Error".title(), "Enter service name!")
            return False
        elif len(service) > 15:
            messagebox.showerror("service name Error".title(), "Service name is too long! Max length is 15 characters")
            return False

        if login == "":
            value = messagebox.askquestion("login value warning".title(),
                                           "You have not entered your login. Default login: "
                                           "'User'. Do you want to continue?")
            if value == "no":
                return False
        if password == "":
            value = messagebox.askquestion("password value warning".title(),
                                           "You have not entered your password. The password will be generated "
                                           "automatically. Do you want to continue?")
            if value == "no":
                return False


class ViewPassWindow(ui.CTkToplevel):
    def __init__(self, root, service):
        ui.CTkToplevel.__init__(self, root, **frame.style)
        self.geometry("250x150")
        self.resizable(False, False)

        self.title(f"View pass")
        self.label = ui.CTkLabel(self, text=service, **h1_label.style).pack(**h1_label.pack)
        self.login, self.password = pass_utils.get(service)
        self.login_copy = CopyFrame(self, self.login)
        self.password_copy = CopyFrame(self, self.password)

        self.ok_button = ui.CTkButton(self, text="OK", command=self.destroy, **main_button.style).pack(
            **main_button.pack)


class EditPassWindow(ui.CTkToplevel):
    def __init__(self, root, service):
        ui.CTkToplevel.__init__(self, root, **frame.style)
        self.geometry("250x150")
        self.resizable(False, False)

        self.old_pass = pass_utils.get(service)

        self.title("Edit pass")
        self.label = ui.CTkLabel(self, text="Enter your changes", **h1_label.style).pack(**h1_label.pack)
        self.login_data = DataFrame(self, "login", self.old_pass[0])
        self.password_data = DataFrame(self, "password", self.old_pass[1])
        self.save_button = ui.CTkButton(self, text="SAVE", command=self.edit_data, **main_button.style).pack(
            **main_button.pack)

    def edit_data(self):
        login = self.login_data.data_enter.get()
        password = self.password_data.data_enter.get()

        if login == "":
            login = self.old_pass[0]
        if password == "":
            password = self.old_pass[1]

        pass_utils.edit(self.service, login, password)
        self.destroy()


class DataFrame(ui.CTkFrame):

    def __init__(self, root, data_type, default_value):
        ui.CTkFrame.__init__(self, root, **frame.style)

        self.data_label = ui.CTkLabel(self, text=f"{data_type.title()}:", **h2_label.style).pack(side=ui.LEFT, padx=5)
        self.data = ui.StringVar()
        self.data_enter = ui.CTkEntry(self, placeholder_text=f"{default_value}", **entry.style)
        self.data_enter.pack(**entry.pack)
        self.pack(fill=ui.X, pady=5)


class CopyFrame(ui.CTkFrame):
    def __init__(self, root, data):
        ui.CTkFrame.__init__(self, root, **frame.style)

        self.label = ui.CTkLabel(self, text=data, **h2_label.style).pack(**h2_label.pack)
        self.copy_button = ui.CTkButton(self, text="Copy", command=lambda: pc.copy(data), **options_button.style) \
            .pack(**options_button.pack)

        self.pack(fill=ui.X, pady=5)
