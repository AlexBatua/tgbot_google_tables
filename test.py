import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheet_id = '1bhzeiQUXPZF4-Iyz1ar7govvjkFl4XAxKSx9pVoHuQc'
sheet_name = 'Sheet1'
credentials_file = 'local.json'
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def client_init(file, rows):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(file, rows)
    return gspread.authorize(credentials)


def get_sheet(id_key):
    client = client_init(credentials_file, scope)
    return client.open_by_key(id_key)


def insert_purchase(purchase: tuple):
    spreadsheet = get_sheet(sheet_id)
    sheet = spreadsheet.worksheet(sheet_name)
    sheet.insert_row(purchase, index=2)





#credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
#client = gspread.authorize(credentials)
#spreadsheet = client.open_by_key(sheet_id)
#sheet = spreadsheet.worksheet(sheet_name)






