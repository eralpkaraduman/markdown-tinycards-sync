from .fetch_resources import fetch_vocabulary_files
from .fetch_resources import parse_vocabulary_files
from .tinycards_sync import TinyCardsSync
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
  files = fetch_vocabulary_files()
  new_decks = parse_vocabulary_files(files)
  print(new_decks)

  # user_name = os.getenv("TINYCARDS_IDENTIFIER")
  # password = os.getenv("TINYCARDS_PASSWORD")

  # api = TinyCardsSync(user_name, password)

  # decks = api.get_decks()

  # print('Found ' + str(len(decks)) + ' existing decks.')
  # for deck in decks:
  #   api.delete_deck(deck['id'])

  # for new_deck in dec



  # for deck_name in deck_dict.keys():
  #   upsert_deck(deck_name, deck_dict[deck_name])
  # deck_name = 'first'
  # upsert_deck(deck_name, deck_dict[deck_name])


  # client = get_tinycards_client()
  # upsert_deck(client, )
  # user_name = os.getenv("TINYCARDS_IDENTIFIER")
  # password = os.getenv("TINYCARDS_PASSWORD")



  # download test vocabulary yaml from here:
  # https://raw.githubusercontent.com/eralpkaraduman/markdown-tinycards-sync/master/resources/test.yaml
  # user_name = os.getenv("TINYCARDS_IDENTIFIER")
  # password = os.getenv("TINYCARDS_PASSWORD")
  # markdown_sync(user_name, password)