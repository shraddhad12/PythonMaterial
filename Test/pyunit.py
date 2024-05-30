import unittest
from unittest.mock import patch, Mock
import requests

def sum(a, b):
    return a+b

def get_user_detail():
    response = requests.get('https://www.google.com/')
    return response

class MyTest(unittest.TestCase):

    # called before calling each test function of class
    def setUp(self) -> None:
        print("Setup Called")
        self.a = 20
        self.b = 20

    #every test function name should start with "test"
    def test_fun_1(self):
        print("test-1 Called")
        #Arrange
        #Act
        result = sum(self.a, self.b)
        self.assertEqual((self.a + self.b), result)
    
    # called after calling each test function of class
    def tearDown(self) -> None:
         print("teardown Called")

    @patch('requests.get')
    def test_get_user_detail(self, mock_get):
         # Set up the mock to return a desired response
        mock_get.return_value = {'key': 'value'}

        result = get_user_detail()

        # Assert the result
        self.assertEqual(result, {'key': 'value'})

#can have multiple classes
class YourTest(unittest.TestCase):

    def test_fun_1(self):
        a, b =1,2
        self.assertEqual((a+b), 3)
        

if __name__ == "__main__":
    unittest.main()