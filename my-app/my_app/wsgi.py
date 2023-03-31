# Set the path
import os, sys  # noqa

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from my_app.application import create_app  # noqa

app = create_app()

if __name__ == "__main__":
    app.run()
