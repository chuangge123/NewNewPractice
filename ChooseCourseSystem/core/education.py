# -*-coding = utf-8-*-
# __author:"NGLS Chuang"
# @time:2019/12/4 16:04
class Education(object):  # 建立逻辑关系。
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class School(Education, object):
    def __init__(self, name, address):
        # super(School, self).__init__(name)
        Education.__init__(self, name)
        self.address = address
        self.teachers = []
        self.students = []
        self.courses = []
        self.grades = []
        print("%s校区 create successful" % name)

    def sign_in(self, student):  # 学员注册
        self.students.append(student)
        print("欢迎学员%s加入到%s" % (student.name, self.name))

    def leave_school(self, student):  # 学员退学
        self.students.remove(student)
        print("很遗憾学员%s退出%s" % (student.name, self.name))

    def creat_course(self, name, cycle, price):
        course = Course(name, cycle, price)
        self.courses.append(course)
        print("课程%s创建成功" % name)
        return course

    def creat_teacher(self, name, ):
        teacher = Teacher(name, self)
        self.teachers.append(teacher)
        print("老师%s创建成功" % name)
        return teacher

    def deplom_teacher(self, teacher):
        self.teachers.append(teacher)
        print('老师%s雇佣成功,恭喜%s校区' % (teacher.name, self.name))

    def fire_teacher(self, teacher, ):
        self.teachers.remove(teacher)
        print('you are fire by %s 教师%s' % (self.name, teacher.name))

    def create_grade(self, name, course):
        grade = Grade(name, course)
        self.grades.append(grade)
        print('班级%s创建成功' % grade.name)
        return grade


class Grade(Education, object):  # 创建班级
    def __init__(self, name, course):
        Education.__init__(self, name)
        self.teachers = []
        self.course = course
        self.students = []

    def sign_in_student(self, student):  # 学员注册，并将学员添加到班级列表。
        self.students.append(student)
        print('%s同学，您的班级为%s' % (student.name, self.name))

    def sign_in_teacher(self, teacher):  # 学员注册，并将学员添加到班级列表。
        self.teachers.append(teacher)
        teacher.grade = self.name
        print('%s教师，您将为%s班级上课' % (teacher.name, self.name))

    def leave_grade_student(self, student):
        self.students.remove(student)
        print('%s同学，您已经离开了%s' % (student.name, self.name))

    def leave_grade_teacher(self, teacher):
        self.teachers.remove(teacher)
        print('%s教师，您已经离开了%s' % (teacher.name, self.name))

    def show_info(self):
        print('班级：%s,老师：%s,课程：%s,学生：%s' % (self.name, self.teachers, self.course, self.students))


class Student(Education, object):  # 创建学员时，选择学校，关联班级
    def __init__(self, name, school, grade, score=0):
        Education.__init__(self, name)
        self.school = None
        self.grade = None
        self.score = score
        self.tuition = 0
        self.choose_school(school)
        self.choose_grade(grade)

    def choose_school(self, school):  # 接受一个学校，不管时什么学校，里面有这个方法就调用即可
        if self.school != None:
            self.school.leave_school()
        school.sign_in(self)  # 学生调用这个办法 将自己（学生）传进当参数
        self.school = school

    def choose_grade(self, grade):
        if self.grade != None:
            self.grade.leave_grade_student()
        grade.sign_in_student(self)
        self.grade = grade

    def pay_tuition(self, money):
        self.tuition += money

    def show_student_info(self):
        print("student:name: %s\t school:%s\t grade:%s\t score:%s\t tuition:%s" %
              (self.name, self.school, self.grade, self.score, self.tuition))


class Teacher(Education, object):
    def __init__(self, name, school):
        Education.__init__(self, name)
        self.school = None
        self.choose_school(school)
        self.grade = None

    def choose_school(self, school):
        if self.school != None:
            self.school.fire_teacher()
        school.deplom_teacher(self)
        self.school = school

    def choose_grade(self, grade):
        if self.grade != None:
            self.grade.leave_grade_teacher()
        grade.sign_in_teacher(self)
        self.grade = grade

    def check_students(self, grade):
        for student in grade.students:
            student.show_student_info()

    def modify_score(self, student, score):
        student.score = score

    def show_students(self):
        if self.grade != None:
            for student in self.grade.students:
                student.show_student_info()
        else:
            print("请选择班级")

    def show_info(self):
        print("teacher:name: %s\t school:%s\t grade:%s" %
              (self.name, self.school, self.grade))


class Course(Education, object):
    def __init__(self, name, cycle, price):
        Education.__init__(self, name)
        self.cycle = cycle
        self.price = price


if __name__ == '__main__':
    school = School("航天人才大学", "北京")
    teacher = school.creat_teacher('孙闯')
    print(teacher.school)
    course = school.creat_course("崔牛B", "1年", "9998")
    grade = school.create_grade("催牛脱产A班", course)
    grade.sign_in_teacher(teacher)
    student = Student("小齐", school, grade)
    teacher.check_students(grade)
    print(teacher.grade)
