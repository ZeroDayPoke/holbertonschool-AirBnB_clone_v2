# Holberton School - AirBnB Clone v2

This repository contains the second version of the AirBnB clone project, which is part of the Holberton School curriculum. In this project, you will learn about the Python programming language, specifically about data models, MySQL, web flask, and more.

## Synopsis

This project covers:

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and implement a SQL script
- How to use MySQL
- What is an ORM
- How to map a Python Class to a MySQL table
- How to handle 2 different storage engines with the same codebase
- How to use environment variables

## File Descriptions

### Directories and Important File(s)

- `console.py`: This file is the entry point of our command interpreter.
- `models/`: This directory contains all classes used for the entire project. A class, called `model`, is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
- `tests/`: This directory contains all unit tests for all functions and classes.
- `web_static/`: This directory contains static HTML and CSS files, from the first portion of this project (one could consider it v1.5 of the HBNB clone).
- `web_flask/`: Contains files associated with Flask app prototype implementation curriculum, including the associated python routing files, as well as, the static HTML and CSS (second portion of the project, effectively equivalent to v2.0 in the nomenclature)

### Tests

#### Console

- `tests/test_console.py`: This file contains the unit test module for our built in console.py.

#### Models

- `tests/test_models/test_base_model.py`: This file contains the unit tests for the base model class.
- `tests/test_models/test_user.py`: This file contains the unit tests for the user class.
- `tests/test_models/test_place.py`: This file contains the unit tests for the place class.
- `tests/test_models/test_review.py`: This file contains the unit tests for the review class.
- `tests/test_models/test_amenity.py`: This file contains the unit tests for the amenity class.
- `tests/test_models/test_city.py`: This file contains the unit tests for the city class.
- `tests/test_models/test_state.py`: This file contains the unit tests for the state class.

#### Engine

- `tests/test_models/test_engine/test_db_storage.py`: This file contains the unit tests for the SQLAlchemy (ORM) database engine implementation.
- `tests/test_models/test_engine/test_file_storage.py`: This file contains the unit tests for the version 1 file storage mode implementation.

## Authors

- **Colan Worstell** - [ColanWorstellProgramming](https://github.com/ColanWorstellProgramming)
- **Chris Stamper** - [ZeroDayPoke](https://github.com/ZeroDayPoke)

## Contributors

As I recall, we originally were instructed to fork a few of the HBNB Clone versions from existing code bases, so there are almost certainly additional contributors/people_to_be_acknowledged :D

## TODO

FINISH README
