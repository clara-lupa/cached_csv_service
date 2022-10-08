import csv
from datetime import datetime


def convert_csv_to_data_dictionary():
    data_dict = {}
    with open("data.csv") as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            month = datetime.fromisoformat(row["date_from"]).month
            data_dict[month] = row
            data_dict[month].pop("date_from")
    return data_dict


def get_values(data):
    pass
