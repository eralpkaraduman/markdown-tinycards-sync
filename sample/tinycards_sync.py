import os
import requests


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

  def get_decks(self, user_id = None):
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