# Task: Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

#Import the datetime class as d and the date class from the module datetime.
from datetime import date, datetime as d

# Define a class called 'Person' to represent a person with a name, country and date of birth.
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
# Define a method to calculate the age of a person using the date of birth and today's date.
    def calculate_age(self): 
        born = d(self.date_of_birth.year, self.date_of_birth.month, self.date_of_birth.day)
        age_in_days = d.utcnow() - born
        age = int(age_in_days.days) // 365
        return age
    
# Example usage: Create two person objects from the Person class and print their different data.
person1 = Person("Anna Schmidt", "Germany", date(1999, 1, 30))
print("\nName: ", person1.name)
print("Country: ", person1.country)
print("Date of Birth: ", person1.date_of_birth)
print("Age: ", person1.calculate_age())

person2 = Person("Jakub Novák", "Czech Republic", date(1994, 11, 4))
print("\nName: ", person2.name)
print("Country: ", person2.country)
print("Date of Birth: ", person2.date_of_birth)
print("Age: ", person2.calculate_age())       

