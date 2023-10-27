from bs4 import BeautifulSoup
from time import sleep
import re
from html import unescape
from datetime import date

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrap_leetcode(link):
    option = Options()
    option.add_argument('-headless')
    
    browser = webdriver.Firefox(options=option)
    browser.get(link)
    sleep(4)
    css_selector = '.flex.cursor-pointer.items-center.rounded.text-left.focus\:outline-none.whitespace-nowrap.text-label-2.dark\:text-dark-label-2.bg-transparent.dark\:bg-dark-transparent.hover\:bg-transparent.dark\:hover\:bg-transparent.hover\:text-label-1.dark\:hover\:text-dark-label-1.active\:bg-transparent.dark\:active\:bg-dark-transparent.ml-2.px-2.py-1\\.5.pr-1.font-medium.text-xs.group'
    
    button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))    
    button.click()

    elements = browser.find_elements(By.CSS_SELECTOR, '.relative.flex.h-8.cursor-pointer.select-none.py-1\\.5.pl-2.text-label-2.dark\\:text-dark-label-2')

    for element in elements:
        if 'Python3' in element.text:
            element.click()
            break
    sleep(1)
    html = browser.page_source
    browser.quit()

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('a', {'class': 'mr-2 text-label-1 dark:text-dark-label-1 hover:text-label-1 dark:hover:text-dark-label-1 text-lg font-medium'})
    content = soup.find('div', {'class': 'view-lines monaco-mouse-cursor-text'})
    
    title = re.sub('<.*?>', '', str(title))
    # print(title)
    
    content = [unescape(x) for x in re.sub('<.*?>', '<>', str(content)).replace('\xa0', ' ').split('<>') if x]
    content = f"# {link}\n" + ''.join(['\n' + x if x.startswith(('    ', 'class', '#')) else x for x in content])
    # print(content)
    return (title, content)
    
if __name__=="__main__":
    
    d = date.today()
    
    c = scrap_leetcode(input("Link: "))
    name = f"{d}_{c[0].replace('.', '', 1)}.py"
    with open(name, 'w') as file:
        file.write(c[1])
    print(f"'{name}' created")
    