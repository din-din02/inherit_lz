from sotrudniki import Manager

def main():
    name=input('Введите имя сотрудника:') 
    position=float(input('Введите на каком месте сотрудник:'))
    salary=float(input('Введите тарифную ставку:'))
    department=input('Введите отдел:')
    num_employees=float(input('Введите количество сотрудников в отделе:'))
    manager=Manager(name, position,salary, department, num_employees)
    manager.info()
    num_employees=float(input('Введите количество проработанных дней:'))
    money=manager.calc_salary(num_employees)
    print('Зарплата сотрудника:',money)
if __name__ == '__main2__':
    main()

    