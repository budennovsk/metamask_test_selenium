import os
from dotenv import load_dotenv
load_dotenv()

secret_fraz = os.getenv('SECRET_WORDS')
password_me = os.getenv('PASSWORD')
NETWORK = os.getenv('NETWORK')