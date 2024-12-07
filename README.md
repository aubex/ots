![badge](https://img.shields.io/badge/coverage-88%-green)

# One-Time Secret Sharing App

A simple FastAPI application that requires a strong https deployment and allows users to securely share secrets via a one-time link. Once the secret is viewed, it is deleted from the server, ensuring that it can only be accessed once.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)
- [Test](#test)

## Features

- **One-Time Secret Sharing**: Securely share sensitive information with a unique, single-use link.
- **Fast and Lightweight**: Built with FastAPI for high performance.
- **Simple Codebase**: Easy to understand and modify.

## Prerequisites

- **Python 3.7+**

## Dependencies 

- Python 3.7+, nothing else

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/aubex/ots.git
    cd ots
    ```
2. **run the application locally**:
    ```bash
    python src/ots.py
    ```

## License

This project is open-source and available under the MIT License.

## Test
to run tests `uv` is the most easy option:
```
uv run --extra dev python -m pytest --cov=src
```