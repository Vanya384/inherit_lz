from animal import Animal,Dog
from transport import Car,Vehicle

cat_animal = Animal("Барсик",5,"Кот")
cat_animal.info()
cat_animal.make_sound()

big_dog = Dog("Бизон",9,"Собака","Немецкая овчарка",True)
big_dog.info()
big_dog.make_sound()
big_dog.guard_house()

small_dog = Dog("Лева",4,"Собака","Той терьер",False)
small_dog.info()
small_dog.make_sound()
small_dog.guard_house()

machine = Vehicle("Volvo","FH16",2019)
machine.info()
my_car = Car("Audi","RS6",2022,"Бензин",250,4,6000,800)
my_car.info()
calculated_power = my_car.engine_power_calc()
print(f"Рассчитанная мощность двигателя: {calculated_power} лошадиных сил")



