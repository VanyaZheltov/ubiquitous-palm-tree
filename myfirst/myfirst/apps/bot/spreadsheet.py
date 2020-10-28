"""from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8') 
from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
CREDENTIALS_FILE = '/myfirst/apps/bot/englishpush.json'  #  ← имя скаченного файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
spreadsheetId = '1ljHiXFuoeTaZS4ZFSpekCdAsBGh6B5EsFPc3gDCAk2c'
range_name = 'Лист1!A:G'
def get_auth():
    table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
    print(table['values'][0])
    return table['values'][0]"""
    