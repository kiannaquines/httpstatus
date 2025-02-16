# HTTP Status API

## Overview

The HTTP Status API is a Python package that provides an enumeration of HTTP status codes along with their names and descriptions. This package can be used to handle and interpret HTTP status codes in a more readable and maintainable way.

This documentation provides an overview of the package, installation instructions, usage examples, and contribution guidelines.

## Features

- Enumeration of all standard HTTP status codes.
- Descriptive names and explanations for each status code.
- Methods to filter status codes by their categories (informational, success, redirection, client error, server error).
- Utility methods to retrieve status codes by their integer value.

## Installation Guide

To install the package, use the following command:

```sh
pip install .
```

## Usage

```python
from httpstatus.http_status import HTTPStatus

# Accessing an HTTP status code
print(HTTPStatus.OK)  # Output: 200 OK: Standard response for successful HTTP requests.

# Getting the status code, name, and description
status = HTTPStatus.NOT_FOUND
print(status.status)       # Output: 404
print(status.name)         # Output: Not Found
print(status.description)  # Output: The requested resource could not be found but may be available in the future.

# Filtering status codes by category
success_codes = HTTPStatus.success_responses()
print(success_codes)  # Output: List of all 2xx success status codes

# Retrieving status by code
status = HTTPStatus.from_status(500)
print(status)  # Output: 500 Internal Server Error: A generic error message, given when an unexpected condition was encountered.
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on the GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Kian Naquines - kjgnaquines@gmail.com

This documentation provides an overview of the package, installation instructions, usage examples, and contribution guidelines.
