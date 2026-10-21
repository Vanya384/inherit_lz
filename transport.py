class Vehicle:
    def __init__(self,brand:str,model:str,year:int):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"brand:{self.brand},model:{self.model},year:{self.year}")


class Car(Vehicle):
    def __init__(self,brand : str, model : str, year : int, fuel_type : str, max_speed : int, engine_capacity : int, rotation_speed : int, pe : int):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed
        self.pe = pe

    def info(self):
        print(f"brand:{self.brand}, model:{self.model}, year:{self.year}, fuel_type:{self.fuel_type}, max_speed:{self.max_speed}, engine_capacity:{self.engine_capacity}, rotation_speed:{self.rotation_speed}")

    def engine_power_calc(self):
        power = (self.pe * self.rotation_speed)/7127
        return power

        
    