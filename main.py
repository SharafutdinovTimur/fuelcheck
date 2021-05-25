import sheet_conn as gs
import json
import datetime
import requests

#проверка последнего элемента в значениях агросигнала
last_row_F = len(gs.service.spreadsheets().values().get(spreadsheetId=gs.spreadsheet_id, range='F:F').execute().get('values', []))
last_row_B = len(gs.service.spreadsheets().values().get(spreadsheetId=gs.spreadsheet_id, range='B:B').execute().get('values', []))

# значения с счетчиков из гугла в словарь
values_from_sheets =[]

range_of_columns = ['B2:B'+str(last_row_B), "C2:C"+str(last_row_B), "D2:D"+str(last_row_B), "E2:E"+str(last_row_B), "F2:F"+str(last_row_B), "G2:G"+str(last_row_B)]

headers = gs.service.spreadsheets().values().get(spreadsheetId=gs.spreadsheet_id, range="B1:G1").execute()['values'][0]

for x in range(1, last_row_B):
    values_from_sheets.append(gs.service.spreadsheets().values().get(spreadsheetId=gs.spreadsheet_id, range="B"+str(x)+":G"+str(x)).execute()['values'])

print(values_from_sheets)






