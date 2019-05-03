import sys
import os

args = sys.argv[1:]
permitted_args = ["--help", "postgres", "-n", "sqlite", "postgreshelp"]
print("args received", args)
illegal_args = [1 for i in args if i not in permitted_args]

show_help = False
show_win_help = False
show_linux_help = False
require_venv = True
venv_present = False
virtualenv_present = "Unchecked"
user_os = sys.platform
python_cmd = "python"

if len(args) == 0 or illegal_args or "--help" in args:
    print("ERROR: Invalid use of argument")
    show_help = True

if "postgreshelp" in args:
    if "win" in user_os:
        show_win_help = True
    else:
        show_linux_help = True

if show_help:
    help_msg = """
About:
This scripts sets up your environment for Khabar-board flask website.

Usage:
    python setupenv.py [postgres, sqlite]

    Note: It will require to setup virtual environment confirm you have venv or virtualenv
    If you want to continue any way use 'python setupenv.py -n' command

Options:
    -n : Skip Making virtualenv
    --help: Show this help

Arguments:
    postgres: Install packages for postgres setup
    sqlite: Install packages for sqlite and initialize the server.
"""
    print(help_msg)
    sys.exit(0)

elif show_win_help:
    help_msg = """
* For windows:
Download and install setupfile from https://www.postgresql.org/download/windows/

* Create a postgreql database and obtain its local url
* Add your postgresql local url of database you created earlier to environment variable named DATABASE_URL
* Make new SECRET_KEY environment variable and random string as value
* Note: Add EMAIL and EMAIL_PASSWORD environment variable with your email and password for password reset functionality!
* Finally,
###  If you are setting first time without migrate folder
      python manage.py db init
      python manage.py db migrate
      python manage.py db upgrade
      python manage.py runserver

###  If migrate folder is present
      python manage.py db upgrade
      python manage.py runserver
"""
    print(help_msg)
    sys.exit(0)

elif show_linux_help:
    help_msg = """
    * For linux:

install postgres:
    sudo apt-get install postgresql postgresql-contrib
* Now create a superuser for PostgreSQL
    sudo -u postgres createuser --superuser name_of_user
* And create a database using created user account
    sudo -u name_of_user createdb name_of_database
* You can access created database with created user by,
    psql -U name_of_user -d name_of_database
* Your postgres database url wil be something like
    postgresql://localhost/name_of_database
* Delete the secrets.json file if present in your folder.
* Set environment variables named DATABASE_URL, EMAIL, and EMAIL_PASSWORD by
      export DATABASE_URL='postgresql://localhost/name_of_database'
      export EMAIL='your_email@something.com'
      export EMAIL_PASSWORD='your password'

  * Note: EMAIL and EMAIL_PASSWORD are only required for password reset functionality!

* After that,
  if migrations folder is present
    python manage.py db upgrade
  otherwise,
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

* Finally run the application with.
    python manage.py runserver
* Website will be at http://localhost:5000 load it in your browser.
"""
    print(help_msg)
    sys.exit(0)

TYPE = args[0]

if "-n" in args:
    require_venv = False


try:
    import venv

    venv_present = True
except ImportError:
    venv_present = False
    try:
        import virtualenv

        virtualenv_present = True
    except ImportError:
        virtualenv_present = False

print("venv_present", venv_present, ":: virtualenv_present", virtualenv_present)

if not venv_present and virtualenv_present:
    if require_venv:
        print(
            "ERROR: No venv in system python",
            "SOLUTION: install 'python-venv' OR 'virtualenv' ",
        )
        continue_anyway = input("I don't recomment it: But type 'y' to continue anyway")
        if continue_anyway == "y":
            require_venv = False

    if require_venv:
        print("No virtualenv. Build failed. Exiting!")
        sys.exit(1)


def activate_venv():
    if "linux" in user_os:
        python = "venv/bin/python"
    elif "win" in user_os:
        python = "venv/scripts/python"
    else:
        print("can't detect os")
        python = "venv/bin/python"


if require_venv and venv_present:
    venv.create("./venv")
    print("Created virtualenv using venv")
    activate_venv()

elif require_venv and virtualenv_present:
    virtualenv.create_environment("./venv/")
    activate_venv()

try:
    os.rename("template_secrets.json", "secrets.json")
except FileNotFoundError:
    if "secrets.json" in os.listdir():
        pass
    else:
        print(e)

message = """
FILE:: 'secrets.json' CREATED!
NOTE:: To get email confirmation and password reset functionality in this webapp
Fill your email and password in this file.
"""

os.system(python_cmd + " -m pip install -r requirements.txt --user")

if TYPE == "sqlite":
    os.system(python_cmd + " manage.py sqlite")
    os.system(python_cmd + " start.py secrets")

elif TYPE == "postgres":
    os.system(python_cmd + " -m pip install -r requirements.txt")
    print("FINISHED!!")
    print(
        "Run 'python setupenv.py postgreshelp' ",
        "for help in setting remaining posgres environment",
    )
