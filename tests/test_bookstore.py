import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestBookstoreAPI(unittest.TestCase):

    def test_get_books(self):
        response = requests.get(f"{BASE_URL}/books")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_add_book(self):
        new_book = {
            "title": "New Book",
            "author": "Author Name",
            "isbn": "1234567890",
            "genre": "Fiction",
            "price": 19.99,
            "quantity": 10
        }
        response = requests.post(f"{BASE_URL}/books", json=new_book)
        self.assertEqual(response.status_code, 201)

    # def test_update_book(self):
    #     updated_book = {
    #         "title": "Updated Book",
    #         "author": "Updated Author",
    #         "isbn": "1234567890",
    #         "genre": "Non-Fiction",
    #         "price": 29.99,
    #         "quantity": 5
    #     }
    #     response = requests.put(f"{BASE_URL}/books/1", json=updated_book)
    #     self.assertEqual(response.status_code, 204)

    def test_delete_book(self):
        response = requests.delete(f"{BASE_URL}/books/1")
        self.assertEqual(response.status_code, 204)

    def test_search_books(self):
        response = requests.get(f"{BASE_URL}/search?query=Book")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == '__main__':
    unittest.main()
