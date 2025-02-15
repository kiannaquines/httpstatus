import unittest
from httpstatus.httpstatus import HTTPStatus


class TestHTTPStatus(unittest.TestCase):

    def test_http_status_values(self):
        """Test that each HTTPStatus has correct attributes."""
        self.assertEqual(HTTPStatus.OK.status, 200)
        self.assertEqual(HTTPStatus.OK.name, "OK")

        self.assertEqual(HTTPStatus.NOT_FOUND.status, 404)
        self.assertEqual(HTTPStatus.NOT_FOUND.name, "Not Found")

    def test_enum_membership(self):
        """Test that all expected status codes are in the enum."""
        self.assertIn(HTTPStatus.OK, HTTPStatus)
        self.assertIn(HTTPStatus.INTERNAL_SERVER_ERROR, HTTPStatus)

    def test_enum_uniqueness(self):
        """Ensure each status code is unique."""
        statuses = {status.status for status in HTTPStatus}
        self.assertEqual(len(statuses), len(HTTPStatus))

    def test_enum_iteration(self):
        """Ensure enumeration of all HTTP statuses works correctly."""
        statuses = list(HTTPStatus)
        self.assertGreater(len(statuses), 0)
        self.assertIn(HTTPStatus.OK, statuses)
        self.assertIn(HTTPStatus.NOT_FOUND, statuses)


if __name__ == "__main__":
    unittest.main()
