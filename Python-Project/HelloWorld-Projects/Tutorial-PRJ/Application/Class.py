class Employee:
    def __init__ (self,firstName,LastName):
        self.first = firstName
        self.last = LastName
        self.email = firstName +'.'+LastName +'@company.com'

    def FullName (self):
        return '{} {}'.format(self.first, self.last)

    def Address (self,city,zipc):
        self.city = city
        self.zipc = zipc



emp_1 = Employee('Prajwol','Thapa')
emp_2 =  Employee('tHHY','Thapa')
Add = Employee('USA','2532')

print (Employee.addressss())
