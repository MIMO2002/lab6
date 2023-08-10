from flask import Blueprint, render_template
from .login import login_bp
from app.models import *
auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')
auth_bp.register_blueprint(login_bp)

@auth_bp.route('/')
def admin_home():
    return 'This is admin'

@auth_bp.route('/users')
def users_list():
    users = db.session.query(User,Student,Gender)\
        .join(Student, User.student_id==Student.id)\
        .join(Gender, Student.gender_id==Gender.id)\
        .with_entities(Student.first_name,Student.last_name,User.login_name,Gender.acronym).all()
        
    return render_template('auth/users.html',users=users)
    