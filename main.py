from httpstatus.http_status import HTTPStatus

print(HTTPStatus.OK)

status = HTTPStatus.NOT_FOUND
print(status.status)
print(status.name)         
print(status.description)

success_codes = HTTPStatus.success_responses()
print(success_codes)

status = HTTPStatus.from_status(500)
print(status)