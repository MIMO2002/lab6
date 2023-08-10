from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), unique=True, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    last_login_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    student = db.relationship('Student', back_populates='user', uselist=False)
    profile = db.relationship('Profile', back_populates='users')
    
    def __repr__(self):
        return f'User ({self.id},{self.login_name},{self.password},{self.profile_id},{self.student_id},{self.status})'
    
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), unique=True, nullable=False)
    order = db.Column(db.Integer, unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    sub_menus = db.relationship('SubMenu', back_populates='menu')
    
    def __repr__(self):
        return f'Menu ({self.id},{self.name_latin},{self.order})'

# Association Object
class ProfileAccessRight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    sub_menu_id = db.Column(db.Integer, db.ForeignKey('sub_menu.id'))
    right_id = db.Column(db.Integer, db.ForeignKey('right.id'))
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    profile = db.relationship('Profile', back_populates='profile_access_rights')
    sub_menu = db.relationship('SubMenu', back_populates='profile_access_rights')
    right = db.relationship('Right', back_populates='profile_access_rights')
    
class SubMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    name_latin = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer,nullable=False)
    end_point = db.Column(db.String(200),unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    menu = db.relationship('Menu', back_populates='sub_menus')
    profile_access_rights = db.relationship('ProfileAccessRight', back_populates='sub_menu')
    
    def __repr__(self):
        return f'SubMenu ({self.id},{self.menu_id},{self.name_latin},{self.order},{self.end_point})'
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(10), unique=True, nullable=False)
    name_latin = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    users = db.relationship('User', back_populates='profile')
    profile_access_rights = db.relationship('ProfileAccessRight', back_populates='profile')
    
    def __repr__(self):
        return f'Profile ({self.id},{self.acronym},{self.name_latin})'

class Right(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(2), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    profile_access_rights = db.relationship('ProfileAccessRight', back_populates='right')
    
    def __repr__(self):
        return f'Right ({self.id},{self.acronym},{self.description})'
