import csv
from datetime import datetime
import math
from functools import lru_cache

cache = {}


def convert_csv_to_data_dictionary() -> dict:
    """Read csv file and return data as dictionary with months as keys"""
    data_dict = {}
    with open("data.csv") as data_file:
        header = [h.strip() for h in data_file.readline().split(",")]
        reader = csv.DictReader(data_file, fieldnames=header)
        for row in reader:
            month = datetime.fromisoformat(row["date_from"]).month
            data_dict[month] = row
            data_dict[month].pop("date_from")
    return data_dict


def get_next_power_threshold(power: float) -> int:
    """Return the upper threshold of the power interval in which the passed values falls"""
    assert power > 0 and power <= 40, "Invalid power value"
    next_tenner = math.ceil(power / 10) * 10
    return 30 if next_tenner == 20 else next_tenner


def get_value_for_single_data_point(power: str, date_string: str) -> float:
    """Given a date and a power value, return the according value from the data dictionary."""
    if "data_dict" not in cache:
        cache["data_dict"] = convert_csv_to_data_dictionary()
    date = datetime.fromisoformat(date_string)
    if date >= datetime(year=2019, month=10, day=1):
        month = 9  # use september for any date after september 2019
    else:
        month = date.month
    power_threshold = get_next_power_threshold(float(power))
    column_name = f"value_up_to_{power_threshold}_kwp"
    return float(cache["data_dict"][month][column_name])


@lru_cache
def get_value_for_data_points(data_points: tuple) -> float:
    if len(data_points) == 0:
        return 0
    return get_value_for_single_data_point(*data_points[0]) + get_value_for_data_points(
        data_points[1:]
    )


def get_values(param: dict) -> dict:
    data_points = tuple(
        [
            (point["power"], point["date"])
            for point in param["data"]["attributes"]["list"]
        ]
    )
    total_value = get_value_for_data_points(data_points)
    result = {"data": {"attributes": {"result": {"value": f"{total_value:.5f}"}}}}
    print(result)
    return result
