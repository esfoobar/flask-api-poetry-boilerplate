# Set the path
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from my_app.application import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
