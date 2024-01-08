from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import keyboard

print('running')

option = Options()
option.add_experimental_option("detach", True)

url = "https://humanbenchmark.com/tests/verbal-memory"
browser = webdriver.Chrome(options=option, keep_alive=True)

browser.get(url)
time.sleep(5)
browser.implicitly_wait(10)
# Open Chrome in debug mode
browser.maximize_window()
time.sleep(2)
screen_width, screen_height = pyautogui.size()
pyautogui.click(screen_width*.5, screen_height*.6)

words = []
count = 0

LIMIT = 100     #Set this to whatever score you want to stop at

while count < LIMIT:
    source = browser.page_source

    # Now, use BeautifulSoup to extract information from the website
    soup = BeautifulSoup(source, 'html.parser')

    # Find the word in the 'word' class
    span = soup.find('div', class_='word')
    word = span.get_text()
    if word not in words:
        words.append(word)
        pyautogui.click(screen_width*.53, screen_height*.5)
        count += 1
    else:
        pyautogui.click(screen_width*.45, screen_height*.5)
        count += 1
print("Type 'q' to quit browser")
if keyboard.is_pressed('q'):
    print('quitting')
    browser.quit()
