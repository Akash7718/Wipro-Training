from oops_concept.college import College
from oops_concept.student import Student
from oops_concept.studentgrade import StudentGrade
from oops_concept.teacher import Teacher

cc = int(input('c code :'))
cn = input('c name:')
ci = input('city:')
rno= int(input('Roll no:'))
sn= input('Enter name:')
m1= int(input('m1:'))
m2= int(input('m2:'))
m3= int(input('m3:'))
eid = int(input('Eid:'))
tn = input('Teacher name:')
de = input('Dept Name:')
bp = float(input('Bp:'))

# project = College(ccode=cc,cname=cn,ccity=ci)
# project.welcome_message()
# project.display_college_details()

# project = Student(ccode = cc,cname=cn, ccity=ci,rno=rno,sname=sn,m1=m1,m2=m2,m3=m3 )
project = StudentGrade(ccode = cc,cname=cn, ccity=ci,rno=rno,sname=sn,m1=m1,m2=m2,m3=m3 )

project.welcome_message()
project.display_college_details()
print(f'Total : {project.calculate_total()}\nAverage:{project.calculate_average()}')
project.calculate_grade()
print(f'Result: {project.result} \t Grade: {project.grade}')


teach = Teacher(ccode=cc,cname=cn,ccity=ci,eid=eid,tn = tn, de=de,bp=bp)
print(f'Eid:{teach.empid} \t Name:{teach.tname}\t Dept:{teach.dept}')
print(f'salary:{teach.calculate_salary()}')