import sqlite3
import unittest
from unittest.mock import MagicMock

from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_index(self):
        # Send a request to the / route
        response = self.client.get("/")

        # Assert that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Assert that the response includes the correct name and email tuples
        self.assertIn(b"Charlie Dixon", response.data)
        self.assertIn(b"charlie.dixon@lendscape.com", response.data)

    def test_submit(self):
        # Create a mock request object with the mock form data
        request = MagicMock()
        request.form = {"id": 3, "name": "John Doe", "email": "johndoe@example.com"}
        response = self.client.post("/", data=request.form)

        self.assertEqual(response.status_code, 302)

        # Connect to the database and check if the data was inserted into the users table
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
        data = c.fetchall()
        conn.close()

        # Assert that the users table contains the correct data
        self.assertEqual(data, [(3, "John Doe", "johndoe@example.com")])

    def tearDown(self):
        # Connect to the database and remove all rows containing the name "John Doe"
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE name = 'John Doe'")
        conn.commit()
        conn.close()


if __name__ == "__main__":
    unittest.main()
