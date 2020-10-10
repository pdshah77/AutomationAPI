"""
.. module:: test_get_users.py
   :synopsis: Test class ensures the Attribute Verification for Users GET/POST API

.. moduleauthor:: Parth Shah <pdshah77@gmail.com>

"""
import unittest
from tests.base_test import AbstractTest
import json
import pytest

class GetUsers(AbstractTest):
    """Test class ensures the Attribute Verification for User Verification"""

    @classmethod
    def setUpClass(cls):
        """ Test class setup function"""
        AbstractTest.setUpClass()
        
        cls.request_headers = {"Accept":"application/json"}


    def tearDown(self):
        pass
    
    def test_no_authorization(self):
        """TC-1 No Authorization in API
        :api tested: https://api.foxpass.com/v1/users/ (GET)"""
    
        response = self.get_users(self,self.request_headers)
        response_json = response.json()
        self.code_message_checker(response_json, "error", "No authorization token found.")
        
    def test_invalid_authorization(self):
        """TC-2 Invalid Authorization in API
        :api tested: https://api.foxpass.com/v1/users/ (GET)"""
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token 123NcEmZlkex'
        response = self.get_users(self,request_headers)
        response_json = response.json()
        self.code_message_checker(response_json, "error", "Invalid authorization token.")    
        
    def test_valid_authorization(self):
        """TC-3 Valid Authorization in API
        :api tested: https://api.foxpass.com/v1/users/ (GET)"""
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token ' + self.secret_key
        response = self.get_users(self,request_headers)
    
    def test_expected_fields_in_users(self):
        """TC-4 Verify Expected Fields in Users Response
        :api tested: https://api.foxpass.com/v1/users/ (GET)"""
        request_headers = self.request_headers.copy()
        request_headers['Authorization'] = 'Token ' + self.secret_key
        response = self.get_users(self,request_headers)
        response_json = response.json()
        fields = ["username", "email", "uid", "created", "gid", "is_eng_user", "is_posix_user", "is_active", "active", "shell","first_name","last_name","github_username","custom_fields"]
        for data in range(len(response_json['data'])):
            for req_field in fields:
                self.assertTrue(response_json['data'][data].__contains__(req_field), "Some of response keys -- %s are malformed for -- %s"%(req_field,response_json['data'][data]))