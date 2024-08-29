import customtkinter as ctk
from tkinter import PhotoImage

from calc import calculate

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Woodworking Calculator")
        self.iconbitmap("app/assets/favicon.ico")
        self.geometry("550x750")
        self.resizable(False, False)

        self.main_menu = Menu(self)

        self.mainloop()

class Menu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_columnconfigure((0,1,2,), weight=1)

        self.title = ctk.CTkLabel(self, text="Woodworker", bg_color="transparent")
        self.title.grid(column=1, row=0, sticky="")

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        self.mat_type = ctk.CTkComboBox(self, values=["option 1", "option 2"],
                                     command=combobox_callback)
        
        self.mat_type.grid(column=1, row=1, sticky="")

        self.mat_quantity = ctk.CTkEntry(self, placeholder_text="Material Quantity")
        self.mat_quantity.grid(pady=15, column=1, row=1, sticky="s")

        self.hours_worked = ctk.CTkEntry(self, placeholder_text="Hours Worked")
        self.hours_worked.grid(pady=15, column=1, row=2, sticky="")
        self.profit_margin = ctk.CTkEntry(self, placeholder_text="Profit Margin (%)")
        self.profit_margin.grid(pady=15, column=1, row=2, sticky="s")

        def btnEvnt() -> None:
            calculate.calculate(None)
        self.calc_button = ctk.CTkButton(self, text="Calculate Price", command=btnEvnt)
        self.calc_button.grid(pady=15, column=1, row=4, sticky="n")

        # Make sure to expand the main frame
        self.pack(expand=True, fill="both")

App()