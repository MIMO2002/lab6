# Database Server
## Running Docker Containers
### Creating Docker Network "mynet"
    docker network create mynet
### Running PostgreSQL Server Container
    docker run --name postgres \
            -d \
            -p 5432:5432 \
            -e POSTGRES_PASSWORD=Rupp2357.! \
            -e POSTGRES_USER=admin \
            -e POSTGRES_DB=AdminDB \
            -v pg_data:/var/lib/postgresql/data \
            --network mynet \
            --restart=always \
            -it postgres
### Run pgadmin4 container
    docker pull dpage/pgadmin4

    docker run -p 5050:80 \
            -e 'PGADMIN_DEFAULT_EMAIL=chhim.bunchhun@rupp.edu.kh' \
            -e 'PGADMIN_DEFAULT_PASSWORD=Rupp2357.!' \
            -e 'PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION=True' \
            -e 'PGADMIN_CONFIG_CONSOLE_LOG_LEVEL=10' \
            --network mynet \
            --restart=always \
            --name pgadmin4 \
            -d dpage/pgadmin4

### phpMyAdmin Container
    docker run -p 8080:80 \
            --name phpmyadmin \
            -e PMA_HOST=mysql.cjyu2g4g0pi9.ap-southeast-1.rds.amazonaws.com \
            -d phpmyadmin
## Connection Setting
### Administration Tools
    phpMyAdmin: phpmyadmin: https://phpmyadmin.icetea8.click
    pgAdmin4: https://pgadmin.komroung.com
### MySQL Server
    host:mysql.cjyu2g4g0pi9.ap-southeast-1.rds.amazonaws.com
    user:admin
    password:Rupp2357.!
    port:3306
    database:smsdb
### PostgreSQL Server
    host:pgadmin.komroung.com
    user:admin
    password:Rupp2357.!
    port:5432
    database:smsdb