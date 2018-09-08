import os
import shutil
import yaml
import ntpath
from git import Repo

def fetch_vocabulary_files():
  repo = 'https://github.com/eralpkaraduman/learning-finnish-notes.git'
  repodir = os.path.join('temp', 'repo')
  vocabularydir = os.path.join(repodir, 'vocabulary')
  absolute_vocabularydir = os.path.join(os.getcwd(), vocabularydir)
  if os.path.isdir(repodir):
    shutil.rmtree(repodir)

  print('cloning repo: ' + repo)
  Repo.clone_from(repo, repodir)

  vocabulary_files = []
  for (_, _, filenames) in os.walk(absolute_vocabularydir):
    vocabulary_files.extend(filenames)
    break

  absolute_vocabulary_files = []
  for filename in vocabulary_files:
    filePath = os.path.join(absolute_vocabularydir, filename)
    absolute_vocabulary_files.append(filePath)

  return absolute_vocabulary_files


def parse_vocabulary_files(files):
  decks = []
  for file_path in files:
    file = open(file_path)
    yaml_data = yaml.load(file)
    file.close()

    cards = []
    for card_front in yaml_data.keys():
      card_back = yaml_data[card_front]
      cards.append({
        'front': card_front,
        'back': card_back,
      })

    deck_name = os.path.splitext(ntpath.basename(file_path))[0]
    decks.append({
      'name': deck_name,
      'cards': cards
    })

  return decks
