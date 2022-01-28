class Person:
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def set_persone(self,p_name,p_surname,p_age):
        self.__name = p_name
        self.__surname = p_surname
        self.__age =p_age

    def __str__(self):
        return "Name: {}, Surname: {}, Age: {}\n".format(self.__name,self.__surname,self.__age)

class Employee(Person):

    def __init__(self,name,surname,age,salary):
        super().__init__(name,surname,age)
        self.salary = salary

    def __str__(self):
        persone = super().__str__()
        return "".join((persone,"Salary: {}\n".format(self.salary)))

class Manager(Employee):

    def __init__(self,name,surname,age,salary):
        super().__init__(name,surname,age,salary)

    def __str__(self):
        return super().__str__()

class Worker(Employee):

    def __init__(self,name,surname,age,salary):
        super().__init__(name,surname,age,salary)

    def __str__(self):
        persone =  Person.__str__(self)
        return "".join((persone,"Salary 100 * {} hours: {}\n".format(self.salary,self.salary * 100)))

class Agent(Employee):
    def __init__(self,name,surname,age,salary,sale):
        super().__init__(name,surname,age,salary)
        self.sale = sale

    def __str__(self):
        persone = Person.__str__(self)
        return "".join((persone, "Salary {} * bonus {} : {}\n"
                        .format(self.salary, self.sale * 0.05,
                                (self.salary + (self.sale * 0.05)))))

def def_print(type,emp_1,emp_2,emp_3):
    print("""
    {}:
    {}
    {}
    {}
    """.format(type,emp_1, emp_2, emp_3))

manager_1 = Manager("Bill","Ace",35,13000)
manager_2 = Manager("Jac","Fort",33,13000)
manager_3 = Manager("Bob","Dorn",32,13000)
def_print("Managers",manager_1,manager_2,manager_3)

agent_1 =Agent("Smith","007",30,5000,300)
agent_2 =Agent("Tod","Bro",33,5000,700)
agent_3 =Agent("Sam","One",31,5000,450)
def_print("Agents",agent_1,agent_2,agent_3)

worker_1 = Worker("Tom","Fod",24,18)
worker_2 = Worker("Tim","More",23,21)
worker_3 = Worker("Rod","Fod",25,20)
def_print("Workers",worker_1,worker_2,worker_3)



