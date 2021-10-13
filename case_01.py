from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys


def init_settings():
	return  {'url': 'https://github.com/login',
				'title': 'Sign in to GitHub · GitHub',
				'login': 'PURIFIED',
				'password': 'PURIFIED',
				'xpath_settings': {
					'login': '//*[@id="login_field"]',
					'password': '//*[@id="password"]',
					'input_button': '/html/body/div[3]/main/div/div[4]/form/div/input[12]'
				}
			}

def init_browser():
	import webbrowser as wb
	
	default_browser = wb.get()
	browser_type = default_browser.name.casefold()
	
	if browser_type == 'firefox':
		return webdriver.Firefox()
	elif browser_type == 'chrome':
		return webdriver.Chrome()
	else:
		print('ERROR!\nSomething is wrong!\nUnknow browser type!')
		exit(1)

def init_page(browser, url):
	browser.get(url)

def login(browser, settings):
	xpath_settings = settings['xpath_settings']

	elem = browser.find_element_by_xpath(xpath_settings['login'])
	elem.send_keys(settings['login'])
	elem = browser.find_element_by_xpath(xpath_settings['password'])
	elem.send_keys(settings['password'])
	elem = browser.find_element_by_xpath(xpath_settings['input_button'])
	elem.send_keys(Keys.RETURN)

def main(argv):
	settings = init_settings()

	browser = init_browser()
	init_page(browser, settings['url'])
	login(browser, settings)

	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))