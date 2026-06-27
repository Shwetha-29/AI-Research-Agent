import os
import csv
import gspread

from google.oauth2.service_account import Credentials


def upload_to_google_sheets(csv_file):

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    cred_path = os.path.join(
        BASE_DIR,
        "credentials.json"
    )

    creds = Credentials.from_service_account_file(
        cred_path,
        scopes=scopes
    )

    client = gspread.authorize(creds)

    SPREADSHEET_ID = "1wnOUrBaKVD1z03tzgc7MFpNVntzQ9XYoUOxor5ATJeI"

    spreadsheet = client.open_by_key(
        SPREADSHEET_ID
    )

    sheet = spreadsheet.sheet1

    sheet.clear()

    rows = []

    with open(
        csv_file,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        for row in reader:
            rows.append(row)

    if rows:
        sheet.update(rows)

    print("\nGoogle Sheet Updated:")
    print(spreadsheet.url)