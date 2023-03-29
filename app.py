import os
from flask import Flask, request
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
from dotenv import load_dotenv


app = Flask('conf_scanner')

load_dotenv()

sheet_id = os.environ.get('SHEET_ID')


creds = service_account.Credentials.from_service_account_file(
    'path/to/key.json')
