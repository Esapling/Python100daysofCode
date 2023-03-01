class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.family_name = "Sasd"
    def swim(self):
        print("Moving in water")
    
    def breathe(self):
        super().breathe()
        print("Doing this in water")
        


a = Fish()
a.breathe()
        