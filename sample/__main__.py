from .core import markdown_sync
from .fetch_resources import fetch_vocabulary_files
from .fetch_resources import parse_vocabulary_files
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
  files = fetch_vocabulary_files()
  deck_dict = parse_vocabulary_files(files)
  print(deck_dict)



  # download test vocabulary yaml from here:
  # https://raw.githubusercontent.com/eralpkaraduman/markdown-tinycards-sync/master/resources/test.yaml
  # user_name = os.getenv("TINYCARDS_IDENTIFIER")
  # password = os.getenv("TINYCARDS_PASSWORD")
  # markdown_sync(user_name, password)