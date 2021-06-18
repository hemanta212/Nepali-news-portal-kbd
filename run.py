import os
import sys
from flask_final.config import Prod, Debug, Secrets
from flask_final import create_app

app = None
args = sys.argv[1:]
if "run:app" in args:
    args = sys.argv[2:]

if len(args) == 0 or args[0] == "prod":
    app = create_app(Prod)
elif args[0] == "debug":
    app = create_app(Debug)
else:
    print(f"Usage: run.py [prod/debug]. Unrecognized argument {args[0]}")

is_env_var_set = os.getenv("SQLALCHEMY_DATABASE_URI")
if not is_env_var_set:
    print(
        ":: No environment variables set!\n"
        ":: Falling back to Debug Mode and reading secrets from file"
    )
    app = create_app(Secrets())

if __name__ == "__main__":
    app.run()
