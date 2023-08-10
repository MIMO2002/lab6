FROM amazonlinux:2

# Install system dependencies
RUN amazon-linux-extras install epel -y && \
    yum update -y && \
    yum install -y python3 python3-pip tzdata mysql-devel postgresql-devel gcc python3-devel && \
    ln -fs /usr/share/zoneinfo/Asia/Phnom_Penh /etc/localtime && \
    rm -rf /var/cache/yum && \
    yum clean all

# Set Python version
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV mysql_config /usr/bin/mysql_config
ENV PG_CONFIG /usr/pgsql-13/bin/pg_config

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Command to run the application
CMD gunicorn --workers=4 -b 0.0.0.0:8080 'run:app'
