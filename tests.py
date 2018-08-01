import api
import unittest

#from unittest.mock import patch

HTTP_200_OK = 200
HTTP_404_NOT_FOUND = 404


class apiTestCase(unittest.TestCase):

	def setUp(self):
		api.app.testing = True
		self.app = api.app.test_client()
	
	def test_valid_username_returns_code_200(self):
		response = self.app.get('/applicant/pato24s')

		self.assertEquals(HTTP_200_OK, response.status_code)

	def test_invalid_username_returns_code_404(self):
		response = self.app.get('/applicant/pato24s!#')
		self.assertEquals(HTTP_404_NOT_FOUND, response.status_code)


if __name__ == '__main__':
    unittest.main()