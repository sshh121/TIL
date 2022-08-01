class Doggy:
    num_of_dogs = 0 #현재 개의 숫자
    birth_of_dogs = 0 #태어난 개의 숫자

    def __init__(self, name, type):
        self.name = name
        self.type = type
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print(f'{self.name} : 왈왈')

    def get_status(self):
        print(f'{Doggy.birth_of_dogs}마리 태어났습니다')    
        print(f'현재 {Doggy.num_of_dogs}마리 있습니다\n')
    
    def __del__(self):
        Doggy.num_of_dogs -= 1

dog1 = Doggy('초코', '코카스파니엘')
dog1.bark()
dog1.get_status()


dog2 = Doggy('감자', '포메라니안')
dog2.bark()
dog2.get_status()

dog3 = Doggy('뽀삐', '치와와')
dog3.bark()
dog3.get_status()

del dog3
print(f'현재 {Doggy.num_of_dogs}마리 있습니다')

