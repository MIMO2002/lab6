from app.models import *

def load_auth():
    insert_menu()
    insert_sub_menu()
    insert_right()
    insert_profile()
    insert_profile_access_right()
    
def load_student():
    insert_gender()
    insert_student()

def insert_gender():
    genders = [
        Gender(name_latin='Female',acronym='F'),\
        Gender(name_latin='Male',acronym='M')
    ]
    db.session.add_all(genders)
    db.session.commit()
    
def insert_student():
    students = [
        Student(first_name='Sok', last_name='Dara', gender_id=2, email='dara@rupp.edu.kh',age=20),\
        Student(first_name='Keo', last_name='Pisey', gender_id=1, email='pisey@rupp.edu.kh',age=20),\
        Student(first_name='Prom', last_name='Sitha', gender_id=1, email='sitha@rupp.edu.kh',age=20),\
        Student(first_name='Ros', last_name='Boran', gender_id=2, email='boran@rupp.edu.kh',age=20)
    ]
    db.session.add_all(students)
    db.session.commit()
    
def insert_menu():
    menus = [
        Menu(name_latin='Setting',order=1),\
        Menu(name_latin='Student',order=2)
    ]
    db.session.add_all(menus)
    db.session.commit()
    
def insert_sub_menu():
    sub_menus = [
        SubMenu(menu_id=1,name_latin='User',order=1,end_point='e01'),\
        SubMenu(menu_id=1,name_latin='Password',order=2,end_point='e02'),\
        SubMenu(menu_id=2,name_latin='Dashboard',order=1,end_point='e03'),\
        SubMenu(menu_id=2,name_latin='Course',order=2,end_point='e04')
    ]
    db.session.add_all(sub_menus)
    db.session.commit()
    
def insert_profile():
    profiles = [
        Profile(acronym='AD',name_latin='Administrator'),\
        Profile(acronym='ST',name_latin='Student'),\
        Profile(acronym='TE',name_latin='Teacher')
    ]
    db.session.add_all(profiles)
    db.session.commit()

def insert_right():
    rights = [
        Right(acronym='R', description='Read Only'),\
        Right(acronym='W', description='Read and Write Only'),\
        Right(acronym='F', description='Read and Write and Delete')
    ]
    db.session.add_all(rights)
    db.session.commit()

def insert_profile_access_right():
    profile_access_rights = [
        ProfileAccessRight(profile_id=1,sub_menu_id=1,right_id=3),\
        ProfileAccessRight(profile_id=1,sub_menu_id=2,right_id=3),\
        ProfileAccessRight(profile_id=1,sub_menu_id=3,right_id=3),\
        ProfileAccessRight(profile_id=1,sub_menu_id=4,right_id=3),\
        ProfileAccessRight(profile_id=2,sub_menu_id=2,right_id=1),\
        ProfileAccessRight(profile_id=2,sub_menu_id=3,right_id=1),\
        ProfileAccessRight(profile_id=3,sub_menu_id=2,right_id=2),\
        ProfileAccessRight(profile_id=3,sub_menu_id=3,right_id=2)
    ]
    db.session.add_all(profile_access_rights)
    db.session.commit()

def insert_user():
    users = [
        User(login_name='dara',password='123',profile_id=1,student_id=1,status=1),\
        User(login_name='pisey',password='123',profile_id=1,student_id=2,status=1),\
        User(login_name='sitha',password='123',profile_id=2,student_id=3,status=1),\
        User(login_name='boran',password='123',profile_id=3,student_id=4,status=1)
    ]
    db.session.add_all(users)
    db.session.commit()