from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
options = Options()
options.add_argument(r'--user-data-dir=C:\Users\Piratena\Desktop\Repositorios\atenea-medran\Como-analizar-twitter\Downloading Twitter images\Screenshots\UserData')
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://www.twitter.com/")
sleep(30)