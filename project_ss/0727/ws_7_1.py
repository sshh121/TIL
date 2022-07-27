class Nationality:  
    def __init__(self, nation):
        self.nation = nation  #인스턴스의 이름에 파라미터로 넘어온 "대한민국"을 넣어라

    def __str__(self):
        return f'나의 국적은 {self.nation}'



korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국