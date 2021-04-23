import unittest
import sqlite3
from unittest import result, mock



from unittest import TestCase, mock, main,result
from unittest.mock import patch
from .auth import login_post,signup_post



class Testmock(unittest.TestCase):

# Testing auth function by using mocking method
 @mock.patch('auth.login_post')
 def test_login_post(self, test_mock):
        test_mock = login_post
        assert test_mock is login_post

 @mock.patch('auth.signup_post')
 def test_signup_postt(self, test_mock):
        test_mock = signup_post
        assert test_mock is signup_post

if __name__ == "__main__":
    unittest.main()