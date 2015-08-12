from selenium import webdriver

browser = webdriver.Chrome('/Users/Oliver/Downloads/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title

