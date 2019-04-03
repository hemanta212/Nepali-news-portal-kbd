from flask_final.config import PostgresProduction
from flask_final import db, create_app

app = create_app(PostgresProduction)

if __name__ == "__main__":
    app.run()
