from main import app
from unittest import TestCase
from flask import json
from nose.tools import ok_, eq_
import unittest



class FlaskappTests(TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_parameter_status_code_500(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibonacci/a')
        # assert the status code of the response
        self.assertEqual(result.status_code, 500)

    def test_parameter_status_code_200(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibonacci/0')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_url_incorrect_status_code_404(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibo/0')
        # assert the status code of the response
        self.assertEqual(result.status_code, 404)

    def test_fibonacci_list_value_0(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibonacci/0')
        # self.client.get('/fibonacci/0')
        # assert the status code of the response
        self.assertEqual(json.loads(result.data), [])

    def test_fibonacci_list_value_1(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibonacci/1')
        # self.client.get('/fibonacci/0')
        # assert the status code of the response
        self.assertEqual(json.loads(result.data), [0])

    def test_fibonacci_list_value_2(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibonacci/2')
        # self.client.get('/fibonacci/0')
        # assert the status code of the response
        self.assertEqual(json.loads(result.data), [0,1])

    # if __name__ == '__main__':   
    # nose.run()
