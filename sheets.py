from gspread import Client, Spreadsheet, Worksheet, service_account

table_id = '1bhzeiQUXPZF4-Iyz1ar7govvjkFl4XAxKSx9pVoHuQc'
table_url = 'https://docs.google.com/spreadsheets/d/1bhzeiQUXPZF4-Iyz1ar7govvjkFl4XAxKSx9pVoHuQc/edit?gid=0#gid=0'
def client_init_json() -> Client:
    """Создание клиента для работы с Google Sheets."""
    return service_account(filename='golden-monkey.json')


def get_table_by_url(client: Client, table_url):
    """Получение таблицы из Google Sheets по ID таблицы."""
    return client.open_by_url(table_url)

def get_worksheet_info(table: Spreadsheet) -> dict:
    worksheets = table.worksheets()
    worksheet_info = {
        "count": len(worksheets),
        "names": [worksheet.title for worksheet in worksheets]
    }
    return worksheet_info
def insert_purchase(table: Spreadsheet, title: str, data: list, index: int = 1):
    worksheet = table.worksheet(title)
    worksheet.insert_row(data, index=index)
    
def test_add_data():
    client = client_init_json()
    table = get_table_by_url(client, table_url)
    worksheet_info = get_worksheet_info(table)
    insert_purchase(
        table=table,
        title=worksheet_info['names'[0]],
        data=['names', 'adress', 'email']
    )

test_add_data()
