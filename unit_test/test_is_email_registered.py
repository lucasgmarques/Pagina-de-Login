
import unittest
from app import is_email_registered

class AppTestCase(unittest.TestCase):
    def test_is_email_registered(self):
        # Assuming a test database with pre-existing records
        self.assertTrue(is_email_registered("johndoe@example.com"))
        self.assertFalse(is_email_registered("janedoe@example.com"))

if __name__ == '__main__':
    unittest.main()
