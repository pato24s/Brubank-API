import sys
sys.path.insert(0, '../')

import api

import unittest
from unittest.mock import patch
from unittest.mock import Mock
import json
from nose.tools import assert_is_none, assert_list_equal

HTTP_200_OK = 200
HTTP_404_NOT_FOUND = 404


class apiTestCase(unittest.TestCase):

	def setUp(self):
		api.app.testing = True
		self.app = api.app.test_client()
	
	@patch('requests.get')
	def test_valid_username_returns_code_200_and_valid_json_with_backend_as_team(self, mockResponse):
		with open('./utils/jsonValidUserBackend') as json_file:  
			jsonResponse = json.load(json_file)

		mockResponse.return_value.json.return_value = jsonResponse
		mockResponse.return_value.status_code=200


		response = self.app.get('/applicant/pato24s')

		jsonValidUserBackend = {'applicant': 'pato24s', 'team': 'Backend'}

		self.assertEqual(response.status_code,HTTP_200_OK)
		self.assertEqual(response.json, jsonValidUserBackend)

	@patch('requests.get')
	def test_valid_username_returns_code_200_and_valid_json_with_web_as_team(self, mockResponse):
		with open('./utils/jsonValidUserWeb') as json_file:  
			jsonResponse = json.load(json_file)

		mockResponse.return_value.json.return_value = jsonResponse
		mockResponse.return_value.status_code=200


		response = self.app.get('/applicant/impronunciable')

		jsonValidUserWeb = {'applicant': 'impronunciable', 'team': 'Web'}

		self.assertEqual(response.status_code,HTTP_200_OK)
		self.assertEqual(response.json, jsonValidUserWeb)


	@patch('requests.get')
	def test_valid_username_returns_code_200_and_valid_json_with_mobile_as_team(self, mockResponse):
		with open('./utils/jsonValidUserMobile') as json_file:  
			jsonResponse = json.load(json_file)

		mockResponse.return_value.json.return_value = jsonResponse
		mockResponse.return_value.status_code=200


		response = self.app.get('/applicant/pepeMobile')

		jsonValidUserMobile = {'applicant': 'pepeMobile', 'team': 'Mobile'}

		self.assertEqual(response.status_code,HTTP_200_OK)
		self.assertEqual(response.json, jsonValidUserMobile)


	@patch('requests.get')
	def test_invalid_username_returns_code_404_and_error_msg(self, mockResponse):
		with open('./utils/jsonInvalidUser') as json_file:  
			jsonResponse = json.load(json_file)

		mockResponse.return_value.json.return_value = jsonResponse
		mockResponse.return_value.status_code=404


		response = self.app.get('/applicant/pato24st')

		jsonInvalidUser = {'message': 'User pato24st is not registered in GitHub'}

		self.assertEqual(response.status_code,HTTP_404_NOT_FOUND)
		self.assertEqual(response.json, jsonInvalidUser)

	@patch('requests.get')
	def test_invalid_language_is_not_considered_and_returns_code_200(self, mockResponse):
		with open('./utils/jsonInvalidLang') as json_file:
			jsonResponse = json.load(json_file)

		mockResponse.return_value.json_return_value = jsonResponse
		mockResponse.return_value.status_code=200

		response = self.app.get('applicant/jtyjty99999')

		jsonInvalidLang = {"applicant": "jtyjty99999", "team": "Web"}

		self.assertEqual(response.status_code,HTTP_200_OK)
		self.assertEqual(response.json, jsonInvalidLang)


if __name__ == '__main__':
    unittest.main()
