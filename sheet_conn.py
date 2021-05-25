import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'fuelagrosignal-9d43e3bdc0d7.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1xwvc6jAwYd07Qu3ireyjORle1CEZdlEbGhGXy_qEusA'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

#water-641@waterforcows.iam.gserviceaccount.com
#3bcdda439636ef192787c285d25ff96dc5d135d7