from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import sys


def init_settings():
	return  {'url': 'https://coolgenerator.com/random-text-generator',
				'new_text': 'PURIFIED',
				'xpath_settings': {
					'button_generate': '/html/body/section[2]/div/div/div[1]/div[1]/div/div[2]/form/div[4]/div/button',
					'text_field': '/html/body/section[2]/div/div/div[1]/div[2]/ul/li/textarea',
				}
			}

def init_browser():
	# return webdriver.Chrome()
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

def new_text(browser, settings):
	xpath_settings = settings['xpath_settings']

	elem = browser.find_element_by_xpath(xpath_settings['button_generate'])
	elem.send_keys(Keys.RETURN)
	sleep(2)
	elem = browser.find_element_by_xpath(xpath_settings['text_field'])
	elem.send_keys(Keys.CONTROL, "A")
	elem.send_keys(settings['new_text'])

def main(argv):
	settings = init_settings()

	browser = init_browser()
	init_page(browser, settings['url'])
	new_text(browser, settings)

	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))