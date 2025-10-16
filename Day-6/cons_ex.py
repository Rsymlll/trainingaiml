class Emp:
    def __init__(self, id, name, qualification):
        self.id = id
        self.name = name 
        self.qualification = qualification

    def display(self):
        print('Id:', self.id)
        print('Name:', self.name)
        print('Qualification:', self.qualification)

class Dev(Emp):
    def __init__(self, id, name, qualification, domain, project):
        super().__init__(id, name, qualification)  # calls parent constructor
        self.domain = domain
        self.project = project

    def display(self):
        super().display()  # calls parent display()
        print('Domain:', self.domain)
        print('Project:', self.project)

# create object
d1 = Dev(101, 'Syam', 'Degree in IT', 'Web Development', 'MyEvent App')
d1.display()
