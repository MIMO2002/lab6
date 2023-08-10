## Flask-SQLALCHEMY INSTALLATION
### Installing the packages
    pip install flask-sqlalchemy
#### PostgreSQL Driver
    pip install psycopg2
    pip install psycopg2-binary
#### MySQL Driver
##### mysqlclient
    # MAC OS
    brew install mysql pkg-config
    # Debian/Ubuntu
    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
    # Red Hat / CentOS
    sudo yum install python3-devel mysql-devel
    # install mysqlclient
    pip install mysqlclient
    #mysql://<username>:<password>@<host>[:<port>]/<dbname>
##### MySQL-Connector
    pip install mysql-connector-python
    #mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
