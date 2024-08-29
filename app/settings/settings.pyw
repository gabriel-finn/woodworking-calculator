import customtkinter as ctk
import json

def loadSettings(filepath):
    try:
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filepath}.")
        return {}

class Settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()
        settings = loadSettings("app/settings/rates.json")

        self.master = master
        pass
