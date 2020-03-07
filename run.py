import sys
from flask_final.config import (
    DatabaseProduction,
    SqliteProduction,
    DatabaseDebug,
    SqliteDebug,
    Secrets,
)
from flask_final import db, create_app

args = sys.argv[1:]
if "run:app" in args:
    args = sys.argv[2:]

if len(args) == 0:
    app = create_app(DatabaseProduction)
else:
    run_type = args[0]
    config_map = {
        "db-debug": DatabaseDebug,
        "sqlite-prod": SqliteProduction,
        "secrets": Secrets(),
        "db-prod": DatabaseProduction,
        "sqlite-debug": SqliteDebug,
    }
    app = create_app(config_map[run_type])

if __name__ == "__main__":
    app.run()
