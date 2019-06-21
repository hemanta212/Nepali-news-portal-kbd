import sys
from flask_final.config import (SqliteProduction, PostgresProduction,
                                PostgresDebug, Secrets, SqliteDebug)
from flask_final import create_app
Config = sys.argv[1:]

if Config == []:
    app = create_app(SqliteProduction)

elif Config[0] == 'secrets':
    config_class = Secrets()
    app = create_app(config_class)
else:
    app = create_app(eval(Config[0]))

if __name__ == "__main__":
    app.run('0.0.0.0')
