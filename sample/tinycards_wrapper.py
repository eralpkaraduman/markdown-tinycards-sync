# -*- coding: utf-8 -*-
from tinycards import Tinycards


class TinycardsWrapper():
  def get_user(self, user_name, password):
    self.client = Tinycards(user_name, password)
    user = self.client.get_user_info()
    return user
