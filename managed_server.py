from selenium import webdriver
from selenium.webdriver.common.keys import Keys

########wait libraries ##########
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

xpaths = { 'submitButton' :"//input[@class='formButton']",
	   		'server' :"//a[@href='http://10.21.32.96:7001/console/console.portal?_nfpb=true&_pageLabel=CoreServerServerTablePage']",
			
			'managedserver' :"//a[@href='http://10.21.32.96:7001/console/console.portal?_nfpb=true&DispatcherPortletperspective=configuration-page&_pageLabel=DispatcherPage&DispatcherPortlethandle=com.bea.console.handles.JMXHandle%28%22com.bea%3AName%3Dosb_server1%2CType%3DServer%22%29']",
			
			'monitoring' :"//a[contains(concat(' ', @title, ' '), ' Monitoring- ')]",
			
			'performance' :"//a[contains(@title,'Monitoring') and contains(@title ,'Performance')]",
			
			
			'garbage' :"//button[@name='Garbage Collect']"
			#'garbage' :"//button[contains(@name,'Garbage') and contains(@title ,'Performance')]"
			
			
         }

browser = webdriver.Firefox()

browser.get('http://10.21.32.96:7001/console/login/LoginForm.jsp')


browser.find_element_by_name("j_username").send_keys('weblogic')  # Find the search box


browser.find_element_by_name("j_password").send_keys('welcome1')  # Find the search box


#Click Login button
browser.find_element_by_xpath(xpaths['submitButton']).click()

#################### end of 1st page ###########

browser.find_element_by_xpath(xpaths['server']).click()

browser.find_element_by_xpath(xpaths['managedserver']).click()

browser.find_element_by_xpath(xpaths['monitoring']).click()

browser.find_element_by_xpath(xpaths['performance']).click()

browser.find_element_by_xpath(xpaths['garbage']).click()

browser.quit()
