'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check_age(self):
        if self.age <= 19:
            return True
        else:
            return False
        
# p1 = Person('성현', 19)
# print(p1.name)
# print(p1.age)
# print(p1.check_age())
    '''




from datetime import date


class Person:
    # 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year) 
    #클래스메소드인 details의 name과 year에 인자들이 들어가고, 계산된 year값이 
    # init으로 돌어가서 name과 age에 각각 들어감


    def check_age(self):
        return self.age > 19

p1 = Person.details('성현', 1999)
print(p1.check_age())