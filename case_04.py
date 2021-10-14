from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from time import sleep
import re

import sys


def init_settings():
	return  {'url': 'https://coolgenerator.com/random-text-generator',
				'lang_nums': [1, 7, 9, 13],
				'xpath_settings': {
					'button_generate': '/html/body/section[2]/div/div/div[1]/div[1]/div/div[2]/form/div[4]/div/button',
					'text_length': '/html/body/section[2]/div/div/div[1]/div[2]/p[1]',
					'language': '/html/body/section[2]/div/div/div[1]/div[1]/div/div[2]/form/div[1]/div/select',
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

def length_text(browser, settings):
	xpath_settings = settings['xpath_settings']
	answer = []

	for language in settings['lang_nums']:
		elem = browser.find_element_by_xpath(xpath_settings['language'])
		lang_list = elem.text.split('\n')
		answer.append(lang_list[language])

		elem = Select(elem)
		elem.select_by_index(language)
		elem = browser.find_element_by_xpath(xpath_settings['button_generate'])
		elem.send_keys(Keys.RETURN)
		sleep(2)

		elem = browser.find_element_by_xpath(xpath_settings['text_length'])
		res = re.search(r'\d+', elem.text)
		answer.append(res.group(0))

	return answer


def main(argv):
	settings = init_settings()

	browser = init_browser()
	init_page(browser, settings['url'])
	ans = length_text(browser, settings)
	
	for i, j in enumerate(ans):
		if i%2:
			print(f'{j}')
		else:
			print(f'Length in {j} is a ', end='')

	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))