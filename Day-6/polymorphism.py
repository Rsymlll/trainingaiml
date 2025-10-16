# class Bird:
#     def fly(self):
#         print('Bird can fly')
    
# class Airplane(Bird):
#     def fly(self):
#         print('Airplane can fly')

# b=Bird()
# print('Bird Implement')
# b.fly()

# a=Airplane()
# print('Airplane Implementation')
# a.fly
# print('Using for loop')

# for obj in [Bird(), Airplane()]:
#     obj.fly()

class Emp:
    def reg(self):
        self.id=int(input('Enter id: '))
        self.name=input('Enter name: ')

    def disp(self):
        print('Name: ',self.name)
        print('ID: ',self.id)

class Dev(Emp):
    def reg(self):
        super().reg()
        self.domain=input('Enter Domain')
    
    def disp(self):
        super().disp()
        print('Domain: ',self.domain)
    
d1=Dev()
d1.reg()
d1.disp()

