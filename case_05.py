from selenium import webdriver

import sys


def init_urls():
	return  ('https://bot.sannysoft.com',
			'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

def init_browser():
	from selenium.webdriver.chrome.options import Options
	
	option = Options()
	option.add_argument('user-agent=I`m a human!')
	option.add_argument('--disable-blink-features=AutomationControlled')
	option.add_experimental_option("detach", True)

	return webdriver.Chrome(options=option)
	# return webdriver.Chrome()

def init_page(browser, url):
	browser.get(url)

def main(argv):
	urls = init_urls()

	for url in urls:
		browser = init_browser()
		init_page(browser, url)

	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))