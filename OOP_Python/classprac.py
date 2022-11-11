class Employee:
    def __init__(self, name, task=None):
        self.name = name
        #check empty list parameter
        if task is None:
            task = []
        self.task = task
        #method to add items to list
    def add_task(self, task):
        self.task.append(task) 
        return self.task   
        #string magic method
    def __str__(self):
        return f'Employee({self.name},{self.task})'

class Person:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        #Accesor method
    def get_fname(self):
        return self.firstname
    def get_lname(self):
        return self.lastname
        #Mutator method
    def set_fname(self, lastname):
        self.lastname = lastname
        #method to get full names 
    def fullname(self):
        return self.firstname +" "+ self.lastname
        #string magic method
    def __str__(self):
        return f'Person({self.firstname},{self.lastname})'
#object instatiation
teacher = Person("Elon","Musk")
#invoking accesor method to output firstname and lastname
p1 = teacher.get_fname()
print(p1)
p2 = teacher.get_lname()
print(p2)
#invoking mutator method to update firstname
teacher.set_fname("UpdatedName")
#invoking fullname methods
p3 = teacher.fullname()
print(p3)
#object instatiation
manager = Employee("Josh")
#calling methods to add items(tasks) in a list
manager.add_task("Supervise")
manager.add_task("Cordinate")
#outputting the  two objects 
print(manager,"\t",p3)


'''
This is an illustration of how to create a class
define init constructor that takes a list arg
and uses a method to add items into the list.
Also demonstrates the string magic method in action,
accesor methods(get_), mutator method (set_),
how to instatiate an object and printout every evaluation.

'''