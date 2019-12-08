# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/12/7
from ChooseCourseSystem.core import data
from ChooseCourseSystem.core import education


def choose_grade():
    print('填写教师信息')
    teacher_name = input('姓名：')
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print('您输入的有误')
        return
    print("选择班级：")
    data.print_grades()
    grade_name = input("班级名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("班级选择错误")
        return
    teacher.choose_grade(grade)
    education.Grade.sign_in_teacher(grade, teacher)
    data.update_teacher(teacher)
    data.update_grade(grade)


def modify_score():
    print('选择老师')
    data.print_teachers()
    teacher_name = input('姓名：')
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("老师选择错误")
        return
    print('选择学生')
    data.print_students()
    student_name = input('学生名：')
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return
    score = input("请输入分数：")
    if not score.isdigit() or 0 > int(score) or int(score) > 120:
        print("输入分数不正确")
        return
    teacher.modify_score(teacher, student, score)
    data.update_teacher(teacher)
    data.update_student(student)
    data.update_grade(teacher.grade)
    print("%s 的成绩修改为: %s" % (student.name, data.get_student(student_name).score))


def show_students():
    print("选择老师：")
    data.print_teachers()
    teacher_name = input("老师名：")
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("老师选择错误")
        return

    teacher.show_students()


def show_teacher():
    print("选择老师：")
    data.print_teachers()
    teacher_name = input("老师名：")
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("老师选择错误")
        return
    teacher.show_info()



def run():
    print("教师视图：")
    print("=" * 20)
    while True:
        print("1.选择班级\n2.查看学生\n3.修改成绩\n4.查看教师\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            choose_grade()
        elif res == "2":
            show_students()
        elif res == "3":
            modify_score()
        elif res == "4":
            show_teacher()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")


if __name__ == "__main__":
    run()
