## INSERT DATA INTO TABLE
#### 1. Insert a new record into a table
- Option 1

        >>> from app.models import Gender
        >>> g1=Gender()
        >>> g1.name_latin = 'Male'
        >>> g1.acronym='M'
        >>> db.session.add(g1)
        >>> db.session.commit()
- Option 2

        >>> from app.models.student import Gender
        >>> g2 = Gender(name_latin='Female', acronym='F')
        >>> db.session.add(g2)
        >>> db.session.commit()
#### 2 Insert multiple rows into a table
##### Option 1: session.bulk_insert_mappings()

        >>> from app.models import Student
        >>> data = [{'first_name':'Dara1','last_name':'Sok','gender_id':1,'email':'sok.dara@rupp.edu.kh','age':35},{'first_name':'Dara2','last_name':'Sok','gender_id':1,'email':'sok.dara2@rupp.edu.kh','age':40}]
        >>> db.session.bulk_insert_mappings(Student,data)
        >>> db.session.commit()
##### Option 2:session.add_all()
        
        >>> students = [Student(first_name='Sok1',last_name='Pisey',gender_id=2,email='sok1@rupp.edu.kh',age=24), Student(first_name='Sok2',last_name='Pisey',gender_id=2,email='sok2@rupp.edu.kh',age=25)]
        >>> db.session.add_all(students)
        >>> db.session.commit()

### Insert some more seeding data
#### Insert profiles
        >>> from app.models import Profile
        >>> profiles = [Profile(acronym='AD',name_latin='Administrator'),Profile(acronym='ST',name_latin='Student')]
        >>> db.session.add_all(profiles)
        >>> db.session.commit()
#### Insert Right
        >>> from app.models import Right
        >>> rights = [Right(acronym='R',description='Read Only'),Right(acronym='W',description='Read and Write Only'),Right(acronym='F',description='Read, Write and Delete')]
        >>> db.session.add_all(rights)
        >>> db.session.commit()
#### Insert Menu
        >>> from app.models import Menu
        >>> menus=[Menu(name_latin='Setting',order=1),Menu(name_latin='Student',order=2)]
        >>> db.session.add_all(menus)
        >>> db.session.commit()
#### 