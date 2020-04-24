import unittest
import requests
from selenium import webdriver
import json
import time

website_link = "https://olympics-269900.appspot.com/"

#unit tests for host-cities pages
class HostTests(unittest.TestCase):

	
	def test_cities_link(self):
		host_page = requests.get(website_link)
		self.assertTrue(host_page.status_code == 200)
	
	def test_each_city_link(self):
		data = None
		with open("../host-cities/venues.json") as json_f:
			data = json.load(json_f)
		for key in data.keys():
			year = str(data[key]["year"])
			season = data[key]["season"]
			city_link = "/host-cities/select?game=" + year + season
			page = requests.get(website_link + city_link)
			self.assertTrue(page.status_code == 200)

	def test_cities_gui(self):
		browser = webdriver.Firefox()
		browser.get(website_link)
		nav_link = browser.find_element_by_link_text("Host Cities")
		nav_link.click()
		self.assertTrue("Host Cities" in browser.title)
		browser.quit()
	
	def test_each_city_gui_and_data(self):
		data = None
		with open("../host-cities/venues.json") as json_f:
			data = json.load(json_f)
		browser = webdriver.Firefox()
		page = browser.get(website_link + "/host-cities")
		imgs = browser.find_elements_by_tag_name("img")
		next = True
		page = 1 #TEST
		while next:
			for img in range(0,len(imgs)):
				next_button = browser.find_element_by_id("myTable_next")
				for i in range(0,page-1):
					next_button.click()
					next_button = browser.find_element_by_id("myTable_next")

				time.sleep(0.2)
				imgs = browser.find_elements_by_tag_name("img")
				if img >= len(imgs):
					break
				try:
					imgs[img].click()
				except:
					link = imgs[img].get_property("src").split("/")[-1].strip(".png")
					browser.get(website_link+"/host-cities/select?game="+link)

				print("checking: " +browser.current_url)
				key = browser.current_url.split("=")[1]
				
				title = browser.find_element_by_id("game-title")
				self.assertTrue(str(data[key]["year"])+" "+data[key]["season"] in title.text)
				
				browser.back()
			
			imgs = browser.find_elements_by_tag_name("img")
			next_button = browser.find_element_by_id("myTable_next")
			if("disabled" in  next_button.get_attribute("class") ):
				next = False	
			else:
				page+=1
		browser.quit()

def test_all_links():
	suite = unittest.TestSuite()
	suite.addTest(HostTests("test_each_city_link"))
	suite.addTest(HostTests("test_cities_link"))
	runner = unittest.TextTestRunner()
	runner.run(suite)

def test_gui():
	suite = unittest.TestSuite()
	suite.addTest(HostTests("test_cities_gui"))
	suite.addTest(HostTests("test_each_city_gui_and_data"))
	runner = unittest.TextTestRunner()
	runner.run(suite)


def run_all_tests():
	suite = unittest.TestSuite()
	suite.addTest(HostTests("test_cities_gui"))
	suite.addTest(HostTests("test_each_city_gui_and_data"))
	suite.addTest(HostTests("test_each_city_link"))
	suite.addTest(HostTests("test_cities_link"))
	runner = unittest.TextTestRunner()
	runner.run(suite)

if __name__ == "__main__":
	# test_all_links()
	# test_gui()
	run_all_tests()