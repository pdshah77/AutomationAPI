#!/usr/bin/env python

"""
.. module:: base_test
   :synopsis: Current base test class for all tests and various functions

.. moduleauthor:: Parth Shah <pdshah77@gmail.com>

"""
import json
import requests
import datetime
import time
import unittest
import logging
import os

class AbstractTest(unittest.TestCase):
    """Base test class for tests and various functions used in tests"""

    @staticmethod
    def get_test_data():
        with open("resoources/env.json") as json_data:
            data = json.load(json_data)

        return data['config']

    @classmethod
    def setUpClass(cls):

        cls.test_data = cls.get_test_data()
        cls.secret_key = cls.test_data['consumer_secret']
        cls.userName = cls.test_data['username']
        cls.email = cls.test_data['email']

    @staticmethod
    def get_users(self,headers):
        url = "https://api.foxpass.com/v1/users/"
        response = self.process_request(self, url, "GET", headers=headers)
        
        return response

    @staticmethod
    def create_user(self,data,headers):
        url = "https://api.foxpass.com/v1/users/"
        response = self.process_request(self, url, "POST", data=data,headers=headers)
        
        return response
    
    
    @staticmethod
    def process_request(self, url, method, headers={}, data="", params={}, **kw):

        #headers['Authorization']= 'Token ' + self.secret_key
        if (method == 'GET'):
            resp = requests.get(url,headers=headers)
        elif (method == 'POST'):
            resp = requests.post(url,headers=headers,data=data)

        return resp

    def code_message_checker(self,  response_json, expected_status, expected_message):
        assert response_json['status'] == expected_status, 'Bad Error Status - Expected: %s - Actual: %s'%(expected_status, response_json['status'])
        assert response_json['message'] == expected_message, 'Bad Error Message - Expected: %s - Actual: %s'%(expected_message, response_json['message'])