class Calculator:   
    def add(self, num1,num2):
        return num1 + num2
    def substract(self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다.'

a=Calculator()
print(a.add(1,2))
print(a.substract(2,1))
print(a.multiply(3,4))
print(a.divide(4,0))

