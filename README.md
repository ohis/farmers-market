# Farmer's Market &middot; [![CircleCI](https://img.shields.io/circleci/project/github/JHart9/farmers-market.svg?style=flat-square)](https://circleci.com/gh/JHart9/farmers-market/)

> Marketplace that runs in the console with set items for sale that can be added, removed, and have discounts applied to them.

- [Running](#running)
    - [Docker](#docker)
    - [Native](#native)
- [Usage](#usage)
- [Tests](#tests)

## Running

### Docker

With [Docker](https://www.docker.com/get-docker) installed, run:

```sh
> docker build -t farmers-market .
> docker run -it farmers-market
```

### Native

Run the following commands with [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed:

```sh
> pip install -r requirements.txt
> python app.py
```

## Usage

While running the marketplace, the following commands are:
- `add` - Add items by code name to the basket, use `stop` to exit the adding prompt or continue entering items.
- `remove` - Remote items by code from the basket, use `stop` to exit this or keep removing items.
- `inv` - Check the inventory of the basket. Can be used in the middle of `add` and `remove`.
- `exit` - When not adding or removing items, exits the marketplace completely and leaves the app.

## Tests

Uses [pytest](https://docs.pytest.org). Intall and run `pytest`, or `pytest -v` for more verbose output.