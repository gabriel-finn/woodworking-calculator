import json

global settings
def loadSettings(filepath:str=None):
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
settings= loadSettings("app/settings/rates.json")

def calcMaterialCost(mat_name:str=None, mat_q=1,) -> int:

    mat_cost = settings.get("materials",{}).get(mat_name,0)

    return float(mat_q) * mat_cost

def calcLaborCost(hours_worked:float=12, hourly_rate:float=20.00):
    return int(hours_worked) * hourly_rate

def calcOverheadCost(overhead=150):

    total = overhead
    return total

def calculate(data:list=None) -> int:
    total_cost = calcMaterialCost(str(data[0]),int(data[1])) + calcLaborCost(data[2]) + calcOverheadCost()
    profit = total_cost * (int(data[3]) / 100)
    return total_cost + profit