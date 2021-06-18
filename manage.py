import os

from flask_final.config import Debug, Secrets
from flask_final import db, create_app

is_env_var_set = os.getenv("SQLALCHEMY_DATABASE_URI")
if not is_env_var_set:
    config = Secrets()
else:
    config = Debug

# Support for relative sqlite URIs
if config.SQLALCHEMY_DATABASE_URI == "sqlite:///site.db":
    temp_app = create_app(config)
    config.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        temp_app.root_path, "site.db"
    )

app = create_app(config)

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
