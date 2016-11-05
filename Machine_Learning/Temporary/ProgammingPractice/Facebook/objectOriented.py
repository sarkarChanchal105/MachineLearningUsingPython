class Employee():
    num_of_employees=0
    raise_amount=1.04
    def __init__(self,f_name,l_name,pay):
        self.firstName=f_name
        self.lastName=l_name
        self.pay=pay
        Employee.num_of_employees +=1

    def fullname(self):
        return ('{} {}'.format(self.firstName,self.lastName))

    def apply_raise(self):
        self.pay=int(self.pay) * 1.04

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

emp_1= Employee('Chanchal','Sarkar','90000')

Employee.set_raise_amt(1.06)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.fullname())
print(emp_1.pay)

