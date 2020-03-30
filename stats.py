from github import Github
import json
from config import ACCESS_TOKEN
import unittest

g = Github(ACCESS_TOKEN)

repo = g.get_repo('laivictor/EE461L-Team-Project')
events = repo.get_events()
collabs = repo.get_collaborators()

master_commits = repo.get_commits().totalCount
total_commits = 0
total_issues = 0 

data = {}
commits = {}
issues = {}


for c in collabs:
	data[c.login] = {}
	data[c.login]['commits'] = 0
	data[c.login]['issues'] = 0
	data[c.login]['name'] = c.name
	data[c.login]['bio'] = c.bio
	data[c.login]['photo'] = c.avatar_url


for e in events:

	name = e.actor.login

	if(e.type == 'PushEvent'):
		data[name]['commits'] = data[name]['commits'] + 1
		total_commits = total_commits + 1
	elif(e.type =='IssuesEvent'):
		data[name]['issues'] = data[name]['issues'] + 1
		total_issues = total_issues + 1

data['total_commits'] = total_commits
data['total_issues'] = total_issues


with open('about.json', 'w') as f:
	json.dump(data, f,  indent = 2)




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



