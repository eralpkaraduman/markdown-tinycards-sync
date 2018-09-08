from .fetch_resources import fetch_vocabulary_files
from .fetch_resources import parse_vocabulary_files
from .tinycards_sync import TinyCardsSync
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    files = fetch_vocabulary_files()
    new_decks = parse_vocabulary_files(files)

    user_name = os.getenv("TINYCARDS_IDENTIFIER")
    password = os.getenv("TINYCARDS_PASSWORD")

    api = TinyCardsSync(user_name, password)

    decks = api.get_decks()

    print('Found ' + str(len(decks)) + ' existing decks.')
    for deck in decks:
      api.delete_deck(deck['id'])

    for new_deck in new_decks:
        deck_name = new_deck['name']
        deck_cards = new_deck['cards']
        api.create_deck(deck_name, deck_cards)
