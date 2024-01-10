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
    sleep(3)

    try:  # Try close new introducion and tutorial
        enable_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".font-medium.items-center.whitespace-nowrap.focus\\:outline-none.inline-flex.bg-fill-3.dark\\:bg-dark-fill-3.hover\\:bg-fill-2.dark\\:hover\\:bg-dark-fill-2.dark\\:text-dark-label-2.rounded-full.px-10.py-\\[14px\\].text-xl.text-white"))
        )
        enable_button.click()

        skip_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "button[data-action='skip']"))
        )
        skip_button.click()
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    cpp_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//button[contains(text(), 'C++')]"))
    )
    cpp_button.click()

    python3_div = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//div[contains(text(), 'Python3')]"))
    )
    python3_div.click()

    sleep(1)
    html = browser.page_source
    browser.quit()

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('a', {'class': "no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"})
    title = re.sub('<.*?>', '', str(title))

    content = soup.find('div', {'class':
                                'view-lines monaco-mouse-cursor-text'})
    content = re.sub('<.*?>', '<>', str(content)).replace('\xa0', ' ')
    content = [unescape(x) for x in content.split('<>') if x]
    content = f"# {link}\n" + ''.join(
        ['\n' + x if x.startswith(('    ', 'class', '#')) else x
            for x in content])

    return (title, content)


if __name__ == "__main__":

    d = date.today()
    c = scrap_leetcode(input("Link: "))
    name = f"{d}_{c[0].replace('.', '', 1)}.py"
    with open(name, 'w') as file:
        file.write(c[1])
    print(f"'{name}' created")
