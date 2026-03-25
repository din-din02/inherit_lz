from animal import Dog          

def main():
    name = input("Введите имя собаки:")
    age = float(input("Введите возраст собаки:"))
    species = input("Введите вид собаки:")
    breed = input("Введите название породы:")
    guard_status = input("Введите статус охраны (да или нет):")
    dog = Dog(name,age,species,breed,guard_status)
    dog.info()
    dog.guard_house()
if __name__ == '__main1__':
    main()