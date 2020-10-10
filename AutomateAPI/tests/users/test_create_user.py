"""
.. module:: test_create_user.py
   :synopsis: Test class ensures Creation of Users POST API

.. moduleauthor:: Parth Shah <pdshah77@gmail.com>

"""
import unittest
from tests.base_test import AbstractTest
import json
import pytest

class CreateUser(AbstractTest):
    """Test class ensures the Creation of User Verification"""

    @classmethod
    def setUpClass(cls):
        """ Test class setup function"""
        AbstractTest.setUpClass()
        
        cls.request_headers = {"Content-Type":"application/json", "Accept":"application/json"}


    def tearDown(self):
        pass
    
    def test_create_user_empty_body(self):
        """TC-1 No Request Body in API
        :api tested: https://api.foxpass.com/v1/users/ (POST)"""
        data = {}
        data = json.dumps(data)
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token ' + self.secret_key
        response = self.create_user(self,data,request_headers)
        response_json = response.json()
        self.code_message_checker(response_json, "error", "Empty request body")
    
    def test_create_user_empty_email(self):
        """TC-2 No Email in Request Body in API
        :api tested: https://api.foxpass.com/v1/users/ (POST)"""
        data = {}
        data["username"] = self.userName
        data["email"] = ""
        data = json.dumps(data)
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token ' + self.secret_key
        response = self.create_user(self,data,request_headers)
        response_json = response.json()
        self.code_message_checker(response_json, "error", "email field required")
        
    def test_create_user_empty_username(self):
        """TC-3 No Username in Request Body in API
        :api tested: https://api.foxpass.com/v1/users/ (POST)"""
        data = {}
        data["username"] = ""
        data["email"] = self.email
        data = json.dumps(data)
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token ' + self.secret_key
        response = self.create_user(self,data,request_headers)
        response_json = response.json()
        self.code_message_checker(response_json, "error", "username field required")
        
    def test_create_user_valid(self):
        """TC-4 Valid Body in API
        :api tested: https://api.foxpass.com/v1/users/ (POST)"""
        data = {}
        data["username"] = self.userName
        data["email"] = self.email
        data["send_email"] = True
        data = json.dumps(data)
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token ' + self.secret_key
        response = self.create_user(self,data,request_headers)
        response_json = response.json()
        self.assertTrue(response_json['status']=='ok', "User Creation Failed")
        