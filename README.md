# Rule Engine Using AST

This project implements a rule engine using Abstract Syntax Trees (AST) to determine user eligibility based on dynamic rules.

## Features

- Create rules from strings and convert them into ASTs
- Combine multiple rules into a single AST
- Evaluate user data against the AST
- Store and load rules from a MongoDB database

## Requirements

- Python 3.x
- MongoDB
- Install dependencies using `pip install -r requirements.txt`

## Running the Application

1. Start MongoDB.
2. Run the main script: `python main.py`.

## Running Tests

Run unit tests using:

```bash
python -m unittest discover
```
