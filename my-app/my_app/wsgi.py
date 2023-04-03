"""
wsgi file
"""
# Set the path


import os
import sys

# Set the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=wrong-import-position
from my_app.application import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
