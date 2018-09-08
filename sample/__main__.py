from .core import markdown_sync
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
  user_name = os.getenv("TINYCARDS_IDENTIFIER")
  password = os.getenv("TINYCARDS_PASSWORD")
  markdown_sync(user_name, password)