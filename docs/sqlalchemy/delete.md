## Delete an Existing Record
- Fetch the Record: Query the database to retrieve the record you want to update using SQLAlchemy's querying capabilities.
- Delete the Record: Use the `db.session.delete()` method to mark the record for deletion.
- Commit the Changes: `Use db.session.commit()` to save the changes to the database.

        >>> u = User.query.get(1)
        >>> db.session.delete(u)
        >>> db.session.commit()