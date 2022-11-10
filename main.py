from flask import app
from flask.cli import run_command
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
