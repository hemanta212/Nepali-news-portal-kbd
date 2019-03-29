import os
import sys
from flask_final.config import PostgresProduction as Config
from flask_final import app, db

app.config.from_object(Config)
database_config = app.config['SQLALCHEMY_DATABASE_URI']

#if database is not postgres but sqlite we initialize it diffrently.
if  database_config == 'sqlite:///site.db':
    print('setting sqlite db....')
    db.create_all()
    print('done.')
    sys.exit(0)

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
