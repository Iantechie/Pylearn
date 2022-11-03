class Employee:
    def __init__(self,id,name,hours,rate):
        self.id = id
        self.name = name
        self.hours = float(hours)
        self.rate = float(rate)
        
        #accesor methods
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_hours(self):
        return self.hours
    def get_rate(self):
        return self.rate
        # get_total_pay method
    def get_total_pay(self):
        total_pay = self.hours*self.rate
        return total_pay

        #string magic method to enable print out object fields
    def __str__(self):
        return f'Employee({self.id},{self.name},{self.hours},{self.rate})'
        #object instatiation
emp1 = Employee(1,'John',3,5)
emp2 = Employee(2,'Doe',4,6)
print(emp1)
print(emp2)
#invoking the accesor method
x = emp2.get_name()
print(x)
