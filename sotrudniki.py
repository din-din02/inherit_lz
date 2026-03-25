import math
class Employee:
    def __init__(self, name, position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def info(self):
        print('Имя:',self.name)
        print('Должность:',self.position)
        print('Тарифная ставка:',self.salary)

    def calc_salary(self,worked_days):
        money=self.position*self.salary*worked_days
        return money
    
class Manager(Employee):
    def __init__(self,name, position,salary, department, num_employees):
        super().__init__(name,position,salary)
        self.department=department
        self.num_employees=num_employees

    def info(self):
        print("*"*10,"Вся информация о сотруднике","*"*10)
        super().info()
        print('Отдел, в котором работает человек',self.department)
        print('Количество сотрудников в отделе',self.num_employees)

    def calc_salary(self, worked_days):
        money_1=self.position*self.salary*worked_days+self.position*self.salary*worked_days*(1/self.num_employees)
        return money_1
    
