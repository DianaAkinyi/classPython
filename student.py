#1) Update the Student Class to include these attributes - first_name, last_name, age, country
    # - Add these methods to the Student class
            # - show_full_name
             #- year_of_birth
           # - show_initials
class Student:
    school="Akirachix"
    def __init__(self,first_name, last_name, age, country):
        self.first_name= first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def show_full_name(self):
        return f"My name is {self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        return f"I was born in  {2023-self.age}"
    
    def show_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"
        

    



# input_string = "apple, orange, banana, mango, apple, mango, pear"
# word_list = input_string.split(",")
# unique_words = sorted(set(word_list))
# for word in unique_words:
#     print(word.strip()#


#2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
#Car
#Fruit
#Account
#Each class should have one class attribute and three instance variables.

#Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

#Then do the following in the interpreter 
#Create two instances of each class. 
#Call each of the methods you defined.
#Once you verify all the methods are working, commit your work, push to GitHub and submit.
#Class comments