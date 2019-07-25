
'''
class student_score:
    def __init__(self, scores):
        self.kor = scores[0]
        self.eng = scores[1]
        self.math = scores[2]
        self.sum = int(scores[0]) + int(scores[1]) + int(scores[2])

    def __del__(self):
        pass


input_value = input()
score = list(input_value.split(", "))
a = student_score(score)
print('국어, 영어, 수학의 총점: {0}'.format(a.sum))
'''
'''
class korean:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def printNationality(self):
        print("대한민국")

a = korean()
a.printNationality()
a.printNationality()
'''
'''
name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진

GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를

다음과 같이 문자열로 출력하는 코드를 작성하십시오.
'''
'''
class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        pass

    def print_name(self):
        print("이름: {0}".format(self.name))

class GraduateStudent(Student):
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __del__(self):
        pass

    def print_name_major(self):
        print("이름: {0}, 전공: {1}".format(self.name, self.major))


a = Student("홍길동")
b = GraduateStudent("이순신", "컴퓨터")

a.print_name()
b.print_name_major()
'''
'''
class Circle:
    def __init__(self, r):
        self.r = r

    def __del__(self):
        pass

    def area_circle(self):
        area = self.r ** 2 * 3.14
        print("원의 면적: {0}".format(area))

a = Circle(2)
a.area_circle()
'''
'''
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __del__(self):
        pass

    def area_rec(self):
        area = self.a * self.b
        print("사각형의 면적: {0}".format(area))

a = Rectangle(4, 5)
a.area_rec()
'''

'''
class Shape:
    def __init__(self, a):
        self.length = a

    def __del__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def __del__(self):
        pass

    def area_sq(self):
        area = self.length * self.length
        return area

a = Square(3)
areas = a.area_sq()

print("정사각형의 면적: {0}".format(areas))
'''



class Person:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def getGender(self):
        return "Unknown"

class Male(Person):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def getGender(self):
        return "Male"

class Female(Person):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def getGender(self):
        return "Female"


a = Male()
b = Female()
print(a.getGender())
print(b.getGender())