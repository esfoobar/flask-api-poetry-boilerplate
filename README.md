# README

## Installation instructions

### MacOS

- This project uses Poetry. To install Poetry do the following
  - Make sure you have `brew` installed
  - Start a terminal
  - Install poetry using `brew install poetry`

### First Migration

- You need a postgres server up and running with the right credentials. The fastest way is to run the Docker postgres database
- Change directory to "my_api": `cd my_api`
- Run the first migration with `poetry run flask db upgrade` or `docker run --rm -it flask-api-poetry-boilerplate poetry run flask db upgrade`
  - Subsequent migrations after models changes can be run with `poetry run flask db migrate -m "added app table field"`.

## Running the application

- Start a terminal
- Navigate to the `my-api/my_api` directory
- Install the packages using `poetry install`
- Then run `poetry run flask run`

## Working with VSCode

- Open a terminal and navigate to the `my-api` directory. Open VSCode in there using `code .`
- For linting:
  - Open a terminal and enter a poetry shell with `poetry shell`. Then search for the Python location by doing `which python`.
  - Open the VSCode palette with CMD + Shit + P and search for `Python: Select Interpreter` and check if there's a Poetry interpreter with the same path or enter the path manually.
- To run the Flask server on port 5000 on macOS, you need to disable the 'AirPlay Receiver' service from System Preferences > Airdrop & Handoff.
- Black formatter is used as well as Pylint
- Testing can be started from the testing navbar for breakpoint interaction

## Working with Docker

- To run the applcation, from the root directory just type `docker-compose up`
- To run tests, run `docker run --rm -it flask-api-poetry-boilerplate poetry run pytest`

## Swagger Docs

- Once the application is running, the Swagger docs are available in [http://localhost:5000/v1.0/](http://localhost:5000/v1.0/)
- For protected routes, execute a log in and then copy the "access_token" string. Click on the "Authorize" button with the padlock and on the text field, add `Bearer <access_token>`, i.e. the text "Bearer", space and page the "access_token" string.
