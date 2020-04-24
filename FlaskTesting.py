from main import app
import unittest
import json

class FlaskTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		
		pass

	@classmethod
	def tearDownClass(cls):
		pass


	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True


	def tearDown(self):
		pass


	def test_home_status_code(self):
		result = self.app.get('/')
		self.assertEqual(result.status_code, 200)

	def test_countries_status_code(self):

		with open('countries.json', 'r') as f:
			data = json.load(f)

		s = '/countries' + str(data['country'])
		result = self.app.get('/countries' + str(data['country']))
		self.assertEqual(result.status_code, 200)

	def test_sports_status_code(self):

		result = self.app.get('/sports')
		self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
	unittest.main()