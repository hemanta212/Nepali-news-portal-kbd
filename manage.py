import os
import sys
from flask_final.config import PostgresProduction, SqliteProduction
from flask_final import db, create_app

arg = sys.argv[1:]
app = create_app(PostgresProduction)

#if database is not postgres but sqlite we initialize it diffrently.
if 'sqlite' in arg:
    app = create_app(SqliteProduction)
    print('setting sqlite db....')
    with app.app_context():
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
