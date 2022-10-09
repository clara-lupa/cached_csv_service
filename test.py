import unittest
from main import (
    get_values,
    convert_csv_to_data_dictionary,
    get_next_power_threshold,
    get_value_for_single_data_point,
)
import json


class TestGetValues(unittest.TestCase):
    def setUp(self) -> None:
        with open("fixtures.json") as test_data:
            [self.param1, self.param2, self.expected_result_format] = json.load(
                test_data
            )
        self.empty_param = {"data": {"attributes": {"list": []}}}
        return super().setUp()

    def create_expected_result_dictionary(self, result_value):
        expected_result = dict(self.expected_result_format)
        expected_result["data"]["attributes"]["result"]["value"] = f"{result_value:.5f}"
        return expected_result

    def test_returns_correct_result_result_for_empty_param(self):
        """Test that the function returns correct format and values for an empty list of parameters"""
        actual_result = get_values(param=self.empty_param)
        expected_result = self.create_expected_result_dictionary(0)
        self.assertDictEqual(actual_result, expected_result)

    def test_returns_correct_result_result_for_param1(self):
        """Test that the function returns correct format and values for a list of two parameter pairs"""
        actual_result = get_values(param=self.param1)
        expected_result = self.create_expected_result_dictionary(0.4962 + 0.4810)
        self.assertDictEqual(actual_result, expected_result)

    def test_returns_correct_result_result_for_param2(self):
        """Test that the function returns correct format and values for a list of one parameter pair"""
        actual_result = get_values(param=self.param2)
        expected_result = self.create_expected_result_dictionary(0.5062)
        self.assertDictEqual(actual_result, expected_result)


class TestConvertCsvToDataDictionary(unittest.TestCase):
    def test_returns_a_dict(self):
        self.assertIsInstance(convert_csv_to_data_dictionary(), dict)

    def test_contains_correct_keys(self):
        actual_key_list = list(convert_csv_to_data_dictionary())
        self.assertEqual(actual_key_list, list(range(1, 10)))


class TestGetNextPowerThreshold(unittest.TestCase):
    def test_raises_exception_for_invalid_power_value(self):
        self.assertRaises(AssertionError, get_next_power_threshold, 50)

    def test_returns_correct_result_for_value_between_thresholds(self):
        actual_result = get_next_power_threshold(32.5)
        self.assertEqual(actual_result, 40)

    def test_returns_correct_result_for_value_on_threshold(self):
        actual_result = get_next_power_threshold(10)
        self.assertEqual(actual_result, 10)


class TestGetValueForSingleParam(unittest.TestCase):
    def setUp(self) -> None:
        self.data_dict = convert_csv_to_data_dictionary()

    def test_returns_correct_value_for_valid_input(self):
        actual_result = get_value_for_single_data_point(
            data_dict=self.data_dict, date="2019-01-22", power="6"
        )
        self.assertEqual(actual_result, 0.5062)

    def test_returns_correct_value_for_date_after_september(self):
        actual_result = get_value_for_single_data_point(
            data_dict=self.data_dict, date="2019-12-31", power="37.5"
        )
        self.assertEqual(actual_result, 0.3470)

    def test_raises_exception_for_invalid_date(self):
        self.assertRaises(
            ValueError,
            get_value_for_single_data_point,
            data_dict=self.data_dict,
            power="37",
            date="2019-13-54",
        )


if __name__ == "__main__":
    unittest.main()
