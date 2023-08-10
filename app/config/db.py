from urllib.parse import quote_plus
from os.path import dirname, abspath,join

BASEDIR = abspath(dirname(dirname(__file__)))
class DB:
    def postgres_uri(self):
        dialect = 'postgresql'
        host = 'pgadmin.komroung.com'
        db = 'smsdb'
        user = 'admin'
        port = '5432'
        password = 'Rupp2357.!'
        db_uri = f'{dialect}://{user}:{quote_plus(password)}@{host}:{port}/{db}'
        return db_uri
    
    def mysql_uri(self):
        dialect = 'mysql'
        host = 'mysql.cjyu2g4g0pi9.ap-southeast-1.rds.amazonaws.com'
        db = 'smsdb'
        user = 'admin'
        port = '3306'
        password = 'Rupp2357.!'
        db_uri = f'{dialect}://{user}:{quote_plus(password)}@{host}:{port}/{db}'
        return db_uri
    
    def mysql_connector_uri(self):
        dialect = 'mysql+mysqlconnector'
        host = 'mysql.cjyu2g4g0pi9.ap-southeast-1.rds.amazonaws.com'
        db = 'smsdb'
        user = 'admin'
        port = '3306'
        password = 'Rupp2357.!'
        db_uri = f'{dialect}://{user}:{quote_plus(password)}@{host}:{port}/{db}'
        return db_uri

    def redis_uri(self):
        dialect = 'redis'
        host = ''
        db = ''
        port = ''
        password = ''
        return f'{dialect}://:{password}@{host}:{port}/{db}'

    def sqlite_uri(self):
        db_path = join(BASEDIR,'data', 'smsdb.db')
        return f'sqlite:///{db_path}'