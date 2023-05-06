class Fruit:
    category="Fruit"
    
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste
    
    def get_name(self):
        return f"This is {self.name}  and it is a {self.category}"
    
    def find_by_color(self):
        return f"The {self.name} color is  {self.color}"
    
    def feel_the_taste(self):
        return f" The {self.category} is {self.taste}"