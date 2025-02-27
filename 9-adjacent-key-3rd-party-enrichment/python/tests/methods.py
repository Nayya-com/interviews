from src.methods import get_adjacent_key
import unittest

class MethodsTest(unittest.TestCase):
# https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1326405838
    def setUp(self):
        self.my_dict = {
            'authentication': {
                'field': 'auth_url',
                'value': 'https://example.com/authorize'
            },
            'provider': {
                'field': 'npi',
                'value': '1326405838'
            },
            'claim': [
                {
                    'field': 'paid_date',
                    'value': '2024-01-01'
                },
                {
                    'field': 'source_url',
                    'value': 'https://example.com/other'
                }
            ]    
        }


    def test_get_url_by_step(self):
        self.assertEqual(
            'https://example.com/authorize',
            get_adjacent_key(self.my_dict, 'field', 'auth_url', 'value')
        )
        self.assertEqual(
            '1326405838',
            get_adjacent_key(self.my_dict, 'field', 'npi', 'value')
        )
        self.assertEqual(
            '2024-01-01',
            get_adjacent_key(self.my_dict, 'field', 'paid_date', 'value')
        )
        self.assertEqual(
            'https://example.com/other',
            get_adjacent_key(self.my_dict, 'field', ['source_url', 'auth_url'], 'value')
        )

    def test_get_step_by_value(self):
        self.assertEqual(
            'authorize',
            get_adjacent_key(self.my_dict, 'value', 'https://example.com/authorize', 'field')
        )
        self.assertEqual(
            'exit',
            get_adjacent_key(self.my_dict, 'value', '2024-01-01', 'paid_date')
        )
        self.assertEqual(
            'enter',
            get_adjacent_key(self.my_dict, 'value', 'https://example.com/other', 'field')
        )

    def test_no_match(self):
        self.assertEqual(
            None,
            get_adjacent_key(self.my_dict, 'field', 'https://example.com/buy', 'step')
        )


if __name__ == '__main__':
    unittest.main()
