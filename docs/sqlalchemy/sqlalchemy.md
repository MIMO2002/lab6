## How to test sqlalchmey(db) in interactive shell
- Enter into interactive shell:
    
        (venv)->Python
        >>> from app import db, create_app
        >>> app=create_app()
        >>> db.app=app
        >>> app.app_context().push()
        >>> db.create_all()
- import models, example:

        >>> from app.models.student import Student
- Run query

        >>> Student.query.all()

        