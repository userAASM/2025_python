# 250516 week11

# 원 클래스 정의부

'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getCircumference(self):
        result = 2 * 3.14159265 * self.radius
        return result
        
    def getArea(self):
        result = 3.14159265 * self.radius ** 2
        return result

# 주프로그램부

small = Circle(1)
big = Circle(10)

print(f'반지름 {small.radius}인 원의', end ='')
print(f'둘레는 {small.getCircumference():.2f}이고, ', end = '')
print(f'넓이는 {small.getArea():.2f}이다.')

print(f'반지름 {big.radius}인 원의', end ='')
print(f'둘레는 {big.getCircumference():.2f}이고, ', end = '')
print(f'넓이는 {big.getArea():.2f}이다.')



class Circle :

    __PI = 3.14159265

    def getPI():
        return Circle.__PI
    
    def __init__(self, radius):
        self.setRadius(radius) 
        
    
    def getRadius(self) :
        return self.__radius


    def setRadius(self, radius) :
        if radius <= 0 :
            return False
        
        self.__radius = radius
        return True
    
    def getCircumference(self) :
        result = 2 * Circle.__PI * self.__radius
        return result
        
    def getArea(self) :
        result = Circle.__PI * self.__radius ** 2
        return result

# 주프로그램부

big = Circle(10)
print(big.getRadius())

big = Circle(100)
print(big.getRadius())

print(Circle.getPI())
'''

class Point :
    def __init__(self, x = 0, y = 0) :
        self.x = x
        self.y = y
    
    def show(self) :
        print(f'({self.x}, {self.y})')

    def set(self, x, y) : #필요 시 x, y의 유효성 확인
        self.x = x
        self.y = y

    def get(self) :
        return (self.x, self.y)


class Rectangle :
    
    def getWidth(self, a, b):
        w = b - a
        return w
    
    def getHeight(self, a, b):
        h = b - a
        return h
    
    def __init__(self, x1, y1, x2, y2) :

        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)

        
    def show(self):
                        
        print(f'\n좌측 상단 꼭지점이 ({self.lt.x}, {self.lt.y})이고, 우측 하단 꼭지점이 ({self.rb.x}, {self.rb.y})인 사각형입니다.')

    def getArea(self):
        W = self.getWidth(self.lt.x, self.rb.x)
        H = self.getHeight(self.lt.y, self.rb.y)

        area = W * H
        return area

    def getPerimeter(self):
        W = self.getWidth(self.lt.x, self.rb.x)
        H = self.getHeight(self.lt.y, self.rb.y)
        
        Perimeter = 2 * (W + H)
        return Perimeter


'''
def test() :
    p1 = Point()
    p2 = Point(2, 3)

    p1.show();

    p1.set(10, 20); p1.show();

    p2.show();

    x, y = p2.get()
    print(f'x = {x}, y = {y}')


# 주프로그램부

if __name__ == '__main__':
    test()

'''

# 주프로그램부 11.3

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

'''

#dustmqanswp 11.2

class Time:
    
    def __init__(self, h = 0, m = 0):
        self.h = h
        self.m = m        

    def display(self):
        print(f'{self.h:02d}:{self.m:02d}')

    def add(self, add): #받을 때 하나의 인수로 받아도 요소를 분리할 수 있음을 생각하지 못함
        addH = self.h + add.h
        addM = self.m + add.m
        if addM >= 60:
            addH += 1
            addM -= 60
        return Time(addH, addM) #Time으로 객체 만들어줄 발상하지 못함
        
    @staticmethod
    def is_valid(h, m):
        if 0 <= h <= 23 and 0 <= m <= 59:
            return True
        else:
            return False


#사용자 정의 함수부
        
def main():
    t1 = Time(9)
    t2 = Time(9, 30)

    t1.display()
    t2.display()

    later = t1.add(Time(1, 15))
    later.display()

    if Time.is_valid(25, 0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')

#주프로그램부

if __name__ == '__main__':
    main()


'''




