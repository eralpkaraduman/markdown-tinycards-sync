import os
import requests
import json
import urllib


class TinyCardsSync():

    api_root = 'https://tinycards.duolingo.com/api/1/'
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip',
        # 'Referer': 'https://tinycards.duolingo.com/create',
        # 'Content-Type': 'application/json; charset=UTF-8',
        'Connection': 'keep-alive',
        # 'Te': 'Trailers',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }

    def __init__(self, user_identifier, user_password):
        self.user_identifier = user_identifier
        self.user_password = user_password
        self.jwt = None

    def login(self):
        print('Logging in...')
        headers = self.default_headers.copy()
        path = self.api_root + 'login'
        payload = {
            'identifier': self.user_identifier,
            'password': self.user_password
        }
        r = requests.post(path, headers, params=payload)
        cookies = r.headers['Set-Cookie'].split(';')
        jwt = next((cookie for cookie in cookies if 'jwt_token' in cookie))
        self.jwt = jwt
        print('JWT: ' + self.jwt)
        self.user_id = str(r.json()['id'])
        print('User id: ' + self.user_id)

    def logged_in(self):
        return self.jwt != None

    def get_decks(self, user_id=None):
        if not self.logged_in():
            self.login()

        print('Fetching decks...')

        if user_id == None:
            user_id = self.user_id

        print('User id: ' + user_id)

        decks = []
        headers = self.default_headers.copy()
        headers['Cookie'] = self.jwt
        path = self.api_root + 'decks?userId=' + user_id
        r = requests.get(path, headers)
        for deckData in r.json()['decks']:
            deck = {
                'name': deckData['name'],
                'id': deckData['id']
            }
            decks.append(deck)
        return decks

    def delete_deck(self, deck_id):
        if not self.logged_in():
            self.login()

        print('Deleting deck: ' + deck_id)

        headers = self.default_headers.copy()
        headers['Cookie'] = self.jwt
        path = self.api_root + 'decks/' + str(deck_id)
        requests.delete(path, headers=headers)

    def create_deck(self, deck_name, deck_cards, deck_description = 'Description'):
        if not self.logged_in():
            self.login()

        print('Creating deck: ' + deck_name)
        print('Cards: ' + str(len(deck_cards)))

        cards_json = self.build_cards_json(deck_cards)

        headers = self.default_headers.copy()
        headers['Cookie'] = self.jwt
        path = self.api_root + 'decks'
        payload = {
            "private": False,
            "cards": cards_json,
            "ttsLanguages": "[]",
            "name": deck_name,
            "blacklistedSideIndices": "[]",
            "blacklistedQuestionTypes": "[]",
            "shareable": False,
            "gradingModes": "[]",
            "description": deck_description,
            "fromLanguage": "en"
        }

        r = requests.post(path, headers=headers, json=payload)
        print('Result: ' + str(r.status_code))
        if r.status_code != 201:
            print(r.json())

    def build_card_side(self, side_text):
        print('Building card side: ' + side_text)
        return {
            'concepts': [
                {
                    'fact': {
                        'type': 'TEXT',
                        'text': side_text
                    }
                }
            ]
        }

    def build_cards_json(self, deck_cards):
        card_list = []
        for card in deck_cards:
            deck_sides = [
                self.build_card_side(card['front']),
                self.build_card_side(card['back'])
            ]
            card_list.append({
                'sides': deck_sides
            })

        return json.dumps(card_list)#.replace('"', '/\"')

# from tinycards import Tinycards
# from tinycards.model import Deck

# def get_tinycards_client():
#   user_name = os.getenv("TINYCARDS_IDENTIFIER")
#   print('Logging in with user: ' + user_name)
#   password = os.getenv("TINYCARDS_PASSWORD")
#   client = Tinycards(user_name, password)
#   print('User id: ' + str(client.user_id))
#   return client

# def upsert_deck(deck_name, data_dict):
#   print('Upserting deck: ' + deck_name)
#   client = get_tinycards_client()
#   # print(client.get_decks())

#   deck = client.find_deck_by_title('Test Deck')
#   print(deck.cards)
    # deck.user_id = client.user_id
    # client.create_deck(deck)

    # user_id = client.user_id

    # deck = Deck(deck_name)
    # for key in data_dict.keys():
    #   value = data_dict[key]
    #   deck.add_card((key, value))

    # deck.user_id = user_id
    # print(deck)
    # print(deck.name)
    # deck = client

    # client.update_deck(deck)
