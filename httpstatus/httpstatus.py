from enum import Enum
from dataclasses import dataclass
from typing import List

@dataclass
class HTTPStatusMixins:
    """
    A dataclass that contains the attributes of an HTTP status code.
    - `status`: The integer value of the HTTP status code.
    - `name`: The name of the HTTP status code.
    - `description`: A brief description of the status code.
    """
    status: int
    name: str
    description: str

class HTTPStatus(HTTPStatusMixins, Enum):
    """
    A Python Enum class representing HTTP status codes along with their name and descriptions.
    Each enum member has three attributes:
    - `status`: The integer value of the HTTP status code.
    - `name`: The name of the HTTP status code.
    - `description`: A brief description of the status code.

    Source: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    Author: Kian Jearard G. Naquines
    """

    # 1xx Informational Response
    CONTINUE = (100, "Continue", "The server has received the request headers and the client should proceed to send the request body.")
    SWITCHING_PROTOCOLS = (101, "Switching Protocols", "The requester has asked the server to switch protocols.")
    PROCESSING = (102, "Processing", "This code indicates that the server has received and is processing the request, but no response is available yet.")
    EARLY_HINTS = (103, "Early Hints", "Used to return some response headers before the final HTTP message.")

    # 2xx Success
    OK = (200, "OK", "Standard response for successful HTTP requests.")
    CREATED = (201, "Created", "The request has been fulfilled, resulting in the creation of a new resource.")
    ACCEPTED = (202, "Accepted", "The request has been accepted for processing, but the processing has not been completed.")
    NON_AUTHORITATIVE_INFORMATION = (203, "Non-Authoritative Information", "The server is a transforming proxy that received a 200 OK from its origin, but is returning a modified version of the origin's response.")
    NO_CONTENT = (204, "No Content", "The server successfully processed the request and is not returning any content.")
    RESET_CONTENT = (205, "Reset Content", "The server successfully processed the request, asks that the requester reset its document view, and is not returning any content.")
    PARTIAL_CONTENT = (206, "Partial Content", "The server is delivering only part of the resource (byte serving) due to a range header sent by the client.")
    MULTI_STATUS = (207, "Multi-Status", "The message body that follows is by default an XML message and can contain a number of separate response codes, depending on how many sub-requests were made.")
    ALREADY_REPORTED = (208, "Already Reported", "The members of a DAV binding have already been enumerated in a preceding part of the (multistatus) response, and are not being included again.")
    IM_USED = (226, "IM Used", "The server has fulfilled a request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.")

    # 3xx Redirection
    MULTIPLE_CHOICES = (300, "Multiple Choices", "Indicates multiple options for the resource from which the client may choose.")
    MOVED_PERMANENTLY = (301, "Moved Permanently", "This and all future requests should be directed to the given URI.")
    FOUND = (302, "Found", "The resource was found, but at a different URI.")
    SEE_OTHER = (303, "See Other", "The response to the request can be found under another URI using a GET method.")
    NOT_MODIFIED = (304, "Not Modified", "Indicates that the resource has not been modified since the version specified by the request headers.")
    USE_PROXY = (305, "Use Proxy", "The requested resource is available only through a proxy, the address for which is provided in the response.")
    TEMPORARY_REDIRECT = (307, "Temporary Redirect", "The request should be repeated with another URI, but future requests should still use the original URI.")
    PERMANENT_REDIRECT = (308, "Permanent Redirect", "The request and all future requests should be repeated using another URI.")

    # 4xx Client Errors
    BAD_REQUEST = (400, "Bad Request", "The server cannot or will not process the request due to an apparent client error.")
    UNAUTHORIZED = (401, "Unauthorized", "Authentication is required and has failed or has not yet been provided.")
    PAYMENT_REQUIRED = (402, "Payment Required", "Reserved for future use.")
    FORBIDDEN = (403, "Forbidden", "The request was valid, but the server is refusing action.")
    NOT_FOUND = (404, "Not Found", "The requested resource could not be found but may be available in the future.")
    METHOD_NOT_ALLOWED = (405, "Method Not Allowed", "A request method is not supported for the requested resource.")
    NOT_ACCEPTABLE = (406, "Not Acceptable", "The requested resource is capable of generating only content not acceptable according to the Accept headers sent in the request.")
    PROXY_AUTHENTICATION_REQUIRED = (407, "Proxy Authentication Required", "The client must first authenticate itself with the proxy.")
    REQUEST_TIMEOUT = (408, "Request Timeout", "The server timed out waiting for the request.")
    CONFLICT = (409, "Conflict", "Indicates that the request could not be processed because of conflict in the request.")
    GONE = (410, "Gone", "Indicates that the resource requested is no longer available and will not be available again.")
    LENGTH_REQUIRED = (411, "Length Required", "The request did not specify the length of its content, which is required by the requested resource.")
    PRECONDITION_FAILED = (412, "Precondition Failed", "The server does not meet one of the preconditions that the requester put on the request.")
    PAYLOAD_TOO_LARGE = (413, "Payload Too Large", "The request is larger than the server is willing or able to process.")
    URI_TOO_LONG = (414, "URI Too Long", "The URI provided was too long for the server to process.")
    UNSUPPORTED_MEDIA_TYPE = (415, "Unsupported Media Type", "The request entity has a media type which the server or resource does not support.")
    RANGE_NOT_SATISFIABLE = (416, "Range Not Satisfiable", "The client has asked for a portion of the file, but the server cannot supply that portion.")
    EXPECTATION_FAILED = (417, "Expectation Failed", "The server cannot meet the requirements of the Expect request-header field.")
    IM_A_TEAPOT = (418, "I'm a Teapot", "The server refuses the attempt to brew coffee with a teapot.")
    MISDIRECTED_REQUEST = (421, "Misdirected Request", "The request was directed at a server that is not able to produce a response.")
    UNPROCESSABLE_ENTITY = (422, "Unprocessable Entity", "The request was well-formed but was unable to be followed due to semantic errors.")
    LOCKED = (423, "Locked", "The resource that is being accessed is locked.")
    FAILED_DEPENDENCY = (424, "Failed Dependency", "The request failed because it depended on another request and that request failed.")
    TOO_EARLY = (425, "Too Early", "Indicates that the server is unwilling to risk processing a request that might be replayed.")
    UPGRADE_REQUIRED = (426, "Upgrade Required", "The client should switch to a different protocol.")
    PRECONDITION_REQUIRED = (428, "Precondition Required", "The origin server requires the request to be conditional.")
    TOO_MANY_REQUESTS = (429, "Too Many Requests", "The user has sent too many requests in a given amount of time.")
    REQUEST_HEADER_FIELDS_TOO_LARGE = (431, "Request Header Fields Too Large", "The server is unwilling to process the request because its header fields are too large.")
    UNAVAILABLE_FOR_LEGAL_REASONS = (451, "Unavailable For Legal Reasons", "A server operator has received a legal demand to deny access to a resource or to a set of resources.")

    # 5xx Server Errors
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error", "A generic error message, given when an unexpected condition was encountered.")
    NOT_IMPLEMENTED = (501, "Not Implemented", "The server either does not recognize the request method, or it lacks the ability to fulfill the request.")
    BAD_GATEWAY = (502, "Bad Gateway", "The server was acting as a gateway or proxy and received an invalid response from the upstream server.")
    SERVICE_UNAVAILABLE = (503, "Service Unavailable", "The server is currently unavailable (because it is overloaded or down for maintenance).")
    GATEWAY_TIMEOUT = (504, "Gateway Timeout", "The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.")
    HTTP_VERSION_NOT_SUPPORTED = (505, "HTTP Version Not Supported", "The server does not support the HTTP protocol version used in the request.")
    VARIANT_ALSO_NEGOTIATES = (506, "Variant Also Negotiates", "Transparent content negotiation for the request results in a circular reference.")
    INSUFFICIENT_STORAGE = (507, "Insufficient Storage", "The server is unable to store the representation needed to complete the request.")
    LOOP_DETECTED = (508, "Loop Detected", "The server detected an infinite loop while processing the request.")
    NOT_EXTENDED = (510, "Not Extended", "Further extensions to the request are required for the server to fulfill it.")
    NETWORK_AUTHENTICATION_REQUIRED = (511, "Network Authentication Required", "The client needs to authenticate to gain network access.")

    def __init__(self, status: int, name: str, description: str):
        """
        Initialize an HTTPStatus enum member.
        """
        self._status = status
        self._name = name
        self._description = description

    @property
    def status(self) -> int:
        return self._status

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @classmethod
    def from_status(cls, status_code: int):
        """
        Returns the HTTPStatus enum member corresponding to the given status code.
        """
        for status in cls:
            if status.status == status_code:
                return status
        raise ValueError(f"No HTTP status found for code {status_code}")

    @classmethod
    def informational_responses(cls) -> List['HTTPStatus']:
        """
        Returns a list of all HTTP status codes in the 1xx range.
        """
        return [status for status in cls if 100 <= status.status < 200]

    @classmethod
    def success_responses(cls) -> List['HTTPStatus']:
        """
        Returns a list of all HTTP status codes in the 2xx range.
        """
        return [status for status in cls if 200 <= status.status < 300]

    @classmethod
    def redirection_responses(cls) -> List['HTTPStatus']:
        """
        Returns a list of all HTTP status codes in the 3xx range.
        """
        return [status for status in cls if 300 <= status.status < 400]

    @classmethod
    def client_error_responses(cls) -> List['HTTPStatus']:
        """
        Returns a list of all HTTP status codes in the 4xx range.
        """
        return [status for status in cls if 400 <= status.status < 500]

    @classmethod
    def server_error_responses(cls) -> List['HTTPStatus']:
        """
        Returns a list of all HTTP status codes in the 5xx range.
        """
        return [status for status in cls if 500 <= status.status < 600]

    def __str__(self):
        return f'{self.status} {self.name}: {self.description}'