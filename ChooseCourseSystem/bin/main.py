# -*-coding = utf-8-*-
# __author:"NGLS Chuang"
# @time:2019/12/4 15:33
from ChooseCourseSystem.core import school_view, student_view, teacher_view


def main():
    print('前面登录省略了，在这个选择您的身份')
    print('请选择角色:1 学校 2教师 3 学生')
    choose = int(input('请选择：'))
    if choose == 1:
        school_view.run()
    elif choose == 2:
        student_view.run()
    elif choose == 3:
        teacher_view.run()
    else:
        print('说人话')


main()
