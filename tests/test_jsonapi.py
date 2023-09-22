import json
import unittest

from jsonapi import MyEncoder, MyDecoder


class TestMyEncoderDecoder(unittest.TestCase):

    def setUp(self):
        self.encoder = MyEncoder()
        self.decoder = MyDecoder()

    def test_encode_decode_complex(self):
        original = complex(3, 4)
        encoded = json.dumps(original, cls=MyEncoder)
        decoded = json.loads(encoded, cls=MyDecoder)

        self.assertEqual(original, decoded)

    def test_encode_decode_range(self):
        original = range(1, 10, 2)
        encoded = json.dumps(original, cls=MyEncoder)
        decoded = json.loads(encoded, cls=MyDecoder)

        # Convert range to list for comparison
        self.assertEqual(list(original), list(decoded))

    def test_default_encode_decode(self):
        # Testing default data types which should use the default JSON encoding/decoding
        data_list = [
            (123, int),
            ("Hello", str),
            ([1, 2, 3], list),
            ({"key": "value"}, dict)
        ]

        for original, expected_type in data_list:
            encoded = json.dumps(original, cls=MyEncoder)
            decoded = json.loads(encoded, cls=MyDecoder)
            self.assertEqual(original, decoded)
            self.assertIsInstance(decoded, expected_type)


if __name__ == '__main__':
    unittest.main()



