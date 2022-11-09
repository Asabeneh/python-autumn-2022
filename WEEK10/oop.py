class Car:
    def __init__(self, name, model, color, mileage):
        self.name = name
        self.model = model
        self.color = color
        self.mileage = mileage
    def get_car_info(self):
        return f'The manufacturer is {self.name}. It was manufcatured in {self.model}. The color is {self.color}. It has been driven {self.mileage} kms.'
    


# Instantiate an object

c1 = Car('Toyota', 2020, 'Silver', '15000')
c2 = Car('Tesla', 2022, 'Golden', '00000')
""" print(c1.name, c1.model)
print(c2.name, c2.model)
print(c1.get_car_info())
print(c2.get_car_info()) """




class Person:
    from datetime import datetime
    now = datetime.now()
    year = now.year
    def __init__(self, first_name, last_name, country, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.birth_year = birth_year
        self.gender = gender
        self.skills = []
    def calcuate_age(self):
        return  self.year - self.birth_year
    def get_fullname (self):
        return f'{self.first_name} {self.last_name}'
    def get_person_info(self):
        fullname = self.get_fullname()
        age = self.calcuate_age()
        return f'{fullname} is from {self.country}. He is {age} years old.'
    


p1 = Person('Asab', 'Yeta', 'Finland',2000, 'Male')
p2 = Person('John', 'Doe', 'Sweden', 2010, 'Male')
p3 = Person('Maria', 'Antti', 'Finland', 2005,'Female')
print(p1.first_name, p1.last_name, p1.country, p1.birth_year)
print(p2.first_name, p2.last_name, p2.country, p2.birth_year)
print(p1.skills)
print(p1.get_person_info())
print(p2.get_person_info())
print(p3.get_person_info())
print(p1.calcuate_age())


class Student(Person):
    def __init__(self, first_name, last_name, country, birth_year, gender):
        super().__init__(first_name, last_name, country, birth_year, gender)
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_person_info(self):
        fullname = self.get_fullname()
        age = self.calcuate_age()
        pronoun = "He" if self.gender == 'Male' else 'She'
        """ pronoun = ''
        if self.gender == 'Male':
            pronoun = 'He'
        else:
            pronoun = 'She' """
        return f'{fullname} is from {self.country}. {pronoun} is {age} years old.'
       
       # CRUD

print(Student)
s1 = Student("Bibek", "Rasbin", 'Finland', 2000, 'Male')
s2 = Student("Yohana", "Asab", 'Finland', 2022, 'Female')
print(s1.get_person_info())
print(s2.get_person_info())
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('Python')
print(s1.skills)
print(s2.skills)





