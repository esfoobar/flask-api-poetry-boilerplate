# README

## Installation instructions

### MacOS

- This project uses Poetry. To install Poetry do the following
  - Make sure you have `brew` installed
  - Start a terminal
  - Install poetry using `brew install poetry`

## Running the application

- Start a terminal
- Navigate to the `my-app/my_app` directory
- Install the packages using `poetry install`
- Then run `poetry run flask run`

## Working with VSCode

- Open a terminal and navigate to the `my-app` directory. Open VSCode in there using `code .`
- For linting:
  - Open a terminal and enter a poetry shell with `poetry shell`. Then search for the Python location by doing `which python`.
  - Open the VSCode palette with CMD + Shit + P and search for `Python: Select Interpreter` and check if there's a Poetry interpreter with the same path or enter the path manually.
- To run the Flask server on port 5000 on macOS, you need to disable the 'AirPlay Receiver' service from System Preferences > Airdrop & Handoff.
- Black formatter is used as well as Pylint
- Testing can be started from the testing navbar for breakpoint interaction

## Working with Docker

- To run the applcation, from the root directory just type `docker-compose up`
- To run tests, run `docker run --rm -it flask-poetry-boilerplate poetry run pytest`
