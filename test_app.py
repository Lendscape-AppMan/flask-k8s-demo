import unittest

from app import app


class IndexTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_index(self):
        # Send a request to the / route
        response = self.client.get("/")

        # Assert that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Assert that the response uses the correct template
        self.assertTemplateUsed("index.html")

        # Assert that the response includes the correct data
        self.assertEqual(
            response.data,
            b'[(1, "John Doe", "john.doe@example.com"), (2, "Jane Smith", "jane.smith@example.com")]',
        )


if __name__ == "__main__":
    unittest.main()
