## Update an Existing Record
- Fetch the Record: Query the database to retrieve the record you want to update using SQLAlchemy's querying capabilities.
- Modify the Data: Modify the attributes of the retrieved object to update the data.
- Commit the Changes: `Use db.session.commit()` to save the changes to the database.

        >>> u = User.query.get(1)
        >>> u.login_name='dara1'
        >>> db.session.commit()