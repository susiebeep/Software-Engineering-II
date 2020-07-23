import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    # check empty passwords
    def test_1(self):
        password = ''
        self.assertFalse(check_pwd(password))


if __name__ == '__main__':
    unittest.main()

