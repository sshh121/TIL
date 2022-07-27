class Doggy:  #클래스명은 첫문자는 대문자
    num_of_dogs = 0
    birth_of_dogs = 0

    @classmethod
    def get_status(cls):
        print('지금 살아있는 강아지:', cls.num_of_dogs)
        print('지금 태어난 강아지:', cls.birth_of_dogs)

    def __init__(self, name, breed): #인스턴스 생성시 사용
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1 #모든 개에 대한 개수들이므로 클래스 변수로 만들기
    
    def __del__(self):
        Doggy.num_of_dogs -= 1


    def bark(self):
        print(f'{self.name}가 멍멍')

d1 = Doggy('해피', '푸등')
d2 = Doggy('멍멍이', '말티즈')
d1.bark()

Doggy.get_status()  #클래스 메소드는 클래스와 함께 쓰는 것을 권장한다