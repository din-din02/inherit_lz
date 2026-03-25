class Animal:
    def __init__(self,name,age,species):
        self.name = name 
        self.age = age
        self.species = species 
    def make_sound(self):
        print("Издаёт звук")
    def info(self):
        print("Имя:",self.name)
        print("Возраст:",self.age)
        print("Вид животного:",self.species)
    def __del__(self):
        print("Объект удалён")

class Dog(Animal):
    def __init__(self,name,age,species,breed,guard_status):
        super().__init__(name,age,species)
        self.breed = breed
        self.guard_status = guard_status
    def info(self):
         print( "*"*10,"Вся информация о собаке","*"*10)
         super().info()
         print("Порода:",self.breed)
         print("Статус охраны:",self.guard_status)
    def guard_house(self):
            print("Что делает собака?")
            if self.guard_status == 'да':
                print("Охраняет дом")
            elif self.guard_status == 'нет':
                print("Отдыхает") 
            else:
                print("Вы ввели не верный статус охраны!")
name = input("Введите имя собаки:")
age = float(input("Введите возраст собаки:"))
species = input("Введите вид собаки:")
breed = input("Введите название породы:")
guard_status = input("Введите статус охраны (да или нет):")
dog = Dog(name,age,species,breed,guard_status)
dog.info()
dog.guard_house()