import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Settings() :
    CIEL_TOKEN = os.getenv("CIEL_TOKEN")