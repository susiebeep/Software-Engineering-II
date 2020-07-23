import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    # check empty passwords
    def test_1(self):
        password = ''
        self.assertFalse(check_pwd(password))

    # check short passwords (length 7)
    def test_2(self):
        password = 'abcdefg'
        self.assertFalse(check_pwd(password))

    # check long passwords (length 21)
    def test_3(self):
        password = 'abcdefghijklmnopqrstu'
        self.assertFalse(check_pwd(password))

    # check for at least one lowercase letter
    def test_4(self):
        password = 'PASSWORD'
        self.assertFalse(check_pwd(password))

    # check for at least one uppercase letter
    def test_5(self):
        password = 'password'
        self.assertFalse(check_pwd(password))


if __name__ == '__main__':
    unittest.main()

