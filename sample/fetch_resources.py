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
  card_dict = {}
  for file_path in files:
    file = open(file_path)
    yaml_data = yaml.load(file)
    file.close()
    card_name = os.path.splitext(ntpath.basename(file_path))[0]
    card_dict[card_name] = yaml_data

  return card_dict
