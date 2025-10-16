class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def print_info(self):
        print('ID:',self.id)
        print('Name:',self.name)