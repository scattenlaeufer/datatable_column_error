# datatable_column_error

An example of an error with datatable and files with varibale numbers of
columns per row I have encountered.

## Install dependencies

To menage dependencies and virtual environments for Python, this example uses
[poetry](https://python-poetry.org/). So to run it the following software is
required:

-   [Python](https://www.python.org/) ^3.9
-   [poetry](https://python-poetry.org/) >=1.0.0

Once those are installed and this repository is cloned, all other dependencies
can be installed by running

```
poetry install
```

## Running examples

One can run the examples by just running the corresponding Python scripts.

### No problems

To run the example without errors, run

```
poetry run python3 works.py
```

This uses `good_data.tsv`.

### IOError

To run the example which throws an `IOError`, run

```
poetry run python3 throws_ioerror.py
```

This uses `bad_data.tsv`.

### ValueError

ton run the exmaple whch thorws a `ValueError`, run

```
poetry run python3 throws_valueerror.py
```

This also uses `bad_data.tsv`.
