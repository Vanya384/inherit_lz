class Animal:
    def __init__(self,name:str, age:int,species:str):
        self.name=name
        self.age=age
        self.species=species


    def make_sound(self):
        print(f"{self.name} издает звук")


    def info(self):
        print(f"name:{self.name}; age:{self.age}, species:{self.species}")


    def __del__(self):
        print(f"Объект {self.name} удален")


class Dog(Animal):
    def __init__(self, name:str, age:int, species:str,breed:str,guard_status:bool,):
        super().__init__(name, age, species)    #забирает данные сразу из родительского класса
        self.breed = breed
        self.guard_status = guard_status  


    def info(self):
        if self.guard_status:
            status = "Да"
        else:
            status = "Нет"
        print(f"Имя: {self.name}, Возраст: {self.age}, Вид: {self.species},Порода: {self.breed}, Охранник: {status}")


    def guard_house(self):
        if self.guard_status:
            Animal.make_sound(self)
        else:
            print(f"Отсутствие охраны")

    