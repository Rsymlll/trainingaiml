class Emp:
    def __init__(self, id, name, qual):
        self.id=id
        self.name=name
        self.qual=qual
    
    def display(self):
        print('Id: ', self.id)
        print('Name: ', self.name)
        print('Qualification: ', self.qual)

class Dev(Emp):
    def __init__(self,id, name, qual, project, domain):
        super().__init__(id, name, qual)
        self.project=project
        self.domain=domain
    
    def display(self):
        super().display()
        print('Domain: ', self.domain)
        print('Project: ', self.project)

dev1= Dev(3, 'Ravi', 'Mtech', 'eShopping', 'dot.net') 
dev1.display()
print('******************************')
emp1= Emp(1, 'Sam', 'MCA')
emp1.display()