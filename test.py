import unittest
from main import get_values, convert_csv_to_data_dictionary
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
        expected_result["data"]["attributes"]["result"]["value"] = str(result_value)
        return expected_result

    def test_returns_correct_result_result_for_empty_param(self):
        """Test that the function returns correct format and values for an empty list of parameters"""
        actual_result = get_values(data=self.empty_param)
        expected_result = self.create_expected_result_dictionary(0)
        self.assertDictEqual(actual_result, expected_result)

    def test_returns_correct_result_result_for_param1(self):
        """Test that the function returns correct format and values for a list of two parameter pairs"""
        actual_result = get_values(data=self.empty_param)
        expected_result = self.create_expected_result_dictionary(0.4962 + 0.4810)
        self.assertDictEqual(actual_result, expected_result)

    def test_returns_correct_result_result_for_param2(self):
        """Test that the function returns correct format and values for a list of one parameter pair"""
        actual_result = get_values(data=self.empty_param)
        expected_result = self.create_expected_result_dictionary(0.5062)
        self.assertDictEqual(actual_result, expected_result)


class TestConvertCsvToDataDictionary(unittest.TestCase):
    def test_returns_a_dict(self):
        self.assertIsInstance(convert_csv_to_data_dictionary(), dict)

    def test_contains_correct_keys(self):
        actual_key_list = list(convert_csv_to_data_dictionary())
        self.assertEqual(actual_key_list, list(range(1, 10)))


if __name__ == "__main__":
    unittest.main()
