def calcMaterialCost(test=123):
    return test

def calcLaborCost(hours_worked:float=12, hourly_rate:float=35.00):
    return hours_worked * hourly_rate

def calcOverheadCost(overhead=150):

    total = overhead
    return total

def calculate(data:list=None) -> int:
    total_cost = calcMaterialCost() + calcLaborCost() + calcOverheadCost()
    profit = total_cost * (25 / 100)
    return total_cost + profit