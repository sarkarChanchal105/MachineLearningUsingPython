class employee:

    raise_amount=1.05

    def __init__(self,first,last):
        self.first=first
        self.last=last

    def printNames(self):
        print (self.first)
        print (self.last)

    def fullname(self):
        print('{} {}'.format(self.first,self.last))


    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


    @classmethod
    def set_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_storing(cls,string):
        first,last=string.split('-')
        return cls(first,last)


class developer(employee):
    def __init__(self,first,last,prog):
        super().__init__(first,last)
        self.prog=prog

    def from_storing(self,string):
        first,last=string.split('-')
        return first,last

class manager(employee):
    def __init__(self,firt,last,employee=None):
        super().__init__(firt,last)
        if employee is None:
            self.employee = []
        else :
            self.employee=employee

    def add_employee(self,emp):
        if emp  not in self.employee:
            self.employee.apped(emp)

    def remove_employee(self,emp):
        if emp   in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print (self.fullname(),emp.fullname())

#print (help(developer))

dev1 = developer('Chanchal','Sarkar','Python')
print ('{} ,{},{}'.format(dev1.first,dev1.last,dev1.prog))

mgr1 =manager('Kaushik','Das',[dev1])
mgr1.print_emp()

emp1= employee.from_storing('Sathvik-Sakala')
# print emp1.first

#
# emp1 =employee('Chanchal','Sarkar')
# emp1.printNames()
# emp2 =employee('Kaushik','Das')
# emp2.printNames()
#
# employee.set_amount(100)
#
# emp1.set_amount(101)
# print employee.raise_amount
#
#
import datetime
my_date= datetime.date(2017,5,4)
print (employee.is_workday(my_date))
print (emp1.is_workday(my_date))
#
