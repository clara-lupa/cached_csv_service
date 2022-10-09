from main import get_values, get_value_for_data_points
import timeit


param = {
    "data": {
        "attributes": {
            "list": [
                {"power": "12", "date": "2019-01-22"},
                {"power": "8", "date": "2019-02-22"},
            ]
            * 100
        }
    }
}


print(timeit.repeat(lambda: get_values(param), number=10000, repeat=5))

print(get_value_for_data_points.cache_info())
get_value_for_data_points.cache_clear()
