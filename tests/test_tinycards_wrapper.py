# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()
from .context import sample

import unittest
import warnings
from time import sleep

# ref: https://github.com/floscha/tinycards-python-api/blob/master/tests/client_test.py

# https://stackoverflow.com/a/26620811 # this didn't work
def ignore_warnings(test_func):
  def do_test(self, *args, **kwargs):
    with warnings.catch_warnings():
      warnings.simplefilter("ignore", ResourceWarning)
      test_func(self, *args, **kwargs)
  return do_test

class TinycardsWrapperTestSuite(unittest.TestCase):
  """TinycardsWrapper test cases."""

  def setUp(self):
    self.tcw = sample.TinycardsWrapper()

  def tearDown(self):
    sleep(1)

  @ignore_warnings
  def test_get_user(self):
    user_name = os.getenv("TINYCARDS_USER_NAME")
    password = os.getenv("TINYCARDS_PASSWORD")
    user = self.tcw.get_user(user_name, password)
    print(user.email)
    sleep(5)
    self.assertEquals(user.email, user_name)
    # assert user.email == user_name
    # assert "deckbot@superdamage.com" == user_name
    
    # assert True


if __name__ == '__main__':
  unittest.main(warnings='ignore')
