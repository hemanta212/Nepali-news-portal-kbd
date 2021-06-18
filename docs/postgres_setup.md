## Setup with postgres database

  * [Unix setup](#unix_pg)
  * [Windows setup (WIP)](#windows_pg)

### Run using postgres database. <a id='pg'></a>
To run the project on posgres database you need to install postgresql 10+ in your system

#### Linux setup: <a id='unix_pg'></a>
1. Install postgres:

```
sudo apt-get install postgresql postgresql-contrib
```

2. Now create a superuser for PostgreSQL

```
sudo -u postgres createuser --superuser name_of_user
```

3. And create a database using created user account

```
sudo -u name_of_user createdb name_of_database
```

4. You can access created database with created user by,

```
psql -U name_of_user -d name_of_database
```

5. Your postgres database url wil be something like

```
postgresql://localhost/name_of_database
```
Or, if you have setup password then,

```
postgresql://user_name:password/localhost/name_of_database
```

7. Now take this url and go back to [this section in Main Readme file](../README.md#setting up-the-postgres-databse)

```
#### Windows setup: <a id='windows_pg'></a>
Download and install [official site](https://www.postgresql.org/download/windows/)

1. Create a postgreql database and obtain its local url
