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