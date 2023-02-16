# README

## Installation instructions

### MacOS

- This project uses Poetry. To install Poetry do the following
  - Make sure you have `brew` installed
  - Start a terminal
  - Install poetry using `brew install poetry`

## Running the application

- Start a terminal
- Copy the `.flaskenv.sample` to `.flaskenv`
- Then run `poetry run flask run`

## Working with VSCode

- For linting, open a terminal and enter a poetry shell with `poetry shell`. Then search for the Python location by doing `which python`. Open the VSCode palette with CMD + Shit + P and search for `Python: Select Interpreter` and check if there's a Poetry interpreter with the same path or enter the path manually.
- To run the Flask server on port 5000 on macOS, you need to disable the 'AirPlay Receiver' service from System Preferences -> Sharing.
- Black formatter is used as well as Pylint
