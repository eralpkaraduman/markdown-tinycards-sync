# -*- coding: utf-8 -*-
from . import helpers
from tinycards import Tinycards
import json

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


def markdown_sync(user_name, password):
  client = Tinycards(user_name, password)
  user = client.get_user_info()
