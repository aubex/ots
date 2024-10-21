# One-Time Secret Sharing App

A simple FastAPI application that requires a strong https deployment and allows users to securely share secrets via a one-time link. Once the secret is viewed, it is deleted from the server, ensuring that it can only be accessed once.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Features

- **One-Time Secret Sharing**: Securely share sensitive information with a unique, single-use link.
- **Fast and Lightweight**: Built with FastAPI for high performance.
- **Simple Codebase**: Easy to understand and modify.

## Prerequisites

- **Python 3.12 or higher**
- **uv**

## Dependencies 

- **fastAPI**
- **Jinja2**

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/aubex/ots.git
    cd ots
    ```
2. **run the application locally**:
    ```bash
    uv run python -m uvicorn --app-dir src/ots main:app
    ```

## License

This project is open-source and available under the MIT License.