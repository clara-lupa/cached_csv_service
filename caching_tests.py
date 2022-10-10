from main import get_values, get_value_for_data_points
import timeit

ATTRIBUTES_LIST_LENGTH = 100
RUNS_PER_REPETITION = 10000
REPETITIONS = 5

param = {
    "data": {
        "attributes": {
            "list": [
                {"power": "12", "date": "2019-01-22"},
            ]
            * ATTRIBUTES_LIST_LENGTH
        }
    }
}


print(
    f"The minimum time for all repetitions was {min(timeit.repeat(lambda: get_values(param), number=RUNS_PER_REPETITION, repeat=REPETITIONS))}"
)

print(get_value_for_data_points.cache_info())
get_value_for_data_points.cache_clear()
