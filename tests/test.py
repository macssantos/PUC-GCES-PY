import unittest
from unittest.mock import patch, mock_open
from your_module import get_config

class TestGetConfig(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='NUMBER,ADDRESS,ZIPCODE\n124234,EIRUWOEJI,345-345\n124234,EIRUWOEJI,345-345\n124234,EIRUWOEJI,345-345\n'))
    def test_get_config_with_csv(self):
        # Chama a função sob teste
        result = get_config()

        # Adicione suas asserções com base no que você espera
        self.assertEqual(result['features_configs'], ['NUMBER', 'ADDRESS', 'ZIPCODE'])
        # Adicione mais asserções conforme necessário

if __name__ == '__main__':
    unittest.main()
