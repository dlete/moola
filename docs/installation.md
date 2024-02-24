### Create a dedicated virtual environment.
```shell
python3 -m venv </path/to/new/virtual/environment>
```


### Activate the virtual environment
```shell
source </path/to/new/virtual/environment>/bin/activate
```


### Upgrade the `pip` module.
Once you are within the Python environment
```shell
pip install --upgrade pip
```


### Install Python packages.
Before installing the Python packages, you need to install these Ubuntu packages
```shell
sudo apt-get install python3-dev libmysqlclient-dev
```
Note: you  need to have `libmysqlclient-dev` in the OS in order to install the Python package `mysqlclient`. And the Ubuntu package `libmysqlclient-dev` does require `python3-dev`.


This must be done within the Python virtual environment.
```shell
pip install -r requirements.txt
```

Note, for MySQL, use the connector `mysqlclient`, it is the [Django recommended library](https://stackoverflow.com/questions/4960048/how-can-i-connect-to-mysql-in-python-3-on-windows)

Ensure the packages have been correctly installed. To check, try to import every module like this:
```shell
python -c "import Django, mysqlclient"
```


# Install the database server

### Install Ubuntu packages
Unless it has not been done already, install these 
```shell
sudo apt-get install python3-dev libmysqlclient-dev
```
Note: you  need to have `libmysqlclient-dev` in the OS in order to install the Python package `mysqlclient`. And the Ubuntu package `libmysqlclient-dev` does require `python3-dev`.


## If you are to use MySQL

Install MySQL in your OS.
```shell
sudo apt-get install mysql-server
```


## If you are to use MariaDB
Check instructions in: [How To Use MySQL or MariaDB with your Django Application on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04). We are also using the package `libmysqlclient-dev` for MariaDB, I have it installed and does the trick. Cannot install `libmariadbclient-dev`, does not exist in Ubuntu 16.04

### If you are to have a cluster
Follow instructions in: [How To Configure a Galera Cluster with MariaDB 10.1 on Ubuntu 16.04 Servers](https://www.digitalocean.com/community/tutorials/how-to-configure-a-galera-cluster-with-mariadb-10-1-on-ubuntu-16-04-servers)


## Common for either MySQL or MariaDB
Log to the database
```shell
mysql -u root -p
```

Create database, user and grant permissions:

```SQL
CREATE DATABASE moola CHARACTER SET UTF8;
CREATE USER 'moola'@'localhost' IDENTIFIED BY 'Friday13';
GRANT ALL PRIVILEGES ON moola.* TO 'moola'@'localhost';
FLUSH PRIVILEGES;
```

and then, for the Django tests:
```SQL
GRANT ALL PRIVILEGES ON test_moola.* to 'moola'@'localhost';
```


Check the grants for a given user with:
```SQL
show grants for 'moola'@'localhost';
```