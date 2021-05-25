class Student(object):
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.__passsword = password

    def study(self, course_name):
        print("%s正在学习%s。" % (self.name, course_name))

    def __printPassword(self):
        print(self._Student__passsword)

    def test(self): 
        self._Student__printPassword()


class Teacher(object):
    __slots__ = ('_name', '_age', '_id')

    def __init__(self, name, age, id):
        self._name = name
        self._age = age
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        print('taecher age @property')
        return self._age


    @property
    def id(self):
        return self._id

    @age.setter
    def age(self, age):
        print('taecher age setter')
        self._age = age

    def foo(self):
        print("name=%s, age=%s, id=%s" %(self._name, self._age, self._id))

if __name__ == '__main__':
    stu1 = Student('Jensen', 38, 1234)
    stu1.study('Python')
#    print(stu1.__passsword)
#    stu1.__printPassword()
    stu1.test()
    
    teacher = Teacher('Eric', '28', '10001')
    teacher.age = '29'
    teacher.foo()
    print(teacher.age)
