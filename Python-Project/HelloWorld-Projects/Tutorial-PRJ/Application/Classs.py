class Employee:
    raise_amount =1.04
    def __init__ (self,firstName,LastName,City,Pay):
        self.first = firstName
        self.last = LastName
        self.email = firstName +'.'+LastName +'@company.com'
		self.City= City
        self.pay = pay

    def FullName (self):
        return '{} {}'.format(self.first, self.last)

    def Address(self):
        return self.City

    def Apply_raise(Self):
        self.pay = (self.pay * 1.04)




emp_1 = Employee('Prajwol','Thapa','Kathmandu')
emp_2 = Employee('tHHY','Thapa','Nepal')


print (emp_1.Address())
