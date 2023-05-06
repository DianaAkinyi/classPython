class Car:
    wheel=4
    
    def __init__(self,make ,model,color):
        self.make=make
        self.model=model
        self.color=color

    def start(self):
        return f"The {self.color}  {self.wheel}  {self.make} is starting"
    
    def stop(self):
        return f"I want the {self.color} {self.make} car  with {self.wheel} to stop."
    
    def  accelerate(self):
        return f"The {self.make} car is accelerating at a high  speed"
