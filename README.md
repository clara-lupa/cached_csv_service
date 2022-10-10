# cached_csv_service

This project provides a function that returns (the sum of) values read from the `data.csv` file, given a list of date-power-combinations. For each of these combinations, the data file contains a certain value. The function returns the sum of all corresponding values for the list of date-power-combinations.
In order to improve performance, the csv file will be converted to a dictionary that is cached. In addition to that, the values calculated for any list of date-power-combinations will be cached as well.

To run the project, run the function `get_values` from the file `main.py`. To run the tests, run `python -m unittest test`.
The file `caching_test` contains a script to track and print runtimes and cache info for an adjustable number of runs and repetitions. It can be invoked by running `python caching_tests`.