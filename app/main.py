import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk

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
        self.grid_columnconfigure((0,1,2), weight=1)

        self.title = ctk.CTkLabel(self, text="Woodworker", font=("Arial",32), bg_color="transparent")
        self.title.grid(column=1, row=0, sticky="")

        def combobox_callback(choice) -> None:
            pass

        self.mat_type = ctk.CTkComboBox(self, 
                                     values=["Pine Wood", "Oak Wood", "Birch Wood"],
                                     command=combobox_callback)
        
        self.mat_type.grid(column=1, row=1, sticky="")

        self.mat_quantity = ctk.CTkEntry(self, placeholder_text="Material Quantity")
        self.mat_quantity.grid(pady=15, column=1, row=1, sticky="s")

        self.hours_worked = ctk.CTkEntry(self, placeholder_text="Hours Worked")
        self.hours_worked.grid(pady=15, column=1, row=2, sticky="")
        self.profit_margin = ctk.CTkEntry(self, placeholder_text="Profit Margin (%)")
        self.profit_margin.grid(pady=15, column=1, row=2, sticky="s")

        def btnEvnt() -> None:
            price_data = [
                self.mat_type.get(),
                self.mat_quantity.get(),
                self.hours_worked.get(),
                self.profit_margin.get()]
            print(calculate.calculate(price_data))


        """img = Image.open("app/assets/cog.png")
        img = img.resize((32, 32))
        cog_image = ImageTk.PhotoImage(img)
        self.settings_btn = ctk.CTkButton(self, width=32, image=cog_image, text="", fg_color="red", command=btnEvnt)
        self.settings_btn.grid(ipadx=3, ipady=3, column=0, row=0, sticky="nw",)"""

        self.calc_btn = ctk.CTkButton(self, text="Calculate Price", command=btnEvnt)
        self.calc_btn.grid(pady=15, column=1, row=4, sticky="n")

        self.pack(expand=True, fill="both")

App()