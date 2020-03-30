import unittesting
import stats


#unit tests for stats module
class TestingStats(unittest.TestCase):

	def test(self):

		test_comm = 0
		test_iss = 0

		for c in collabs:
			test_comm = test_comm + data[c.login]['commits']
			test_iss = test_iss + data[c.login]['issues']
			

		self.assertEqual(data['total_commits'], test_comm)
		self.assertEqual(data['total_issues'], test_iss)



if __name__ == "__main__":
	unittest.main()