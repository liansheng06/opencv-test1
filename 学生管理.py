class Person:
    #人类，体现封装
    def __init__(self, name, age, id_number):#所有子类都有的共同属性
        self._name = name  # 保护属性
        self._age = age
        self._id = id_number
    
    def get_info(self):
        #获取基本信息，体现多态的基础
        return f"姓名: {self._name}, 年龄: {self._age}, ID: {self._id}"
    
    def work(self):
        #工作方法，会在子类中重写
        pass

class Student(Person):
    #学生类，体现继承
    def __init__(self, name, age, id_number, grade, major):
        super().__init__(name, age, id_number)#调用父类构造方法
        self._grade = grade
        self._major = major
        self._courses = []
    
    def get_info(self):
        #重写父类方法，体现多态
        base_info = super().get_info()
        return f"{base_info}, 年级: {self._grade}, 专业: {self._major}"
    
    def work(self):
        #重写方法
        return f"{self._name}正在学习"
    
    def add_course(self, course):
        self._courses.append(course)
    
    def get_courses(self):
        return self._courses

class Teacher(Person):
    #教师类，体现继承
    def __init__(self, name, age, id_number, department):
        super().__init__(name, age, id_number)
        self._department = department
        self._teaching_courses = []
    
    def get_info(self):
        #重写父类方法，体现多态
        base_info = super().get_info()
        return f"{base_info}, 部门: {self._department}"
    
    def work(self):
        #重写方法
        return f"{self._name}正在教课"
    
    def assign_course(self, course):
        self._teaching_courses.append(course)
    
    def get_teaching_courses(self):
        return self._teaching_courses

class Course:
    #课程类
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
    
    def get_course_info(self):
        return f"名称: {self.name}, 学分: {self.credit}"

def main():
    # 创建课程
    math_course = Course("高等数学", 4)
    python_course = Course("Python", 3)
    english_course = Course("大学英语", 2)
    
    # 创建学生
    student1 = Student("张三", 20, "001", "大三", "计算机科学")
    student2 = Student("李四", 19, "002", "大二", "软件工程")
    
    # 为学生添加课程
    student1.add_course(math_course)
    student1.add_course(python_course)
    student2.add_course(english_course)
    student2.add_course(python_course)
    
    # 创建教师
    teacher1 = Teacher("王教授", 45, "001", "计算机学院")
    teacher2 = Teacher("李老师", 35, "002", "外语学院")
    
    # 为教师分配课程
    teacher1.assign_course(math_course)
    teacher1.assign_course(python_course)
    teacher2.assign_course(english_course)
    
    # 演示多态
    people = [student1, student2, teacher1, teacher2]
    for person in people:
        print(f"{person._name}: {person.work()}")  #同样的方法，不同的行为,体现多态

if __name__ == "__main__":
    main()