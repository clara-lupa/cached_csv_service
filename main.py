import csv
from datetime import datetime
import math


def convert_csv_to_data_dictionary() -> dict:
    data_dict = {}
    with open("data.csv") as data_file:
        header = [h.strip() for h in data_file.readline().split(",")]
        reader = csv.DictReader(data_file, fieldnames=header)
        for row in reader:
            month = datetime.fromisoformat(row["date_from"]).month
            data_dict[month] = row
            data_dict[month].pop("date_from")
    return data_dict


def get_next_power_threshold(power) -> int:
    """Return the upper threshold of the power interval in which the passed values falls"""
    assert power > 0 and power <= 40, "Invalid power value"
    next_tenner = math.ceil(power / 10) * 10
    return 30 if next_tenner == 20 else next_tenner


def get_value_for_single_param(data_dict, power, date) -> float:
    """Given a date and a power value, return the according value from the data dictionary."""
    date = datetime.fromisoformat(date)
    if date >= datetime(year=2019, month=10, day=1):
        month = 9  # use september for any date after october 2019
    else:
        month = date.month
    power_threshold = get_next_power_threshold(float(power))
    column_name = f"value_up_to_{power_threshold}_kwp"
    return float(data_dict[month][column_name])


def get_values(param) -> dict:
    params_list = param["data"]["attributes"]["list"]
    data_dict = convert_csv_to_data_dictionary()
    total_value = 0
    for param_pair in params_list:
        total_value += get_value_for_single_param(data_dict=data_dict, **param_pair)
    result = {"data": {"attributes": {"result": {"value": f"{total_value:.5f}"}}}}
    print(result)
    return result
